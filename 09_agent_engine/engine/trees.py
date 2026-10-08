"""Tree 层（v2）：Domain Tree + Capability Tree + JIT 展开。

- Domain Tree：静态组织领域知识（领域由什么组成）。
- Capability Tree：任务动态实例化（为完成这个任务需要什么能力层级），
  每个节点运行时携带 current_state / gap / candidate_tools / selected_tool。
- JIT：按 Agent 状态剪枝，已具备分支不展开，只展开缺失分支。

树与图分工：Tree 负责层级组织与任务分解；跨域复用 / 依赖关系见
capability_graph.py（Capability Graph），树是图的任务视图。
"""
from typing import Any, Dict, List, Optional

from .domain import CapabilityNode, DomainNode
from .knowledge import (DOMAIN_TREE, CAPABILITY_TREE_TEMPLATES, TASK_TYPES,
                        TOOLS)


# ============================================================
# Domain Tree
# ============================================================
def build_domain_tree() -> Dict[str, DomainNode]:
    """从 DOMAIN_TREE 构造 DomainNode 索引（保留 parent/children）。"""
    nodes: Dict[str, DomainNode] = {}

    def walk(raw: Dict[str, Any], parent: Optional[str]) -> None:
        for did, spec in raw.items():
            children = spec.get("children", {})
            node = DomainNode(id=did, name=spec["name"], parent=parent,
                              children=[], description=spec.get("description", ""))
            if isinstance(children, dict):
                node.children = list(children.keys())
                nodes[did] = node
                walk(children, did)
            else:  # list：子领域叶子（可能跨分支复用，单 parent 取首次）
                for c in children:
                    node.children.append(c)
                    if c not in nodes:
                        nodes[c] = DomainNode(
                            id=c, name=c.replace("-", " ").title(), parent=did)
                nodes[did] = node

    walk(DOMAIN_TREE, None)
    return nodes


# ============================================================
# Capability Tree（任务动态实例化）
# ============================================================
def instantiate_capability_tree(task_type: str) -> Dict[str, CapabilityNode]:
    """实例化：建 root + 第一层分支（分支默认未展开，等 JIT 判定）。"""
    nodes: Dict[str, CapabilityNode] = {}
    root_id = f"root.{task_type}"

    if task_type in CAPABILITY_TREE_TEMPLATES:
        tpl = CAPABILITY_TREE_TEMPLATES[task_type]
        branches = tpl["branches"]
        root = CapabilityNode(id=root_id, name=tpl["root_name"],
                              children=[b["id"] for b in branches])
        nodes[root_id] = root
        for b in branches:
            _build_branch(b, root_id, nodes)
    else:
        # 无模板：从 flat TASK_TYPES 投影为一层树
        spec = TASK_TYPES.get(task_type, {"required_capabilities": []})
        caps = spec["required_capabilities"]
        root = CapabilityNode(id=root_id, name=task_type, children=list(caps))
        nodes[root_id] = root
        for cap in caps:
            nodes[cap] = CapabilityNode(
                id=cap, name=cap.replace("-", " ").title(),
                parent=root_id, maps_to=cap)
    return nodes


def _build_branch(b: Dict[str, Any], parent: str,
                  nodes: Dict[str, CapabilityNode]) -> None:
    bid = b["id"]
    nodes[bid] = CapabilityNode(
        id=bid, name=b["name"], parent=parent,
        children=[f"{bid}.{c['id']}" for c in b["children"]],
        maps_to=b["maps_to"], leaf_tags=b["leaf_tags"])
    for c in b["children"]:
        cid = f"{bid}.{c['id']}"
        nodes[cid] = CapabilityNode(
            id=cid, name=c["name"], parent=bid,
            maps_to=c["maps_to"], leaf_tags=c["leaf_tags"])


# ============================================================
# JIT Capability Expansion
# ============================================================
def _agent_conf(agent: Any, cap_id: str) -> float:
    return float(agent.capabilities.get(cap_id, 0.0))


def root_node(nodes: Dict[str, CapabilityNode]) -> CapabilityNode:
    return next(n for n in nodes.values() if n.parent is None)


