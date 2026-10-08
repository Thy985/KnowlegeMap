"""KnowlegeMap Agent-Centric Engine — Agent Operational Memory.

与 Human Memory（06_expansion_index）区分：本记忆服务于未来任务执行。
- 工具统计（usage/success_rate/failure_modes）
- 工作流版本（task_type -> [v1, v2...] 带演进理由）
- 相似任务检索（capability profile 重叠 → 复用历史 workflow/evaluation）
- 成功/失败模式沉淀
"""
from __future__ import annotations

import json
import os
from typing import Dict, List, Optional

from . import knowledge
from .domain import Agent, AgentMemory, Task, TaskRun, ToolStat, Workflow


class MemoryStore:
    """Agent Operational Memory 的 JSON 持久化（08_agent_centric/memory/）。"""

    def __init__(self, memory_dir: str):
        self.memory_dir = memory_dir
        os.makedirs(memory_dir, exist_ok=True)

    # ---- 持久化 ----
    def save_agent_memory(self, memory: AgentMemory) -> str:
        path = os.path.join(self.memory_dir, f"agent_{memory.agent_id}.json")
        payload = {
            "agent_id": memory.agent_id,
            "tool_stats": {k: _stat_dict(v) for k, v in memory.tool_stats.items()},
            "workflow_versions": {k: [_wf_dict(w) for w in versions]
                                  for k, versions in memory.workflow_versions.items()},
            "task_log": [_run_dict(r) for r in memory.task_log],
            "success_patterns": memory.success_patterns,
            "failure_patterns": memory.failure_patterns,
            "environment_failures": memory.environment_failures,
            "updated_at": memory.updated_at,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        return path

    def load_agent_memory(self, agent_id: str) -> AgentMemory:
        path = os.path.join(self.memory_dir, f"agent_{agent_id}.json")
        m = AgentMemory(agent_id=agent_id)
        if not os.path.exists(path):
            return m
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        m.tool_stats = {k: ToolStat(**v) for k, v in payload.get("tool_stats", {}).items()}
        m.workflow_versions = {k: [_wf_from_dict(w) for w in v]
                               for k, v in payload.get("workflow_versions", {}).items()}
        m.task_log = [_run_from_dict(r) for r in payload.get("task_log", [])]
        m.success_patterns = payload.get("success_patterns", [])
        m.failure_patterns = payload.get("failure_patterns", [])
        m.environment_failures = payload.get("environment_failures", [])
        m.updated_at = payload.get("updated_at", m.updated_at)
        return m


def apply_post_task_learning(agent: Agent, memory: AgentMemory, run: TaskRun,
                             tool_results: Optional[Dict[str, dict]] = None) -> None:
    """Post-task Learning：任务结果 + Evaluation → Memory/能力更新。"""
    tool_results = tool_results or {}
    for tool in run.toolchain:
        res = tool_results.get(tool, {"success": run.evaluation.score >= 0.6 if run.evaluation else True,
                                      "failure_mode": ""})
        memory.record_tool_usage(tool, success=bool(res.get("success")), failure_mode=res.get("failure_mode", ""))

    # 成功/失败模式沉淀
    if run.evaluation:
        if run.evaluation.score >= 0.6:
            pattern = f"{run.task.task_type}: {run.toolchain}"
            if pattern not in memory.success_patterns:
                memory.success_patterns.append(pattern)
        else:
            fp = f"{run.task.task_type}: {run.evaluation.failure}"
            if fp not in memory.failure_patterns:
                memory.failure_patterns.append(fp)

    # 环境失败记录（来自 tool_results 中 failure_mode == 'env'）
    for tool, res in tool_results.items():
        if res.get("failure_mode") == "env":
            memory.environment_failures.append(f"{tool}: {res.get('note', '')}")

    memory.record_task_run(run)


def reuse_historical_workflow(memory: AgentMemory, task: Task,
                              required_caps: Optional[List[str]] = None) -> Optional[Workflow]:
    """相似任务 → 历史工作流（Task Similarity → Previous Workflow → Improved Workflow）。"""
    profile = set(required_caps) if required_caps else None
    similar = memory.find_similar_tasks(task, top_k=1, profile=profile)
    if not similar:
        return None
    prev_run = similar[0]
    prev_type = prev_run.task.task_type
    return memory.best_workflow(prev_type)


def evolve_workflow(memory: AgentMemory, task_type: str, new_wf: Workflow,
                    prev_wf: Optional[Workflow]) -> Workflow:
    """工作流版本演进：v2 相对 v1 的改进理由显式化。"""
    prev_versions = memory.workflow_versions.get(task_type, [])
    version = len(prev_versions) + 1
    new_wf.version = version
    if prev_wf:
        new_wf.evolution_reason = _evolution_reason(prev_wf, new_wf)
    memory.add_workflow_version(task_type, new_wf)
    return new_wf


def _evolution_reason(old: Workflow, new: Workflow) -> str:
    old_score = _wf_score(old)
    new_score = _wf_score(new)
    diff = [f"v{old.version}→v{new.version}"]
    if new_score > old_score:
        diff.append(f"评估分 {old_score:.2f}→{new_score:.2f}")
    if len(new.stages) != len(old.stages):
        diff.append(f"阶段数 {len(old.stages)}→{len(new.stages)}")
    return "; ".join(diff)


def _wf_score(w: Workflow) -> float:
    if not w.evaluation:
        return 0.0
    return sum(e.score for e in w.evaluation) / len(w.evaluation)


# ---------------- serialization helpers ----------------
def _stat_dict(s: ToolStat) -> dict:
    return {"usage_count": s.usage_count, "success_count": s.success_count,
            "success_rate": s.success_rate, "failure_modes": s.failure_modes,
            "last_used": s.last_used, "best_workflow_version": s.best_workflow_version}


def _wf_dict(w: Workflow) -> dict:
    return {"goal": w.goal, "version": w.version, "evolution_reason": w.evolution_reason,
            "tools": w.tools, "checkpoints": w.checkpoints,
            "stages": [{"stage_id": s.stage_id, "goal": s.goal, "tools": s.tools,
                        "checkpoint": s.checkpoint, "failure_recovery": s.failure_recovery,
                        "depends_on": s.depends_on} for s in w.stages]}


def _wf_from_dict(d: dict) -> Workflow:
    from .domain import WorkflowStage
    w = Workflow(goal=d.get("goal", ""), version=d.get("version", 1),
                 evolution_reason=d.get("evolution_reason", ""),
                 tools=d.get("tools", []), checkpoints=d.get("checkpoints", []))
    for s in d.get("stages", []):
        w.stages.append(WorkflowStage(stage_id=s.get("stage_id", ""), goal=s.get("goal", ""),
                                      tools=s.get("tools", []), checkpoint=s.get("checkpoint", ""),
                                      failure_recovery=s.get("failure_recovery", ""),
                                      depends_on=s.get("depends_on", [])))
    return w


def _run_dict(r: TaskRun) -> dict:
    return {"run_id": r.run_id, "task_id": r.task.task_id, "task_type": r.task.task_type,
            "objective": r.task.objective,
            "required_capabilities": r.required_capabilities,
            "missing_capabilities": r.missing_capabilities,
            "toolchain": r.toolchain, "result_summary": r.result_summary, "ran_at": r.ran_at,
            "evaluation_score": r.evaluation.score if r.evaluation else None}


def _run_from_dict(d: dict) -> TaskRun:
    from .domain import Task
    t = Task(task_id=d.get("task_id", d.get("run_id", "")), task_type=d.get("task_type", ""),
             objective=d.get("objective", ""))
    return TaskRun(run_id=d.get("run_id", ""), task=t,
                   required_capabilities=d.get("required_capabilities", []),
                   missing_capabilities=d.get("missing_capabilities", []),
                   toolchain=d.get("toolchain", []),
                   result_summary=d.get("result_summary", ""), ran_at=d.get("ran_at", ""))
