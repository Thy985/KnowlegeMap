"""v4 · 历史先验回灌 compose 端到端测试。

闭合"演进 → 影响未来选择"：
- 历史失败工具受 fit 惩罚，有替代时落选/被互斥排除
- 唯一提供者保留（不丢能力）并记录 history_warnings
- 真实 success_rate 校准可靠性
- 成功率回升后惩罚解除
- 无历史时行为不回归
"""
import unittest

from engine.composition import (HistoryPrior, build_history_prior, compose,
                               fit_score, evaluate_candidate, _tool)
from engine.domain import Agent, AgentMemory, Task, ToolStat
from engine.pipeline import run_agent_task
from engine.skill_evolution import evolve_skill


def tstat(usage: int, success: int, fms=None) -> ToolStat:
    return ToolStat(usage_count=usage, success_count=success,
                    success_rate=round(success / usage, 3) if usage else 0.0,
                    failure_modes=fms or {})


def task() -> Task:
    return Task(task_id="t", task_type="security-assessment",
                objective="安全测试", risk_level="high")


class TestHistoryPrior(unittest.TestCase):

    def test_01_failed_tool_loses_to_alternative(self):
        hist = HistoryPrior(
            tool_stats={"browser-use": tstat(3, 0, {"timeout": 3})},
            removed={"browser-use": "http-interaction(sr=0.00)"})
        chain = compose(["browser-use", "mcp"], task(),
                        ["http-interaction"], env={"platform": "linux"},
                        history=hist)
        # 历史失败的 browser-use 被降权，http-interaction 改选 mcp
        self.assertEqual(chain.capability_tool_map["http-interaction"], "mcp")
        self.assertNotIn("browser-use", chain.chain)

    def test_02_mutual_exclusion_uses_adjusted_fit(self):
        hist = HistoryPrior(
            tool_stats={"browser-use": tstat(3, 0, {"timeout": 3})},
            removed={"browser-use": "reconnaissance(sr=0.00)"})
        chain = compose(["browser-use", "playwright"], task(),
                        ["reconnaissance", "endpoint-discovery"],
                        env={"platform": "linux"}, history=hist)
        self.assertIn("browser-use", chain.excluded)
        self.assertIn("历史失败",
                      chain.excluded_reasons["browser-use"])

    def test_03_sole_provider_retained_with_warning(self):
        hist = HistoryPrior(
            tool_stats={"garak": tstat(3, 0, {"timeout": 3})},
            removed={"garak": "reconnaissance(sr=0.00)"})
        chain = compose(["garak"], task(), ["reconnaissance"],
                        env={"platform": "linux"}, history=hist)
        # 唯一提供者即使历史失败也保留（不丢能力）
        self.assertEqual(chain.capability_tool_map["reconnaissance"], "garak")
        self.assertNotIn("garak", chain.excluded)
        self.assertIn("garak", chain.history_warnings)
        self.assertIn("无替代", chain.history_warnings["garak"])

    def test_04_observed_success_calibrates_reliability_up(self):
        hist = HistoryPrior(tool_stats={"some-tool": tstat(3, 3)})
        static_rel = 0.6
        adj = hist.adjustment("some-tool", static_rel)
        # observed sr=1.0 > static 0.6 → 正校准
        self.assertGreater(adj, 0)
        # 无历史/无统计的工具 adjustment 为 0
        self.assertEqual(HistoryPrior().adjustment("unknown", 0.6), 0.0)

    def test_05_build_prior_removed_and_recovery(self):
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["playwright"] = tstat(3, 3)
        mem.tool_stats["mcp"] = tstat(3, 0, {"timeout": 3})
        evolve_skill("http-interaction", mem)
        hp = build_history_prior(mem)
        self.assertIn("mcp", hp.removed)
        # 成功率回升到 0.5（不再 <0.5）→ 解除
        mem.tool_stats["mcp"] = tstat(6, 3, {"timeout": 3})
        hp2 = build_history_prior(mem)
        self.assertNotIn("mcp", hp2.removed)

    def test_06_no_history_no_regression(self):
        caps = ["http-interaction", "endpoint-discovery"]
        c1 = compose(["browser-use", "playwright", "mcp"], task(),
                     caps, env={"platform": "linux"})
        c2 = compose(["browser-use", "playwright", "mcp"], task(),
                     caps, env={"platform": "linux"},
                     history=HistoryPrior())
        self.assertEqual(c1.chain, c2.chain)
        self.assertEqual(fit_score(evaluate_candidate(
            _tool("mcp"), task(), caps, {"platform": "linux"})),
                         fit_score(evaluate_candidate(
            _tool("mcp"), task(), caps, {"platform": "linux"})))

    def test_07_pipeline_uses_history(self):
        mem = AgentMemory(agent_id="a")
        mem.tool_stats["playwright"] = tstat(3, 3)
        mem.tool_stats["mcp"] = tstat(3, 0, {"timeout": 3})
        evolve_skill("http-interaction", mem)
        agent = Agent(agent_id="a", identity="t", role="pen-test",
                      objective="security",
                      available_tools=["garak", "playwright", "mcp", "promptfoo"],
                      environment={"platform": "linux", "sandbox": "docker"},
                      constraints=["authorized-only"], autonomy_level=3)
        obs = {
            "detection-accuracy": {"score": 0.92, "observation": "x"},
            "false-positive-rate": {"score": 0.85, "observation": "x"},
            "evidence-completeness": {"score": 0.88, "observation": "x"},
            "reproducibility": {"score": 0.90, "observation": "x"},
        }
        r = run_agent_task(agent, task(), memory=mem, observations=obs)
        # mcp 历史失败但无替代 → 保留并警告，不丢能力
        self.assertIn("mcp", r.chain.history_warnings)
        self.assertIn("mcp", r.chain.chain)


if __name__ == "__main__":
    unittest.main()
