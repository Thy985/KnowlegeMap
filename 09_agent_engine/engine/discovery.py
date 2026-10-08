"""KnowlegeMap Agent-Centric Engine — Discovery & Gap Analysis.

核心行为改变：Task → Capability Requirements → Capability Gap → Tool/Project Discovery。
Discovery 发现的是"能力"（含未知能力），不是直接推荐项目。
"""
from __future__ import annotations

from typing import Dict, List, Optional

from . import knowledge
from .domain import Agent, Capability, Evidence, Task


class DiscoveryError(Exception):
    pass


def decompose_task(task: Task) -> List[str]:
    """Task → Required Capabilities（能力需求分解）。

    优先使用知识库的 task_type 分解规则；未识别的任务类型：
    - 尝试从 objective 关键词匹配现有能力（未知能力发现的第一步）；
    - 保留为 raw 能力需求（由外部钩子扩展）。
    """
    ttype = knowledge.TASK_TYPES.get(task.task_type)
    if ttype:
        return list(ttype["required_capabilities"])

    # 未知能力发现：从 objective 中提取关键词 → 能力候选
    discovered: List[str] = []
    obj = task.objective.lower()
    for cap_id, cap in knowledge.CAPABILITIES.items():
        if any(kw in obj for kw in _KEYWORDS.get(cap_id, [])):
            discovered.append(cap_id)
    return discovered


def gap_analysis(agent: Agent, required: List[str]) -> List[str]:
    """Capability Gap：已有能力（confidence >= 阈值） vs 需求能力。"""
    missing = [c for c in required if not agent.has_capability(c)]
    # 前置能力缺口也要展开（依赖图传递闭包）
    expanded = set(missing)
    for m in missing:
        _expand_prereqs(m, expanded, agent)
    return [c for c in required if c in expanded] + sorted(expanded - set(required))


def _expand_prereqs(cap_id: str, expanded: set, agent: Agent) -> None:
    pre = knowledge.CAPABILITIES.get(cap_id, {}).get("prerequisites", [])
    for p in pre:
        if not agent.has_capability(p) and p not in expanded:
            expanded.add(p)
            _expand_prereqs(p, expanded, agent)


def discover_for_capability(cap_id: str, seen: Optional[set] = None) -> List[str]:
    """Capability → Candidate Tools（种子知识库；未知能力返回空并标记）。"""
    seen = seen or set()
    cands = knowledge.capability_candidates(cap_id)
    out = [c for c in cands if c not in seen]
    return out


def discover_unknown_capabilities(objective: str) -> List[str]:
    """未知能力发现：从任务目标推导"可能还不知道需要什么"的能力域。"""
    found: List[str] = []
    obj = objective.lower()
    for cap_id, keywords in _KEYWORDS.items():
        if any(kw in obj for kw in keywords) and cap_id not in found:
            found.append(cap_id)
    return found


def build_capability_models(cap_ids: List[str], source: str = "task-decomposition") -> Dict[str, Capability]:
    """把能力 id 实例化为 Capability 对象（含知识库证据锚点）。"""
    models: Dict[str, Capability] = {}
    for cap_id in cap_ids:
        meta = knowledge.CAPABILITIES.get(cap_id)
        if not meta:
            continue
        models[cap_id] = Capability(
            capability_id=cap_id,
            name=meta["name"],
            description=meta["description"],
            prerequisites=list(meta["prerequisites"]),
            required_tools=list(meta["candidate_tools"]),
            related_projects=list(meta["related_projects"]),
            confidence=0.0,
            evidence=[Evidence(source=meta["source"], type="FACT", confidence=0.9,
                               supporting_observation=f"能力定义来自仓库资产：{source}")],
        )
    return models


# 关键词表：objective 解析与未知能力发现的共同依据
_KEYWORDS: Dict[str, List[str]] = {
    "reconnaissance": ["recon", "侦察", "scan", "enumeration", "测绘", "信息收集"],
    "endpoint-discovery": ["endpoint", "端点", "path", "路径", "route", "路由"],
    "http-interaction": ["http", "请求", "api", "接口", "request", "重放", "replay"],
    "vulnerability-detection": ["漏洞", "vulnerability", "注入", "injection", "安全测试", "security test", "越权"],
    "browser-interaction": ["浏览器", "browser", "网页", "页面", "e2e", "端到端"],
    "sandbox-execution": ["沙箱", "sandbox", "隔离", "isolat", "执行不可信", "untrusted"],
    "agent-memory": ["记忆", "memory", "记忆库", "跨会话"],
    "agent-evaluation": ["评测", "eval", "评估", "基准", "benchmark", "验证"],
    "multi-agent-orchestration": ["多 agent", "multi-agent", "多智能体", "编排", "orchestrat", "团队", "team"],
    "local-inference": ["本地", "local", "离线", "offline", "端侧", "edge", "边缘"],
    "observability": ["可观测", "observ", "监控", "monitor", "trace", "追踪"],
    "protocol-interop": ["协议", "protocol", "mcp", "a2a", "互操作", "interop"],
    "security-governance": ["安全治理", "权限", "permission", "边界", "boundary", "治理", "governance"],
    "runtime-defense": ["拦截", "防火墙", "firewall", "防护", "defense", "防御"],
    "long-term-memory": ["长期", "long-term", "持久记忆"],
    "state-persistence": ["状态", "state", "checkpoint", "断点", "恢复", "resume"],
    "scheduling": ["调度", "schedule", "定时", "周期", "cron"],
    "failure-recovery": ["恢复", "recovery", "容错", "fault", "重试", "retry"],
    "monitoring": ["监控", "monitor", "运行状态", "成本", "cost"],
    "self-improvement": ["自我改进", "self-improv", "学习", "演化", "evolve"],
    "privacy-guard": ["隐私", "privacy", "脱敏", "不出端"],
    "embedding": ["嵌入", "embedding", "检索", "rag"],
    "assertion": ["断言", "assert", "验证结果", "校验"],
}
