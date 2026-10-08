"""KnowlegeMap Agent-Centric Engine — Domain Model.

Mode B（Agent-Centric Task Expansion）的一等实体定义。
规范文档：08_agent_centric/docs/01_agent_domain_model.md
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------- Evidence

@dataclass
class Evidence:
    source: str                 # URL / 实验 / 观察来源
    type: str = "FACT"          # FACT / DESIGN / OBSERVATION / EXPERIMENT
    confidence: float = 0.5
    timestamp: str = field(default_factory=_now)
    supporting_observation: str = ""

# ---------------------------------------------------------------- Capability

@dataclass
class Capability:
    """能力——Mode B 的发现单位。能力 ≠ 工具：一能力可多工具实现。"""
    capability_id: str
    name: str
    description: str
    prerequisites: List[str] = field(default_factory=list)
    required_tools: List[str] = field(default_factory=list)
    related_projects: List[str] = field(default_factory=list)
    confidence: float = 0.0        # Agent 侧已掌握信心
    evidence: List[Evidence] = field(default_factory=list)
    evaluation_history: List["Evaluation"] = field(default_factory=list)


# ------------------------------------------------- Tree nodes（v2）

@dataclass
class CapabilityNode:
    """Capability Tree 节点（任务动态实例化）。

    树表达"完成这个任务需要什么能力层级"；节点运行时携带
    current_state / gap / candidate_tools / selected_tool 的统一视图。
    叶子节点通过 maps_to 映射到扁平能力库（knowledge.CAPABILITIES），
    工具发现与 Gap 判定复用该映射。
    """
    id: str                      # 点分路径，如 reconnaissance.asset-discovery
    name: str
    parent: Optional[str] = None
    children: List[str] = field(default_factory=list)
    maps_to: str = ""            # 映射到扁平 capability id
    leaf_tags: List[str] = field(default_factory=list)  # 叶子工具发现关键词
    # 运行时状态（JIT 展开后填充）
    expanded: bool = False
    current_state: float = 0.0
    gap: bool = False
    candidate_tools: List[str] = field(default_factory=list)
    selected_tool: Optional[str] = None
    selection_reason: Optional["SelectionReason"] = None
    evidence: List[str] = field(default_factory=list)

    def is_leaf(self) -> bool:
        return not self.children


@dataclass
class DomainNode:
    """Domain Tree 节点：静态组织领域知识（领域由什么组成）。"""
    id: str
    name: str
    parent: Optional[str] = None
    children: List[str] = field(default_factory=list)
    description: str = ""

# ---------------------------------------------------------------- Tool

@dataclass
class Tool:
    name: str
    category: str
    interface: str = "CLI"        # CLI / API / SDK / MCP / GUI / model
    input_format: str = "text"    # 组合时检查数据流兼容
    output_format: str = "text"
    environment_requirements: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    cost: str = "low"             # low / med / high
    reliability: float = 0.5      # 0-1 信号（来源+统计）
    security_implications: List[str] = field(default_factory=list)
    automation_friendly: float = 0.5   # 0-1：CLI 原生/结构化输出
    structured_output: float = 0.5     # 0-1
    ecosystem_maturity: float = 0.5    # 0-1
    maintenance_status: str = "active" # active / maintenance / archived
    source_cards: List[str] = field(default_factory=list)  # 证据（候选卡/star）
    capabilities: List[str] = field(default_factory=list)  # 该工具实现的能力
    selection_reasons: List["SelectionReason"] = field(default_factory=list)

# ---------------------------------------------------------------- Skill

@dataclass
class Skill:
    name: str
    purpose: str
    trigger: str = ""
    procedure: str = ""
    required_tools: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    evaluation: List["Evaluation"] = field(default_factory=list)
    usage_count: int = 0
    success_rate: float = 0.0
    last_used: Optional[str] = None


@dataclass
class SkillVersion:
    """Skill 的版本化资产（由 tool_stats 真实数据驱动演进）。"""
    skill_id: str
    version: int
    capability: str = ""
    procedure: List[str] = field(default_factory=list)
    required_tools: List[str] = field(default_factory=list)   # 按成功率重排
    tool_success: Dict[str, float] = field(default_factory=dict)
    removed_tools: List[str] = field(default_factory=list)   # 持续失败被降级
    inserted_steps: List[str] = field(default_factory=list)  # 针对失败插入
    evolution_reason: str = ""
    created_at: str = field(default_factory=_now)

# ---------------------------------------------------------------- Workflow

@dataclass
class WorkflowStage:
    stage_id: str
    goal: str
    tools: List[str] = field(default_factory=list)
    checkpoint: str = ""
    failure_recovery: str = ""
    depends_on: List[str] = field(default_factory=list)

@dataclass
class Workflow:
    goal: str
    stages: List[WorkflowStage] = field(default_factory=list)
    agent_roles: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)      # 工具链（有向序）
    dependencies: Dict[str, List[str]] = field(default_factory=dict)
    checkpoints: List[str] = field(default_factory=list)
    failure_recovery: str = ""
    evaluation: List["Evaluation"] = field(default_factory=list)
    version: int = 1
    evolution_reason: str = ""    # v2 相对 v1 为什么更好

# ---------------------------------------------------------------- Task

@dataclass
class Task:
    task_id: str
    task_type: str                # security-assessment / autonomous-agent / ...
    objective: str
    constraints: List[str] = field(default_factory=list)
    environment: Dict[str, str] = field(default_factory=dict)
    desired_output: str = ""
    risk_level: str = "low"       # low / med / high / critical
    evaluation_criteria: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=_now)

# ---------------------------------------------------------------- Evaluation

@dataclass
class Evaluation:
    criterion: str
    score: float = 0.0            # 0-1
    evidence: List[Evidence] = field(default_factory=list)
    failure: str = ""             # 失败模式（false-positive / timeout / ...）
    regression: bool = False      # 相对上次是否回退
    reproducibility: float = 0.0  # 0-1
    evaluated_at: str = field(default_factory=_now)

# ---------------------------------------------------------------- Selection Reason

@dataclass
class SelectionReason:
    """每个 Tool/Skill/Project 选择的多维理由。Star 数仅弱信号。"""
    candidate: str
    task_fit: float = 0.0
    capability_coverage: float = 0.0
    interface_compatibility: float = 0.0
    automation_friendliness: float = 0.0
    structured_output: float = 0.0
    reliability: float = 0.0
    maintenance_status: str = ""
    ecosystem_maturity: float = 0.0
    environment_compatibility: float = 0.0
    computational_cost: str = ""
    permission_requirements: str = ""
    security_risk: str = ""
    evidence_quality: str = ""
    note: str = ""                # 为什么选 A 而不选 B

# ---------------------------------------------------------------- Agent

@dataclass
class Agent:
    agent_id: str
    identity: str
    role: str
    objective: str
    available_tools: List[str] = field(default_factory=list)   # tool names
    available_skills: List[str] = field(default_factory=list)
    memory: "AgentMemory" = None
    environment: Dict[str, str] = field(default_factory=dict)
    constraints: List[str] = field(default_factory=list)
    autonomy_level: int = 3       # 0=人工逐级批准, 5=全自主
    capabilities: Dict[str, float] = field(default_factory=dict)  # cap_id -> confidence
    weaknesses: List[str] = field(default_factory=list)
    task_history: List["TaskRun"] = field(default_factory=list)
    evaluations: List[Evaluation] = field(default_factory=list)

    def capability_names(self) -> List[str]:
        return [c for c, conf in self.capabilities.items() if conf >= 0.5]

    def has_capability(self, cap_id: str, threshold: float = 0.5) -> bool:
        return self.capabilities.get(cap_id, 0.0) >= threshold

# ---------------------------------------------------------------- TaskRun

@dataclass
class TaskRun:
    run_id: str
    task: Task
    required_capabilities: List[str] = field(default_factory=list)
    missing_capabilities: List[str] = field(default_factory=list)
    toolchain: List[str] = field(default_factory=list)
    workflow: Optional[Workflow] = None
    evaluation: Optional[Evaluation] = None
    result_summary: str = ""
    ran_at: str = field(default_factory=_now)

    def capability_profile(self) -> Dict[str, int]:
        """能力画像（用于相似任务检索）。"""
        return {c: 1 for c in self.required_capabilities}

# ---------------------------------------------------------------- Memory

@dataclass
class Memory:
    """Human Memory 索引句柄（06_expansion_index）——Mode B 只引用，不复制。"""
    human_index_path: str = "06_expansion_index/README.md"

@dataclass
class ToolStat:
    usage_count: int = 0
    success_count: int = 0
    success_rate: float = 0.0
    failure_modes: Dict[str, int] = field(default_factory=dict)
    last_used: Optional[str] = None
    best_workflow_version: int = 1

@dataclass
class AgentMemory:
    """Agent Operational Memory——服务于未来任务（与 Human Memory 区分）。"""
    agent_id: str
    tool_stats: Dict[str, ToolStat] = field(default_factory=dict)
    workflow_versions: Dict[str, List[Workflow]] = field(default_factory=dict)  # task_type -> [v1, v2...]
    skill_versions: Dict[str, List["SkillVersion"]] = field(default_factory=dict)  # skill_id -> [v1, v2...]
    task_log: List[TaskRun] = field(default_factory=list)
    success_patterns: List[str] = field(default_factory=list)   # 有效组合经验
    failure_patterns: List[str] = field(default_factory=list)   # 高频失败模式
    environment_failures: List[str] = field(default_factory=list)  # 环境约束导致失败
    updated_at: str = field(default_factory=_now)

    def record_tool_usage(self, tool: str, success: bool, failure_mode: str = "") -> None:
        stat = self.tool_stats.setdefault(tool, ToolStat())
        stat.usage_count += 1
        if success:
            stat.success_count += 1
        else:
            if failure_mode:
                stat.failure_modes[failure_mode] = stat.failure_modes.get(failure_mode, 0) + 1
        stat.success_rate = round(stat.success_count / stat.usage_count, 3) if stat.usage_count else 0.0
        stat.last_used = _now()
        self.updated_at = _now()

    def record_task_run(self, run: TaskRun) -> None:
        self.task_log.append(run)
        self.updated_at = _now()

    def add_workflow_version(self, task_type: str, wf: Workflow) -> None:
        versions = self.workflow_versions.setdefault(task_type, [])
        versions.append(wf)
        self.updated_at = _now()

    def best_workflow(self, task_type: str) -> Optional[Workflow]:
        versions = self.workflow_versions.get(task_type, [])
        if not versions:
            return None
        # 取评估分数最高的版本
        return max(versions, key=lambda w: _wf_score(w))

    def find_similar_tasks(self, task: Task, top_k: int = 3,
                           profile: Optional[set] = None) -> List[TaskRun]:
        """基于能力画像（required capabilities）重叠检索相似历史任务。

        profile：任务侧的能力需求集合（由调用方从 Task 分解得到）。
        与 Human Memory 区分：这里检索的是"做过的任务"，用于复用 workflow/evaluation。
        """
        if profile is None:
            profile = set(task.evaluation_criteria)   # fallback：无分解结果时退化为 criteria
        scored = []
        for run in self.task_log:
            run_profile = set(run.required_capabilities)
            overlap = len(profile & run_profile)
            union = len(profile | run_profile) or 1
            scored.append((overlap / union, run))
        scored.sort(key=lambda x: -x[0])
        return [r for _, r in scored[:top_k] if _ > 0]

def _wf_score(w: Workflow) -> float:
    if not w.evaluation:
        return 0.0
    return sum(e.score for e in w.evaluation) / len(w.evaluation)
