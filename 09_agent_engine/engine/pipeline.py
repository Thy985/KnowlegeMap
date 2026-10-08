"""KnowlegeMap Agent-Centric Engine — Pipeline（最小闭环主流程）。

链路：Task → Capability Extraction → Gap Analysis → Tool/Project Discovery
     → Tool Composition → Workflow → Evaluation → Memory（→ Capability Evolution）

安全边界：Agent-Centric ≠ 无限自治。risk_level 高 → 强制 approval（EP-002）。
"""
from __future__ import annotations

from typing import Callable, Dict, List, Optional

from . import knowledge
from .capability_graph import CapabilityGraph
from .composition import ComposedChain, compose, evaluate_candidate, fit_score
from .discovery import decompose_task, discover_for_capability, gap_analysis
from .domain import (Agent, AgentMemory, CapabilityNode, Evidence,
                     SelectionReason, Task, TaskRun)
from .evaluation import evaluate_run, update_agent_capabilities
from .memory import (MemoryStore, apply_post_task_learning, evolve_workflow,
                     reuse_historical_workflow)
from .skill_evolution import evolve_skills_for_caps
from .trees import (annotate_selections, discover_tools_for_tree,
                    instantiate_capability_tree, jit_expand,
                    missing_capabilities as tree_missing, render_tree)
from .workflow import synthesize_workflow


