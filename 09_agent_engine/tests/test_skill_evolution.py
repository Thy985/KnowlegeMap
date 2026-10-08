"""v3 · Skill Evolution 端到端测试（tool_stats 数据驱动）。

覆盖：
- 样本不足不演进（防版本膨胀）
- 持续失败工具被剔除 + 演进理由引用真实成功率
- 工具按成功率重排（不剔除）
- 无显著变化不产生新版本
- 版本递增 + 最新版本复用
- 记忆持久化 round-trip
- 完整 pipeline 端到端触发
"""
import os
import tempfile
import unittest

from engine.domain import Agent, AgentMemory, SkillVersion, Task, ToolStat
from engine.memory import MemoryStore
from engine.pipeline import run_agent_task
from engine.skill_evolution import (evolve_skill, evolve_skills_for_caps,
                                    latest_skill)


def stat(usage: int, success: int, fms=None) -> ToolStat:
    return ToolStat(usage_count=usage, success_count=success,
                    success_rate=round(success / usage, 3) if usage else 0.0,
                    failure_modes=fms or {})


class TestSkillEvolution(unittest.TestCase):

    def test_01_insufficient_samples_no_evolution(self):
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["playwright"] = stat(2, 2)
        mem.tool_stats["mcp"] = stat(2, 0, {"timeout": 2})
        # 所有工具 usage < 3 → 不演进
        self.assertIsNone(evolve_skill("http-interaction", mem))

    def test_02_persistent_failure_tool_removed(self):
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["playwright"] = stat(3, 3)
        mem.tool_stats["mcp"] = stat(3, 0, {"timeout": 3})
        sv = evolve_skill("http-interaction", mem)
        self.assertIsNotNone(sv)
        self.assertEqual(sv.removed_tools, ["mcp"])
        self.assertEqual(sv.required_tools, ["playwright"])
        # 演进理由引用真实成功率
        self.assertIn("sr=0.00", sv.evolution_reason)
        # 高频 timeout 触发检查步骤
        self.assertTrue(any("超时" in s for s in sv.inserted_steps))
        self.assertIn("mcp", sv.inserted_steps[0])

    def test_03_tools_reordered_by_success_rate(self):
        # 两个工具成功率都 ≥0.5（不剔除），但有高低
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["garak"] = stat(3, 2)       # 0.667
        mem.tool_stats["playwright"] = stat(3, 3)  # 1.000
        sv = evolve_skill("vulnerability-detection", mem)
        self.assertEqual(sv.removed_tools, [])
        # 原顺序 garak,playwright → 重排 playwright,garak
        self.assertEqual(sv.required_tools, ["playwright", "garak"])

    def test_04_no_change_no_new_version(self):
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["playwright"] = stat(3, 3)
        mem.tool_stats["mcp"] = stat(3, 3)
        # 都 100% 成功，顺序不变，无失败 → 不产生新版本
        self.assertIsNone(evolve_skill("http-interaction", mem))

    def test_05_version_increment_and_reuse(self):
        mem = AgentMemory(agent_id="a")
        # 第一轮：mcp 3 次全失败
        mem.tool_stats["playwright"] = stat(3, 3)
        mem.tool_stats["mcp"] = stat(3, 0, {"timeout": 3})
        v1 = evolve_skill("http-interaction", mem)
        self.assertEqual(v1.version, 1)
        self.assertIn("mcp", v1.removed_tools)

        # 后续：mcp 又 3 次成功（total 6, success 3, sr=0.5 不再 <0.5）
        mem.tool_stats["mcp"] = stat(6, 3, {"timeout": 3})
        v2 = evolve_skill("http-interaction", mem)
        self.assertEqual(v2.version, 2)
        self.assertNotIn("mcp", v2.removed_tools)
        self.assertIn("mcp", v2.required_tools)

        # 复用最新版本（不重新从零）
        latest = latest_skill("http-interaction", mem)
        self.assertIs(latest, v2)
        self.assertEqual(len(mem.skill_versions["http-interaction"]), 2)

    def test_06_skill_versions_persist_roundtrip(self):
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["playwright"] = stat(3, 3)
        mem.tool_stats["mcp"] = stat(3, 0, {"timeout": 3})
        evolve_skill("http-interaction", mem)
        with tempfile.TemporaryDirectory() as d:
            store = MemoryStore(d)
            store.save_agent_memory(mem)
            loaded = store.load_agent_memory("a")
            self.assertIn("http-interaction", loaded.skill_versions)
            sv = loaded.skill_versions["http-interaction"][0]
            self.assertIsInstance(sv, SkillVersion)
            self.assertEqual(sv.removed_tools, ["mcp"])
            self.assertEqual(sv.required_tools, ["playwright"])

    def test_07_pipeline_triggers_skill_evolution(self):
        agent = Agent(agent_id="a", identity="t", role="pen-test",
                      objective="security",
                      available_tools=["garak", "playwright", "mcp", "promptfoo"],
                      environment={"platform": "linux", "sandbox": "docker"},
                      constraints=["authorized-only"], autonomy_level=3)
        mem = AgentMemory(agent_id="a")
        obs = {
            "detection-accuracy": {"score": 0.92, "observation": "garak 17/18"},
            "false-positive-rate": {"score": 0.85, "observation": "ok"},
            "evidence-completeness": {"score": 0.88, "observation": "captured"},
            "reproducibility": {"score": 0.90, "observation": "repro"},
        }
        for i in range(3):
            t = Task(task_id=f"t-{i}", task_type="security-assessment",
                     objective="对授权站点做安全测试", risk_level="high")
            tr = {tool: {"success": True, "failure_mode": ""}
                  for tool in ["garak", "playwright", "promptfoo"]}
            tr["mcp"] = {"success": False, "failure_mode": "timeout"}
            r = run_agent_task(agent, t, memory=mem,
                               observations=obs, tool_results=tr)
        # 第 3 次后 http-interaction 演进
        ids = [s.skill_id for s in r.evolved_skills]
        self.assertIn("http-interaction", ids)
        # 报告含 Skill Evolution 段
        self.assertIn("Skill Evolution", r.render_report())


if __name__ == "__main__":
    unittest.main()
