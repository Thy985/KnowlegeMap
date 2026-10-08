"""Capability Graph（v2 · 底层图）。

树与图分工：
- Tree（trees.py）：层级组织、任务分解（Domain Tree 静态 / Capability Tree 动态）。
- Graph（本模块）：跨领域复用、依赖关系、组合关系。

典型：http-interaction 同时属于 Web Security / API Testing / Web Automation /
Browser Agents——树无法表达多 parent，图通过 domain membership 表达复用。
树是图的"任务视图"：同一图节点可在不同任务的树中出现。
"""
from collections import defaultdict
from typing import Dict, List, Set

from .knowledge import CAPABILITIES


# capability → domains（多对多，跨域复用）
DOMAIN_MEMBERSHIP: Dict[str, List[str]] = {
    "reconnaissance": ["web-security", "red-teaming"],
    "endpoint-discovery": ["web-security", "api-testing"],
    "http-interaction": ["web-security", "api-testing",
                         "web-automation", "browser-agents"],
    "vulnerability-detection": ["web-security", "red-teaming"],
    "request-replay": ["web-security"],
    "result-aggregation": ["web-automation", "agent-evaluation"],
    "evidence-collection": ["web-security", "agent-evaluation"],
    "reporting": ["web-security", "agent-evaluation"],
    "browser-interaction": ["web-security", "web-automation",
                            "browser-agents", "e2e-testing"],
    "sandbox-execution": ["web-automation", "developer-tools"],
    "agent-memory": ["agent-memory", "agent-runtime"],
    "agent-evaluation": ["agent-evaluation"],
    "multi-agent-orchestration": ["agent-runtime"],
    "local-inference": ["runtime"],
    "observability": ["observability"],
    "protocol-interop": ["developer-tools", "agent-runtime"],
    "security-governance": ["governance"],
    "runtime-defense": ["runtime-defense", "governance"],
    "long-term-memory": ["agent-memory"],
    "state-persistence": ["agent-runtime"],
    "scheduling": ["agent-runtime"],
    "failure-recovery": ["agent-runtime"],
    "monitoring": ["observability", "runtime-defense"],
    "self-improvement": ["agent-runtime", "agent-evaluation"],
    "privacy-guard": ["governance"],
    "embedding": ["agent-memory"],
    "assertion": ["agent-evaluation", "e2e-testing"],
}


class CapabilityGraph:
    """能力图：节点=扁平能力；边=依赖（prerequisites）+ domain membership。"""

    def __init__(self) -> None:
        self.nodes: Set[str] = set(CAPABILITIES.keys())
        self.depends: Dict[str, List[str]] = {
            cap: list(CAPABILITIES[cap].get("prerequisites", []))
            for cap in self.nodes}
        self.membership: Dict[str, List[str]] = {
            cap: list(DOMAIN_MEMBERSHIP.get(cap, [])) for cap in self.nodes}
        self.domain_caps: Dict[str, Set[str]] = defaultdict(set)
        for cap, doms in self.membership.items():
            for d in set(doms):
                self.domain_caps[d].add(cap)

    # ---- 跨域复用查询 ----
    def domains_of(self, cap: str) -> List[str]:
        return sorted(set(self.membership.get(cap, [])))

    def capabilities_in(self, domain: str) -> List[str]:
        return sorted(self.domain_caps.get(domain, set()))

    def shared_capabilities(self, d1: str, d2: str) -> List[str]:
        """两个领域复用的能力（图的核心价值）。"""
        return sorted(self.domain_caps.get(d1, set()) &
                      self.domain_caps.get(d2, set()))

    def reusable_cross_domain(self, min_domains: int = 2) -> List[str]:
        return sorted(c for c, doms in self.membership.items()
                      if len(set(doms)) >= min_domains)

    # ---- 依赖查询 ----
    def dependents(self, cap: str) -> List[str]:
        """直接依赖 cap 的能力。"""
        return sorted(c for c, prereqs in self.depends.items()
                      if cap in prereqs)

    def removal_impact(self, cap: str) -> List[str]:
        """删掉 cap 的传递影响（沿依赖边闭包）。"""
        impact: Set[str] = set()
        frontier = [cap]
        while frontier:
            cur = frontier.pop()
            for d in self.dependents(cur):
                if d not in impact:
                    impact.add(d)
                    frontier.append(d)
        return sorted(impact)

    # ---- 渲染 ----
    def render(self) -> str:
        lines: List[str] = ["# Capability Graph（跨域复用视图）", ""]
        lines.append("## 跨域复用能力（≥2 领域）")
        for cap in self.reusable_cross_domain():
            lines.append(f"- **{cap}** → {', '.join(self.domains_of(cap))}")
        lines.append("")
        lines.append("## 领域 → 能力")
        for d in sorted(self.domain_caps):
            lines.append(f"- {d}: {', '.join(self.capabilities_in(d))}")
        return "\n".join(lines)