class PipelineResult:
    """一次 Agent Task Expansion 的完整产物（可渲染/可导出）。"""

    def __init__(self, task: Task, agent: Agent):
        self.task = task
        self.agent = agent
        self.required_capabilities: List[str] = []
        self.unknown_capabilities: List[str] = []
        self.missing_capabilities: List[str] = []
        self.discovered_tools: Dict[str, List[str]] = {}
        self.tree_nodes: Dict[str, CapabilityNode] = {}
        self.capability_graph: CapabilityGraph = CapabilityGraph()
        self.chain: Optional[ComposedChain] = None
        self.workflow = None
        self.run: Optional[TaskRun] = None
        self.evaluation = None
        self.approval_required: bool = False
        self.history_reused: bool = False
        self.history_source: Optional[str] = None
        self.evolved_skills: List = []

    def render_report(self) -> str:
        """人读报告：完整回答"为什么选这些工具/删掉 X 会损失什么"。"""
        lines = []
        lines.append(f"# Agent Task Expansion：{self.task.objective}")
        lines.append(f"task_type={self.task.task_type} risk={self.task.risk_level} "
                     f"approval_required={self.approval_required}")
        lines.append("")
        lines.append("## 1. Required Capabilities（任务→能力分解）")
        lines.append(", ".join(self.required_capabilities) or "(none)")
        if self.unknown_capabilities:
            lines.append("_未知能力发现（目标解析）_：" + ", ".join(self.unknown_capabilities))
        lines.append("")
        lines.append("## 2. Capability Gap（已有 vs 需求）")
        lines.append("missing: " + ", ".join(self.missing_capabilities) or "(none)")
        lines.append("")
        lines.append("## 2.1 Capability Tree（任务动态实例化 · JIT 展开）")
        lines.append("```")
        lines.append(render_tree(self.tree_nodes) if self.tree_nodes else "(none)")
        lines.append("```")
        lines.append("")
        lines.append("## 3. Tool Discovery（能力驱动，非关键词驱动）")
        for cap, tools in self.discovered_tools.items():
            lines.append(f"- {cap}: {', '.join(tools)}")
        lines.append("")
        lines.append("## 4. Tool Composition（组合理由）")
        if self.chain:
            lines.append(f"工具链：{self.chain.summary()}")
            for name, reason in self.chain.reasons.items():
                lines.append(f"- **{name}**  fit={fit_score(reason):.3f}  "
                             f"task_fit={reason.task_fit} coverage={reason.capability_coverage} "
                             f"auto={reason.automation_friendliness} structured={reason.structured_output} "
                             f"reliability={reason.reliability} eco={reason.ecosystem_maturity}")
                lines.append(f"  - 理由：{reason.note or '详见各维评分'}；"
                             f"权限={reason.permission_requirements}；风险={reason.security_risk}")
            if self.chain.excluded:
                lines.append("**排除候选**：")
                for name in self.chain.excluded:
                    lines.append(f"- {name}：{self.chain.excluded_reasons.get(name, '')}")
            if self.chain.excluded_reasons:
                incompat = {k: v for k, v in self.chain.excluded_reasons.items()
                            if "数据流" in v or "不兼容" in v}
                if incompat:
                    lines.append("**数据流缺口**（需转换环节）：")
                    for k, v in incompat.items():
                        lines.append(f"- {k}: {v}")
        lines.append("")
        lines.append("## 5. Workflow")
        if self.workflow:
            lines.append(f"v{self.workflow.version}（{self.workflow.evolution_reason or '首版'}）")
            for s in self.workflow.stages:
                lines.append(f"- {s.stage_id} [{s.goal}] tools={s.tools} dep={s.depends_on or '-'}")
                lines.append(f"  - checkpoint: {s.checkpoint}")
                lines.append(f"  - recovery: {s.failure_recovery}")
        if self.history_reused:
            lines.append(f"_复用历史工作流（{self.history_source}）_" if self.history_source else "")
        lines.append("")
        lines.append("## 6. Evaluation")
        if self.evaluation:
            lines.append(f"score={self.evaluation.score:.3f} failure={self.evaluation.failure or 'none'} "
                         f"reproducibility={self.evaluation.reproducibility}")
            for e in self.evaluation.evidence:
                lines.append(f"- {e.source} ({e.type}): {e.supporting_observation}")
        lines.append("")
        lines.append("## 7. Memory Update")
        lines.append(f"run_id={self.run.run_id if self.run else 'n/a'}；"
                     "工具统计/工作流版本/失败模式已回写 Agent Operational Memory")
        lines.append("")
        lines.append("## 7.1 Skill Evolution（tool_stats 数据驱动）")
        if self.evolved_skills:
            for sv in self.evolved_skills:
                lines.append(f"- **{sv.skill_id}** → v{sv.version}：{sv.evolution_reason}")
                if sv.removed_tools:
                    lines.append(f"  - 剔除：{', '.join(sv.removed_tools)}")
                if sv.required_tools:
                    lines.append(f"  - 工具（重排后）：{', '.join(sv.required_tools)}")
        else:
            lines.append("(本次无显著演进：工具样本不足或表现稳定)")
        lines.append("")
        lines.append("---")
        lines.append(f"证据纪律：所有工具/能力锚点见 03_expansion_queue/candidates + "
                     "00_bootstrap/00_starred_reference.md（FACT 优先）。")
        return "\n".join(lines)


