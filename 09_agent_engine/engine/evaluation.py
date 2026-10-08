"""KnowlegeMap Agent-Centric Engine — Evaluation.

Evaluation 服务于两个目的：
1. 任务侧：按 criterion 对 TaskRun 结果打分（含失败模式/回归/可复现性）；
2. 能力侧：把任务评估回写为 Capability confidence 更新。
"""
from __future__ import annotations

from typing import Dict, List, Optional

from .domain import Agent, Evaluation as Eval, Evidence, TaskRun


def evaluate_run(run: TaskRun, criteria: List[str],
                 observations: Optional[Dict[str, dict]] = None) -> Eval:
    """对一次任务执行做评估。observations 由执行器提供（证据来源）。

    observations: {criterion: {"score": 0-1, "evidence": str, "failure": str}}
    """
    obs = observations or {}
    scores = []
    for crit in criteria:
        o = obs.get(crit, {})
        score = float(o.get("score", 0.0))
        failure = o.get("failure", "")
        evidence = Evidence(
            source=o.get("evidence", "engine-simulated"),
            type="EXPERIMENT",
            confidence=0.8,
            supporting_observation=f"criterion={crit} failure={failure or 'none'}",
        )
        scores.append(score)
        if failure:
            run.result_summary += f"[{crit}:{failure}] "
    overall = round(sum(scores) / len(scores), 3) if scores else 0.0
    ev = Eval(
        criterion="; ".join(criteria),
        score=overall,
        evidence=[Evidence(source="task-run", type="EXPERIMENT", confidence=0.8,
                           supporting_observation=run.result_summary or "no observations")],
        failure=run.result_summary.strip() or "",
        reproducibility=0.7,
    )
    run.evaluation = ev
    return ev


def update_agent_capabilities(agent: Agent, run: TaskRun, delta: float = 0.2) -> None:
    """任务评估回写能力置信度：成功 → 置信提升；失败 → 记录弱点。"""
    for cap in run.required_capabilities:
        cur = agent.capabilities.get(cap, 0.0)
        if run.evaluation and run.evaluation.score >= 0.6:
            agent.capabilities[cap] = round(min(1.0, cur + delta), 2)
        else:
            agent.capabilities[cap] = round(max(0.0, cur - delta * 0.5), 2)
            if cap not in agent.weaknesses:
                agent.weaknesses.append(cap)
    agent.evaluations.append(run.evaluation) if run.evaluation else None
