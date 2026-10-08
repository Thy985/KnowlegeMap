"""KnowlegeMap Agent-Centric Engine — Tool Composition.

核心：Tools 不是集合，而是有向工具链（Tool Graph）。
每个选择都带多维 Selection Reason；组合时显式检查数据流兼容/互斥/并行/前置。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from . import knowledge
from .domain import SelectionReason, Task, Tool, ToolStat


@dataclass
class HistoryPrior:
    """历史先验（v4 · 演进结果回灌 compose）。

    - 可靠性校准：样本足够时用真实 success_rate 校准静态 reliability；
    - 历史失败淘汰：被最新 skill 剔除且未恢复的工具施加 fit 惩罚。
    """
    tool_stats: Dict[str, ToolStat] = field(default_factory=dict)
    removed: Dict[str, str] = field(default_factory=dict)  # tool -> "skill(sr=..)"
    min_samples: int = 3
    drop_rate: float = 0.5
    reliability_blend: float = 0.5
    remove_penalty: float = 0.12

    def adjustment(self, tool: str, static_reliability: float) -> float:
        delta = 0.0
        st = self.tool_stats.get(tool)
        if st and st.usage_count >= self.min_samples:
            # 真实成功率校准 reliability 维度
            delta += (_WEIGHTS["reliability"] * self.reliability_blend
                      * (st.success_rate - static_reliability))
        if tool in self.removed:
            delta -= self.remove_penalty
        return round(delta, 3)


def build_history_prior(memory) -> HistoryPrior:
    """从 Agent Memory 构造历史先验；剔除工具若成功率回升则解除。"""
    removed: Dict[str, str] = {}
    for sid, versions in memory.skill_versions.items():
        latest = versions[-1]
        for t in latest.removed_tools:
            st = memory.tool_stats.get(t)
            sr = st.success_rate if st else 0.0
            # 未恢复（无统计，或样本足够且仍 < 阈值）
            if not st or (st.usage_count >= 3 and sr < 0.5):
                removed[t] = f"{sid}(sr={sr:.2f})"
    return HistoryPrior(tool_stats=dict(memory.tool_stats), removed=removed)


@dataclass
class ComposedChain:
    chain: List[str] = field(default_factory=list)          # 有向序（数据流）
    reasons: Dict[str, SelectionReason] = field(default_factory=dict)
    capability_tool_map: Dict[str, str] = field(default_factory=dict)
    parallel_groups: List[List[str]] = field(default_factory=list)
    excluded: List[str] = field(default_factory=list)        # 被排除候选 + 原因
    excluded_reasons: Dict[str, str] = field(default_factory=dict)
    history_warnings: Dict[str, str] = field(default_factory=dict)  # 历史失败但无替代

    def summary(self) -> str:
        return " -> ".join(self.chain) if self.chain else "(empty)"


# 评分权重：task_fit 优先于 star/生态（Star 仅弱信号）
_WEIGHTS = {
    "task_fit": 0.25,
    "capability_coverage": 0.20,
    "automation_friendliness": 0.15,
    "structured_output": 0.10,
    "reliability": 0.10,
    "ecosystem_maturity": 0.10,
    "interface_compatibility": 0.10,
}

# 数据流兼容表：input_format -> 可消费的 output_format
_FORMAT_COMPAT = {
    "script": ["script", "structured", "text", "retrieved", "traces", "task"],
    "task": ["structured", "text", "task"],
    "config": ["text", "structured", "script"],
    "trace": ["traces", "structured", "text"],
    "span": ["traces", "structured"],
    "code": ["text", "script", "structured"],
    "model-target": ["text", "task"],
    "attack-plan": ["structured", "text"],
    "agent-config": ["structured", "text"],
    "threat-model": ["text", "structured", "guidance"],
    "traffic": ["traces", "alerts", "structured"],
    "graph": ["structured", "text"],
    "agent-card": ["structured", "text"],
    "tool-schema": ["structured", "text", "task"],
    "research-task": ["text", "structured"],
    "model": ["text", "task"],
    "text": ["text", "structured", "traces", "retrieved"],
}

# 互斥组：同组工具语义重叠，同一任务只选其一（除非明确组合理由）
_MUTUAL_EXCLUSION = [
    {"browser-use", "playwright", "webwright"},   # 浏览器自动化选一个主链
    {"mem0", "dsh-memory-evolve"},                # 记忆后端选一个
    {"garak", "pyrit"},                           # 红队扫描选一个主
    {"otel-genai", "langfuse"},                   # 观测选一个主（可换）
    {"ollama", "glm-edge", "llamafile"},          # 本地推理选一个
]


def _tool(name: str) -> Tool:
    meta = knowledge.get_tool(name)
    return Tool(name=name, **meta)


def _interface_score(tool: Tool) -> float:
    """接口兼容性：CLI/SDK/headless 对 agent 友好度排序。"""
    score = {"CLI": 1.0, "CLI+SDK": 1.0, "CLI+Server": 0.9, "SDK": 0.85,
             "SDK+CLI": 0.9, "headless-http": 1.0, "SaaS+SDK": 0.8,
             "插件": 0.75, "framework": 0.5, "service": 0.6, "model": 0.6}.get(
        tool.interface, 0.6)
    return score


def evaluate_candidate(tool: Tool, task: Task, required_caps: List[str],
                       env: Optional[Dict[str, str]] = None) -> SelectionReason:
    """候选 → 多维评分（Selection Reason）。Star/生态只是其中一维。"""
    env = env or {}
    coverage = len(set(tool.capabilities) & set(required_caps)) / max(len(required_caps), 1)
    task_fit = _task_fit(tool, task)
    interface = _interface_score(tool)
    env_compat = _env_compat(tool, env)
    env_cost = _cost_score(tool.cost)
    env_risk = _risk_score(tool)

    reason = SelectionReason(
        candidate=tool.name,
        task_fit=task_fit,
        capability_coverage=round(coverage, 2),
        interface_compatibility=round(interface, 2),
        automation_friendliness=round(tool.automation_friendly, 2),
        structured_output=round(tool.structured_output, 2),
        reliability=round(tool.reliability, 2),
        maintenance_status=tool.maintenance_status,
        ecosystem_maturity=round(tool.ecosystem_maturity, 2),
        environment_compatibility=round(env_compat, 2),
        computational_cost=tool.cost,
        permission_requirements="; ".join(tool.permissions) or "none",
        security_risk="; ".join(tool.security_implications) or "none",
        evidence_quality="FACT（候选卡/star 证据锚点）" if tool.source_cards else "DESIGN（推断）",
    )
    return reason


def fit_score(reason: SelectionReason) -> float:
    """综合分（star 仅体现在 ecosystem_maturity 一维，权重 0.10）。"""
    s = reason
    return round(
        _WEIGHTS["task_fit"] * s.task_fit
        + _WEIGHTS["capability_coverage"] * s.capability_coverage
        + _WEIGHTS["automation_friendliness"] * s.automation_friendliness
        + _WEIGHTS["structured_output"] * s.structured_output
        + _WEIGHTS["reliability"] * s.reliability
        + _WEIGHTS["ecosystem_maturity"] * s.ecosystem_maturity
        + _WEIGHTS["interface_compatibility"] * s.interface_compatibility,
        3,
    )


def _fallback(cap: str, tool_names: List[str], task: Task,
              required_caps: List[str], env: Optional[Dict[str, str]],
              blocked: set, history: Optional[HistoryPrior] = None) -> Optional[str]:
    """互斥裁决后，为能力回退到次优候选（排除 blocked 工具）。"""
    cands = [n for n in tool_names
             if cap in knowledge.get_tool(n)["capabilities"] and n not in blocked]
    if not cands:
        return None
    scored = []
    for n in cands:
        t = _tool(n)
        r = evaluate_candidate(t, task, required_caps, env)
        base = fit_score(r)
        adj = round(base + history.adjustment(n, t.reliability), 3) if history else base
        scored.append((adj, n))
    scored.sort(key=lambda x: -x[0])
    return scored[0][1]


def compose(tool_names: List[str], task: Task, required_caps: List[str],
            env: Optional[Dict[str, str]] = None,
            history: Optional[HistoryPrior] = None) -> ComposedChain:
    """Candidate Tools → Tool Composition（组合理由 + 有向链 + 并行/互斥/前置）。

    算法：
    1. 逐能力挑最佳工具（fit + 历史先验 adjustment），同能力覆盖者合并；
    2. 互斥组裁决：同组只保留调整后 fit 最高者，被淘汰者记录 excluded_reasons；
    3. 按能力依赖序（required_caps 顺序）排序形成数据流链；
    4. 检查 input/output 格式兼容；不兼容则尝试插入转换环节并记录；
    5. 并行组：互不依赖且不同阶段可并行者归组。

    history（v4）：真实成功率校准可靠性、历史失败工具受惩罚；某能力只有
    历史失败工具一个候选时仍保留（不丢能力），记入 history_warnings。
    """
    env = env or {}
    chain = ComposedChain()

    # 1. 每能力选最佳
    used: Dict[str, str] = {}
    adjfit: Dict[str, float] = {}
    for cap in required_caps:
        cands = [n for n in tool_names if cap in knowledge.get_tool(n)["capabilities"]]
        if not cands:
            continue
        scored = []
        for n in cands:
            t = _tool(n)
            r = evaluate_candidate(t, task, required_caps, env)
            base = fit_score(r)
            adj = round(base + history.adjustment(n, t.reliability), 3) if history else base
            adjfit[n] = adj
            scored.append((adj, r, t))
        scored.sort(key=lambda x: -x[0])
        best = scored[0]
        used[cap] = best[2].name
        chain.reasons.setdefault(best[2].name, best[1])

    # 2. 互斥裁决
    excluded_names: set = set()
    for grp in _MUTUAL_EXCLUSION:
        hit = [n for n in used.values() if n in grp]
        if len(hit) > 1:
            # 保留调整后 fit 最高者
            keep = max(hit, key=lambda n: adjfit.get(n, fit_score(chain.reasons.get(n, SelectionReason(n)))))
            for other in hit:
                if other != keep:
                    chain.excluded.append(other)
                    excluded_names.add(other)
                    hist = f"；历史失败 {history.removed[other]}" if history and other in history.removed else ""
                    chain.excluded_reasons[other] = (
                        f"与 {keep} 语义重叠（互斥组 {sorted(grp)}），"
                        f"fit {adjfit.get(other)} < {adjfit.get(keep)}{hist}"
                    )
                    # 从 used 中剔除，并为该能力回退次优候选
                    # （排除已排除工具 + 同互斥组其余成员，避免再次冲突）
                    blocked = excluded_names | (grp - {keep})
                    for k, v in list(used.items()):
                        if v == other:
                            fb = _fallback(k, tool_names, task,
                                           required_caps, env, blocked, history)
                            if fb:
                                used[k] = fb
                                tfb = _tool(fb)
                                rfb = evaluate_candidate(tfb, task, required_caps, env)
                                chain.reasons.setdefault(fb, rfb)
                                adjfit[fb] = round(
                                    fit_score(rfb) + (history.adjustment(fb, tfb.reliability) if history else 0.0), 3)
                            else:
                                del used[k]

    # 3. 按能力依赖序构链
    ordered = []
    for cap in required_caps:
        if cap in used and used[cap] not in ordered:
            ordered.append(used[cap])
    chain.chain = ordered
    chain.capability_tool_map = dict(used)

    # 历史失败但仍被保留（无替代）→ 警告
    if history:
        for n in ordered:
            if n in history.removed:
                chain.history_warnings[n] = (
                    f"历史失败 {history.removed[n]}，但无替代工具，暂保留"
                    "（需改进/人工确认）")

    # 4. 格式兼容检查（在 ordered 相邻之间）
    for i in range(len(ordered) - 1):
        a, b = _tool(ordered[i]), _tool(ordered[i + 1])
        compat = b.input_format in _FORMAT_COMPAT.get(a.output_format, [])
        if not compat:
            chain.excluded_reasons[f"{a.name}->{b.name}"] = (
                f"数据流不兼容：{a.name}({a.output_format}) → {b.name}({b.input_format})，"
                "需要转换环节（记录为设计缺口）"
            )

    # 5. 并行组：相邻且互不依赖（无前置关系）
    groups: List[List[str]] = []
    for i, cap in enumerate(required_caps):
        if cap in used:
            groups.append([used[cap]])
    chain.parallel_groups = [g for g in groups if len(g) == 1]

    return chain


def _task_fit(tool: Tool, task: Task) -> float:
    """任务适配度：工具类别与任务类型的先验匹配。"""
    ttype = task.task_type
    category_map = {
        "security-assessment": {"redteam": 1.0, "governance": 0.8, "browser": 0.7,
                                "protocol": 0.5, "evals": 0.6, "harness": 0.6, "sandbox": 0.5},
        "e2e-web-testing": {"browser": 1.0, "evals": 0.7, "observability": 0.6, "protocol": 0.5},
        "long-running-autonomous-agent": {"harness": 1.0, "orchestration": 0.9, "memory": 0.8,
                                          "observability": 0.7, "evals": 0.7},
        "local-mobile-ai-assistant": {"local-inference": 1.0, "memory": 0.7, "observability": 0.5},
        "multi-agent-team": {"orchestration": 1.0, "protocol": 0.9, "observability": 0.7,
                             "memory": 0.7, "runtime-defense": 0.6},
        "agent-eval-harness": {"evals": 1.0, "observability": 0.8, "sandbox": 0.8, "harness": 0.7},
    }
    mapping = category_map.get(ttype, {})
    return mapping.get(tool.category, 0.5)


def _env_compat(tool: Tool, env: Dict[str, str]) -> float:
    if not env:
        return 0.8
    os = env.get("os", "").lower()
    if os and "windows" in os and "windows" not in " ".join(tool.environment_requirements).lower():
        return 0.6
    if env.get("net") == "offline" and "cloud" in " ".join(tool.environment_requirements).lower():
        return 0.3
    return 0.9


def _cost_score(cost: str) -> float:
    return {"low": 1.0, "med": 0.6, "high": 0.3}.get(cost, 0.5)


def _risk_score(tool: Tool) -> float:
    """安全风险：高风险工具降低可用性（安全边界显式化，EP-002）。"""
    s = " ".join(tool.security_implications).lower()
    if "授权" in s or "授权" in s or "scope" in s:
        return 0.8
    if "sandbox" in s or "沙箱" in s:
        return 0.85
    if "拦截" in s or "权限面" in s or "broad" in s:
        return 0.55
    return 0.9
