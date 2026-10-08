#!/usr/bin/env python3
"""KnowlegeMap Agent-Centric Engine — CLI.

用法示例：
  python cli.py run --agent pen-test-agent --task-type security-assessment \
      --objective "对授权网站执行安全测试" --task-id task-demo-001
  python cli.py run --task-type e2e-web-testing --objective "跑端到端回归" --demo
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine import knowledge                       # noqa: E402
from engine.domain import Agent, Task              # noqa: E402
from engine.memory import MemoryStore              # noqa: E402
from engine.pipeline import run_agent_task         # noqa: E402
from engine.store import AssetStore                # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def build_agent(agent_id: str) -> Agent:
    """从 08_agent_centric/agents/ 加载；不存在则建默认 profile。"""
    return Agent(
        agent_id=agent_id,
        identity=f"{agent_id}（KnowlegeMap Mode B）",
        role="generic task executor",
        objective="根据任务发现能力需求并构建工具链",
        capabilities={},      # 空能力 → 全缺口（演示 Capability Gap）
        autonomy_level=3,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="KnowlegeMap Agent-Centric Engine")
    sub = ap.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="运行 Agent Task Expansion 最小闭环")
    run.add_argument("--agent", default="pen-test-agent")
    run.add_argument("--task-type", required=True,
                     choices=sorted(knowledge.TASK_TYPES.keys()))
    run.add_argument("--objective", required=True)
    run.add_argument("--task-id", default="task-default")
    run.add_argument("--risk", default="", help="覆盖任务风险级")
    run.add_argument("--write-assets", action="store_true",
                     help="把产物写入 08_agent_centric/ 资产层")

    demo = sub.add_parser("demo", help="演示安全测试任务闭环")
    demo.add_argument("--agent", default="pen-test-agent")

    args = ap.parse_args()

    if args.cmd == "demo":
        args = argparse.Namespace(
            cmd="run", agent=args.agent, task_type="security-assessment",
            objective="对一个合法授权的网站执行安全测试，产出漏洞清单与证据链",
            task_id="task-demo-security", risk="high", write_assets=True)
        demo_obs = {
            "detection-accuracy": {"score": 0.92, "evidence": "garak 检出 17/18 已知漏洞", "failure": ""},
            "false-positive-rate": {"score": 0.85, "evidence": "playwright 重放验证 3 个候选", "failure": "2 个 false-positive 候选"},
            "evidence-completeness": {"score": 0.88, "evidence": "promptfoo 证据链完整 16/18", "failure": ""},
            "reproducibility": {"score": 0.90, "evidence": "两次运行结果一致", "failure": ""},
        }
    else:
        demo_obs = None

    ttype = knowledge.get_task_type(args.task_type)
    task = Task(
        task_id=args.task_id,
        task_type=args.task_type,
        objective=args.objective,
        risk_level=args.risk or ttype.get("risk_level", "low"),
        desired_output=ttype.get("desired_output", ""),
        evaluation_criteria=list(ttype.get("criteria", [])),
        constraints=list(ttype.get("constraints", [])) if ttype.get("constraints") else [],
    )
    agent = build_agent(args.agent)

    mem_dir = os.path.join(REPO_ROOT, "08_agent_centric", "memory")
    store = MemoryStore(mem_dir)
    asset = AssetStore(os.path.join(REPO_ROOT, "08_agent_centric"))

    result = run_agent_task(agent, task, store=store, observations=demo_obs)
    print(result.render_report())

    if args.write_assets:
        p1 = asset.save_task_run(result)
        p2 = asset.save_workflow(result.workflow, task.task_type) if result.workflow else None
        p3 = asset.save_agent_profile(agent)
        p4 = asset.export_capability_registry()
        p5 = asset.export_domain_tree()
        p6 = asset.export_capability_graph(result)
        p7 = asset.export_skills()
        print(f"\n[assets] {p1}\n[assets] {p2}\n[assets] {p3}\n[assets] {p4}"
              f"\n[assets] {p5}\n[assets] {p6}\n[assets] {p7}")


if __name__ == "__main__":
    main()
