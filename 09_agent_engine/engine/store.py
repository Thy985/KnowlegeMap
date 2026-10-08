"""KnowlegeMap Agent-Centric Engine — Markdown Asset Store.

把引擎产物持久化为 08_agent_centric/ 下的人读 Markdown 资产
（tasks / workflows / capabilities / agents），与 Human 资产层保持同构。
"""
from __future__ import annotations

import os
from typing import Optional

from . import knowledge
from .domain import Agent, Workflow
from .pipeline import PipelineResult


class AssetStore:
    def __init__(self, base_dir: str):
        self.base = base_dir
        for sub in ("tasks", "workflows", "capabilities", "agents",
                    "evaluations", "skills", "domains"):
            os.makedirs(os.path.join(self.base, sub), exist_ok=True)

    # ---- TaskRun → tasks/ ----
    def save_task_run(self, result: PipelineResult) -> str:
        path = os.path.join(self.base, "tasks", f"{result.task.task_id}.md")
        content = result.render_report()
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    # ---- Workflow → workflows/ ----
    def save_workflow(self, wf: Workflow, task_type: str) -> str:
        path = os.path.join(self.base, "workflows", f"{task_type}_v{wf.version}.md")
        lines = [
            f"# Workflow v{wf.version} · {task_type}",
            f"goal: {wf.goal}",
            f"evolution_reason: {wf.evolution_reason or '首版'}",
            f"tools: {', '.join(wf.tools)}",
            "",
            "## stages",
        ]
        for s in wf.stages:
            lines.append(f"### {s.stage_id} [{s.goal}]")
            lines.append(f"- tools: {', '.join(s.tools) or '-'}")
            lines.append(f"- depends_on: {', '.join(s.depends_on) or '-'}")
            lines.append(f"- checkpoint: {s.checkpoint}")
            lines.append(f"- failure_recovery: {s.failure_recovery}")
        lines.append("")
        lines.append(f"checkpoints: {len(wf.checkpoints)} ｜ agents: {', '.join(wf.agent_roles)}")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return path

    # ---- Capability 注册表（从种子知识库导出，供查询） ----
    def export_capability_registry(self) -> str:
        path = os.path.join(self.base, "capabilities", "README.md")
        lines = [
            "# Capability Registry（Agent-Centric 能力注册表）",
            "",
            "> 由引擎从种子知识库导出（09_agent_engine/engine/knowledge.py）。",
            "> 能力是发现单位：先发现'需要什么能力'，再找实现工具。",
            "",
            "| capability_id | 名称 | 前置能力 | 工具候选 | 相关项目 | 证据锚点 |",
            "|---|---|---|---|---|---|",
        ]
        for cap_id, meta in sorted(knowledge.CAPABILITIES.items()):
            lines.append(
                f"| {cap_id} | {meta['name']} | {', '.join(meta['prerequisites']) or '-'} "
                f"| {', '.join(meta['candidate_tools']) or '-'} "
                f"| {', '.join(meta['related_projects']) or '-'} | {meta['source']} |"
            )
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return path

    # ---- Agent profile → agents/ ----
    def save_agent_profile(self, agent: Agent) -> str:
        path = os.path.join(self.base, "agents", f"{agent.agent_id}.md")
        caps = ", ".join(f"{c}({conf:.2f})" for c, conf in sorted(agent.capabilities.items()))
        lines = [
            f"# Agent Profile · {agent.agent_id}",
            f"- identity: {agent.identity}",
            f"- role: {agent.role}",
            f"- objective: {agent.objective}",
            f"- autonomy_level: {agent.autonomy_level}（0=人工逐级批准，5=全自主）",
            f"- available_tools: {', '.join(agent.available_tools) or '-'}",
            f"- capabilities: {caps or '-'}",
            f"- weaknesses: {', '.join(agent.weaknesses) or '-'}",
            f"- constraints: {', '.join(agent.constraints) or '-'}",
            f"- task_history: {len(agent.task_history)}",
            "",
        ]
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return path

    # ---- Domain Tree → domains/（v2）----
    def export_domain_tree(self) -> str:
        from .trees import build_domain_tree
        nodes = build_domain_tree()
        path = os.path.join(self.base, "domains", "README.md")
        lines = ["# Domain Tree（领域树 · 静态组织）", "",
                 "> 组织领域由什么组成；任务空间见各 Capability Tree。", ""]
        roots = [n for n in nodes.values() if n.parent is None]
        for r in roots:
            lines.append(f"- **{r.name}**")
            for c in r.children:
                child = nodes.get(c)
                cname = child.name if child else c
                grandchildren = child.children if child else []
                if grandchildren:
                    lines.append(f"  - {cname}")
                    for gc in grandchildren:
                        gnode = nodes.get(gc)
                        lines.append(f"    - {gnode.name if gnode else gc}")
                else:
                    lines.append(f"  - {cname}")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return path

    # ---- Capability Graph → capabilities/graph.md（v2）----
    def export_capability_graph(self, result: PipelineResult) -> str:
        path = os.path.join(self.base, "capabilities", "graph.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(result.capability_graph.render() + "\n")
        return path

    # ---- Skills → skills/（v2 · Capability→Skill→Tool 分层）----
    def export_skills(self) -> str:
        path = os.path.join(self.base, "skills", "README.md")
        lines = ["# Skills（技能库 · How 层）", "",
                 "> Capability=What / Skill=How / Tool=With what / Project=来源。",
                 ""]
        for sid, sk in knowledge.SKILLS.items():
            lines.append(f"## {sk['name']}（{sid}）")
            lines.append(f"- purpose: {sk['purpose']}")
            lines.append(f"- trigger: {sk['trigger']}")
            lines.append(f"- capability: {sk['capability']}")
            lines.append(f"- procedure: " + " → ".join(sk["procedure"]))
            lines.append(f"- required_tools: {', '.join(sk['required_tools'])}")
            lines.append(f"- prerequisites: {', '.join(sk['prerequisites']) or '-'}")
            lines.append("")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return path