def jit_expand(nodes: Dict[str, CapabilityNode], agent: Any,
                threshold: float = 0.5) -> Dict[str, CapabilityNode]:
    """按 Agent 状态剪枝：

    - 分支已具备（conf ≥ threshold）→ gap=False，剪枝不展开；
    - 分支缺失 → gap=True，展开到叶子，逐叶子判定状态。
    """
    root = root_node(nodes)
    for bid in root.children:
        branch = nodes[bid]
        conf = _agent_conf(agent, branch.maps_to)
        branch.current_state = conf
        if conf >= threshold:
            branch.gap = False
            branch.expanded = False
        else:
            branch.gap = True
            branch.expanded = True
            for cid in branch.children:
                leaf = nodes[cid]
                lconf = _agent_conf(agent, leaf.maps_to)
                leaf.current_state = lconf
                leaf.gap = lconf < threshold
                leaf.expanded = True
    return nodes


def missing_capabilities(nodes: Dict[str, CapabilityNode]) -> List[str]:
    """收集 JIT 展开后判定为缺失的扁平能力（去重，保序）。"""
    seen: List[str] = []
    root = root_node(nodes)
    for bid in root.children:
        branch = nodes[bid]
        if branch.gap and branch.maps_to not in seen:
            seen.append(branch.maps_to)
        if branch.expanded:
            for cid in branch.children:
                leaf = nodes[cid]
                if leaf.gap and leaf.maps_to not in seen:
                    seen.append(leaf.maps_to)
    return seen


# ============================================================
# 节点级工具发现（能力驱动）
# ============================================================
def _discover_for_node(node: CapabilityNode) -> List[str]:
    from .discovery import discover_for_capability
    cands = list(discover_for_capability(node.maps_to))
    if node.leaf_tags:
        for tname, t in TOOLS.items():
            blob = " ".join([t["category"], tname] +
                            t.get("capabilities", [])).lower()
            if any(tag.lower() in blob for tag in node.leaf_tags):
                if tname not in cands:
                    cands.append(tname)
    return cands[:6]


def discover_tools_for_tree(nodes: Dict[str, CapabilityNode]) -> None:
    """对 gap 节点做能力驱动发现，候选填入 candidate_tools。"""
    root = root_node(nodes)
    for bid in root.children:
        branch = nodes[bid]
        if not branch.gap:
            continue
        if branch.children:
            for cid in branch.children:
                leaf = nodes[cid]
                if leaf.gap:
                    leaf.candidate_tools = _discover_for_node(leaf)
        else:
            branch.candidate_tools = _discover_for_node(branch)


def annotate_selections(nodes: Dict[str, CapabilityNode],
                        capability_tool_map: Dict[str, str]) -> None:
    """把 composed chain 的选择回填到节点 selected_tool。"""
    root = root_node(nodes)
    for bid in root.children:
        branch = nodes[bid]
        targets = [bid] + branch.children
        for cid in targets:
            node = nodes[cid]
            chosen = capability_tool_map.get(node.maps_to)
            if chosen and node.gap:
                node.selected_tool = chosen


# ============================================================
# 渲染
# ============================================================
def render_tree(nodes: Dict[str, CapabilityNode]) -> str:
    """渲染 Capability Tree（含 state / gap / selected）。"""
    root = root_node(nodes)
    lines: List[str] = [f"{root.name}（{root.id}）"]
    for bid in root.children:
        b = nodes[bid]
        mark = "✅" if not b.gap else "❌"
        if not b.expanded and not b.gap:
            mark = "✅（已具备，JIT 剪枝）"
        lines.append(f"├── {b.name} {mark} conf={b.current_state:.2f}")
        if b.expanded:
            kids = b.children
            for i, cid in enumerate(kids):
                leaf = nodes[cid]
                lmark = "✅" if not leaf.gap else "❌"
                sel = f" → {leaf.selected_tool}" if leaf.selected_tool else ""
                prefix = "│   └── " if i == len(kids) - 1 else "│   ├── "
                lines.append(f"{prefix}{leaf.name} {lmark}{sel}")
    return "\n".join(lines)


def render_domain_tree() -> str:
    nodes = build_domain_tree()
    lines: List[str] = []
    roots = [n for n in nodes.values() if n.parent is None]
    for r in roots:
        lines.append(f"{r.name}")
        for c in r.children:
            child = nodes.get(c)
            name = child.name if child else c
            lines.append(f"└── {name}")
    return "\n".join(lines)
