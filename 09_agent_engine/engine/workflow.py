"""KnowlegeMap Agent-Centric Engine — Workflow Synthesis.

把 Tool Chain 编排为可执行工作流：阶段/依赖/检查点/失败恢复/角色。
"""
from __future__ import annotations

from typing import Dict, List, Optional

from . import knowledge
from .domain import Task, Workflow, WorkflowStage


_STAGE_TEMPLATES: Dict[str, str] = {
    # capability_id -> 阶段目标模板
    "reconnaissance": "目标测绘与暴露面识别",
    "endpoint-discovery": "端点/路径发现",
    "http-interaction": "HTTP 会话构造与请求执行",
    "vulnerability-detection": "漏洞检测（注入/越权/配置）",
    "request-replay": "请求重放与回归验证",
    "result-aggregation": "多工具结果归一化聚合",
    "evidence-collection": "证据链收集（请求/响应/轨迹）",
    "reporting": "生成可追溯报告",
    "browser-interaction": "结构化浏览器操作",
    "assertion": "确定性断言验证",
    "sandbox-execution": "隔离环境执行",
    "agent-memory": "记忆写入/检索",
    "long-term-memory": "长期记忆维护",
    "agent-evaluation": "以证据评测 agent 行为",
    "multi-agent-orchestration": "多角色任务分解与协作",
    "protocol-interop": "协议接入与互操作",
    "local-inference": "本地推理执行",
    "embedding": "本地嵌入与检索",
    "privacy-guard": "隐私防护检查",
    "observability": "观测埋点与追踪",
    "monitoring": "运行状态监控",
    "scheduling": "任务调度",
    "state-persistence": "状态持久化与检查点",
    "failure-recovery": "失败检测与恢复",
    "self-improvement": "基于评估自我改进",
    "security-governance": "权限边界与治理检查",
    "runtime-defense": "运行时拦截与告警",
}

_RECOVERY = {
    "vulnerability-detection": "失败 → 缩小范围重试；标记 false-positive 候选待人工确认",
    "browser-interaction": "选择器失效 → 重新定位/等待重试；超时进入下一阶段并记录",
    "http-interaction": "连接失败 → 指数退避重试 ≤3 次；会话过期 → 重建会话",
    "evidence-collection": "证据缺失 → 标记判定为低置信并请求重放",
    "reporting": "生成失败 → 保留结构化中间结果",
}


def synthesize_workflow(task: Task, required_caps: List[str],
                       capability_tool_map: Dict[str, str],
                       version: int = 1,
                       evolution_reason: str = "") -> Workflow:
    """按能力依赖序把工具链编排为阶段工作流。"""
    wf = Workflow(
        goal=task.objective,
        tools=list(dict.fromkeys(capability_tool_map.values())),
        version=version,
        evolution_reason=evolution_reason,
        checkpoints=[],
        failure_recovery="阶段级恢复策略见各 stage",
    )
    prev = None
    for cap in required_caps:
        tool = capability_tool_map.get(cap, "")
        stage_id = f"stage-{len(wf.stages) + 1}"
        stage = WorkflowStage(
            stage_id=stage_id,
            goal=_STAGE_TEMPLATES.get(cap, cap),
            tools=[tool] if tool else [],
            checkpoint=f"检查点：{_STAGE_TEMPLATES.get(cap, cap)} 产出物完整",
            failure_recovery=_RECOVERY.get(cap, "记录失败模式并继续"),
            depends_on=[prev] if prev else [],
        )
        wf.stages.append(stage)
        wf.dependencies[stage_id] = stage.depends_on
        wf.checkpoints.append(stage.checkpoint)
        prev = stage_id
    wf.agent_roles = _roles_for(task.task_type)
    return wf


def _roles_for(task_type: str) -> List[str]:
    return {
        "security-assessment": ["recon-specialist", "vuln-detector", "evidence-collector", "reporter"],
        "e2e-web-testing": ["browser-operator", "assertion-runner", "reporter"],
        "long-running-autonomous-agent": ["scheduler", "state-keeper", "memory-manager", "monitor", "improver"],
        "local-mobile-ai-assistant": ["local-inference-runner", "memory-manager", "privacy-guard"],
        "multi-agent-team": ["orchestrator", "protocol-broker", "memory-manager", "governance-guard"],
        "agent-eval-harness": ["eval-runner", "sandbox-operator", "evidence-collector"],
    }.get(task_type, ["executor"])