def run_agent_task(
    agent: Agent,
    task: Task,
    memory: Optional[AgentMemory] = None,
    store: Optional[MemoryStore] = None,
    tool_observer: Optional[Callable[[str, str], dict]] = None,
    observations: Optional[Dict[str, dict]] = None,
    tool_results: Optional[Dict[str, dict]] = None,
) -> PipelineResult:
    """最小闭环主入口。

    tool_observer：真实执行挂钩（未提供时用模拟观察值，测试可注入）。
    observations：Evaluation 观察值 {criterion: {score, evidence, failure}}。
    tool_results：per-tool 执行结果 {tool: {success, failure_mode}}（真实执行器
        产出；未提供时 post-task learning 退化为按整体评估判定各工具）。
    """
    result = PipelineResult(task, agent)

    # --- 安全边界：risk 高 → approval（EP-002）---
    result.approval_required = task.risk_level in ("high", "critical")
    if result.approval_required and agent.autonomy_level >= 5:
        # 全自主 agent 遇高风险任务也强制 approval 门槛
        result.approval_required = True

    # --- 1. Task → Capability Extraction（扁平，供组合/工作流/记忆）---
    result.required_capabilities = decompose_task(task)
    from .discovery import discover_unknown_capabilities
    result.unknown_capabilities = discover_unknown_capabilities(task.objective)

    # --- 2. Capability Tree 实例化 + JIT 展开（按 agent 状态剪枝）---
    result.tree_nodes = instantiate_capability_tree(task.task_type)
    jit_expand(result.tree_nodes, agent)
    result.missing_capabilities = tree_missing(result.tree_nodes)

    # --- 3. 节点级工具发现（能力驱动）+ 扁平汇总（兼容组合/工作流）---
    discover_tools_for_tree(result.tree_nodes)
    for cap in result.required_capabilities:
        result.discovered_tools[cap] = discover_for_capability(cap)

    # --- 4. Tool Composition（含组合理由）---
    all_cands: List[str] = []
    for tools in result.discovered_tools.values():
        for t in tools:
            if t not in all_cands:
                all_cands.append(t)
    if all_cands:
        result.chain = compose(all_cands, task, result.required_capabilities, agent.environment)
        # 组合理由补 note（为什么选 A 不选 B——互斥场景）
        _annotate_reasons(result.chain, result.required_capabilities)
        # 把组合选择回填到树节点 selected_tool
        annotate_selections(result.tree_nodes, result.chain.capability_tool_map)

    # --- 5. Workflow Synthesis（相似任务 → 复用历史）---
    mem = memory or (store.load_agent_memory(agent.agent_id) if store else None)
    if mem is None:
        mem = AgentMemory(agent_id=agent.agent_id)
    if result.chain:
        prev = reuse_historical_workflow(mem, task, result.required_capabilities)
        wf = synthesize_workflow(task, result.required_capabilities,
                                 result.chain.capability_tool_map)
        if prev:
            result.history_reused = True
            result.history_source = f"similar task history（{prev.goal} v{prev.version}）"
        evolve_workflow(mem, task.task_type, wf, prev)
        result.workflow = wf

    # --- 6. Execution（挂钩或模拟）---
    run = TaskRun(run_id=f"{task.task_id}-{len(mem.task_log) + 1}", task=task,
                  required_capabilities=result.required_capabilities,
                  missing_capabilities=result.missing_capabilities,
                  toolchain=result.chain.chain if result.chain else [],
                  workflow=result.workflow)
    result.run = run
    if tool_observer:
        for tool in run.toolchain:
            tool_observer(tool, "pre")
            # 真实执行器在此接入（授权/沙箱由 observer 外部保证）

    # --- 7. Evaluation ---
    criteria = knowledge.TASK_TYPES.get(task.task_type, {}).get("criteria", [])
    result.evaluation = evaluate_run(run, criteria, observations)
    if criteria:
        # 用评估回写能力
        update_agent_capabilities(agent, run)

    # --- 8. Memory（Post-task Learning）---
    apply_post_task_learning(agent, mem, run, tool_results or observations)
    # --- 8.1 Skill Evolution（tool_stats 真实数据驱动）---
    result.evolved_skills = evolve_skills_for_caps(mem, result.required_capabilities)
    if store:
        store.save_agent_memory(mem)
    agent.memory = mem
    return result


def _annotate_reasons(chain: ComposedChain, required_caps: List[str]) -> None:
    """为互斥排除与数据流决策补充自然语言理由。"""
    for name, reason in chain.reasons.items():
        note = f"适配 {reason.task_fit:.2f}，覆盖 {reason.capability_coverage:.2f}，"
        if reason.automation_friendliness >= 0.85:
            note += "CLI 原生/结构化输出，agent 可直接调用；"
        else:
            note += "自动化偏弱，需包装层；"
        if reason.security_risk and reason.security_risk != "none":
            note += f"安全影响：{reason.security_risk}；"
        reason.note = note


def analyze_tool_loss(chain: ComposedChain) -> Dict[str, List[str]]:
    """'如果删掉 Tool X，会损失什么能力？'——图结构可查询性。"""
    loss: Dict[str, List[str]] = {}
    for cap, tool in chain.capability_tool_map.items():
        loss.setdefault(tool, []).append(cap)
    return loss
