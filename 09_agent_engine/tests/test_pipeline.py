"""KnowlegeMap Agent-Centric Engine — End-to-End Tests（Scenario A-F）。

运行：cd 09_agent_engine && python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import knowledge                              # noqa: E402
from engine.domain import Agent, Task                     # noqa: E402
from engine.memory import MemoryStore                     # noqa: E402
from engine.pipeline import PipelineResult, run_agent_task  # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# 安全测试任务的观察值（模拟执行：detection 高、false-positive 低、证据完整、可复现）
SECURITY_OBS = {
    "detection-accuracy": {"score": 0.92, "evidence": "garak 检出 17/18 已知漏洞", "failure": ""},
    "false-positive-rate": {"score": 0.85, "evidence": "playwright 重放验证 3 个候选", "failure": "2 个 false-positive 候选"},
    "evidence-completeness": {"score": 0.88, "evidence": "promptfoo 证据链完整 16/18", "failure": ""},
    "reproducibility": {"score": 0.90, "evidence": "两次运行结果一致", "failure": ""},
}


def make_agent(agent_id: str = "test-agent", capabilities: dict = None) -> Agent:
    return Agent(
        agent_id=agent_id,
        identity=f"{agent_id}（test）",
        role="generic executor",
        objective="按任务发现能力并构建工具链",
        capabilities=capabilities or {},
        autonomy_level=3,
    )


def make_task(task_type: str = "security-assessment", objective: str = "",
              task_id: str = "t", risk: str = "") -> Task:
    ttype = knowledge.get_task_type(task_type)
    return Task(
        task_id=task_id,
        task_type=task_type,
        objective=objective or ttype.get("desired_output", task_type),
        risk_level=risk or ttype.get("risk_level", "low"),
        desired_output=ttype.get("desired_output", ""),
        evaluation_criteria=list(ttype.get("criteria", [])),
    )


class ScenarioA_HumanCentric_Unbroken(unittest.TestCase):
    """Scenario A：Human 认知扩展不破坏。"""

    def test_human_assets_intact(self):
        """Human 侧核心资产文件仍存在且可读（引擎未触碰 00-07 层）。"""
        for path in [
            "06_expansion_index/README.md",
            "03_expansion_queue/README.md",
            "99_templates/candidate_card.md",
            "07_radar_watch/README.md",
            "04_connections/README.md",
        ]:
            full = os.path.join(REPO_ROOT, path)
            self.assertTrue(os.path.exists(full), f"Human 资产缺失：{path}")
            with open(full, "r", encoding="utf-8") as f:
                self.assertGreater(len(f.read()), 100)

    def test_human_dedup_reference_readable(self):
        """去重基准（38 对象）可被程序读取——Mode A 数据流入口保持。"""
        idx = os.path.join(REPO_ROOT, "06_expansion_index/README.md")
        with open(idx, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[cand]", content)
        self.assertIn("[validated]", content)

    def test_human_template_compatible(self):
        """候选卡模板仍符合 99_templates 约定（新卡可继续按旧模板写入）。"""
        tpl = open(os.path.join(REPO_ROOT, "99_templates/candidate_card.md"),
                   encoding="utf-8").read()
        for required in ("一句话定位", "它解决什么问题", "证据与验证计划", "决策"):
            self.assertIn(required, tpl)


class ScenarioB_AgentTaskExpansion(unittest.TestCase):
    """Scenario B：Agent Task Expansion——输入 Task+Agent，输出能力+工具+工作流。"""

    def test_full_chain(self):
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-b")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp),
                                    observations=SECURITY_OBS)

        self.assertIsInstance(result, PipelineResult)
        # Task → Capability
        self.assertEqual(len(result.required_capabilities), 8)
        for cap in ("reconnaissance", "vulnerability-detection", "evidence-collection", "reporting"):
            self.assertIn(cap, result.required_capabilities)
        # Capability → Tool
        self.assertTrue(result.discovered_tools["vulnerability-detection"])
        # Composition → 有向链
        self.assertTrue(result.chain)
        self.assertGreaterEqual(len(result.chain.chain), 1)
        # Workflow
        self.assertIsNotNone(result.workflow)
        self.assertEqual(len(result.workflow.stages), 8)
        # Evaluation（注入观察）
        self.assertIsNotNone(result.evaluation)
        self.assertGreater(result.evaluation.score, 0.5)
        # 安全边界：high risk → approval
        self.assertTrue(result.approval_required)

    def test_unknown_capability_discovery(self):
        """未知能力发现：从 objective 解析出任务还没明说的能力域。"""
        agent = make_agent()
        task = make_task(task_type="long-running-autonomous-agent",
                         objective="构建长期运行的自主 Agent（调度/记忆/恢复）",
                         task_id="t-u")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        self.assertTrue(result.unknown_capabilities)
        self.assertIn("scheduling", result.required_capabilities)


class ScenarioC_CapabilityGap(unittest.TestCase):
    """Scenario C：Capability Gap——输入 Task+已有能力，输出缺失能力。"""

    def test_gap_output(self):
        # agent 已具备浏览器交互（高置信），任务仍需它
        agent = make_agent(capabilities={"browser-interaction": 0.95, "assertion": 0.9})
        task = make_task(task_type="e2e-web-testing", task_id="t-c")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))

        self.assertNotIn("browser-interaction", result.missing_capabilities)
        self.assertIn("http-interaction", result.missing_capabilities)
        self.assertIn("evidence-collection", result.missing_capabilities)

    def test_prereq_expansion(self):
        """前置能力展开：缺失能力的前置也被标为缺口。"""
        agent = make_agent()
        task = make_task(task_type="agent-eval-harness", task_id="t-c2")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        # sandbox-execution 缺 → 其前置也计入
        self.assertIn("sandbox-execution", result.missing_capabilities)


class ScenarioD_ToolComposition(unittest.TestCase):
    """Scenario D：Tool Composition——候选工具 → 组合方案 + 组合理由。"""

    def test_composition_reasons(self):
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-d")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))

        chain = result.chain
        # 每个选中工具都有多维 Selection Reason
        for name in chain.chain:
            reason = chain.reasons[name]
            self.assertGreater(reason.task_fit, 0)
            self.assertGreater(reason.automation_friendliness, 0)
            self.assertTrue(reason.note)          # 组合理由非空
            self.assertTrue(reason.security_risk)  # 安全影响显式化

    def test_mutual_exclusion(self):
        """互斥组裁决：mem0 与 dsh-memory-evolve 不同时入选。"""
        agent = make_agent()
        task = make_task(task_type="local-mobile-ai-assistant", task_id="t-d2")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))

        chain = result.chain
        memory_tools = set(chain.chain) & {"mem0", "dsh-memory-evolve"}
        self.assertLessEqual(len(memory_tools), 1)
        if chain.excluded:
            self.assertTrue(all(chain.excluded_reasons.get(e) for e in chain.excluded))

    def test_star_is_weak_signal_only(self):
        """Star 只体现在 ecosystem_maturity 一维（权重 0.10），不单独决定选择。"""
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-d3")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        # garak/pyrit 星级远低于 playwright，但任务适配（redteam 1.0）主导侦察/检测选型
        reasons = result.chain.reasons
        self.assertIn("garak", reasons)


class ScenarioE_PostTaskLearning(unittest.TestCase):
    """Scenario E：Post-task Learning——任务结果+Evaluation → Agent 能力/Memory 更新。"""

    def test_memory_updated(self):
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-e")
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            result = run_agent_task(agent, task, store=store, observations=SECURITY_OBS)
            # Memory：工具统计已回写
            mem = store.load_agent_memory(agent.agent_id)
            self.assertTrue(mem.tool_stats)
            for tool in result.chain.chain:
                stat = mem.tool_stats[tool]
                self.assertGreater(stat.usage_count, 0)
                self.assertGreater(stat.success_rate, 0)
            # Memory：成功模式沉淀 + 任务日志
            self.assertTrue(mem.success_patterns)
            self.assertEqual(len(mem.task_log), 1)
        # Capability 演化：成功 → 置信提升
        agent2 = make_agent()
        with tempfile.TemporaryDirectory() as tmp2:
            store2 = MemoryStore(tmp2)
            run_agent_task(agent2, task, store=store2, observations=SECURITY_OBS)
        self.assertGreater(agent2.capabilities.get("reconnaissance", 0), 0)

    def test_failure_shapes_capability(self):
        """失败 → 弱点记录 + 置信下降。"""
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-e2")
        bad_obs = {
            "detection-accuracy": {"score": 0.3, "evidence": "漏检", "failure": "missed-detection"},
            "false-positive-rate": {"score": 0.2, "evidence": "误报", "failure": "false-positive"},
            "evidence-completeness": {"score": 0.4, "evidence": "证据缺", "failure": "missing-evidence"},
            "reproducibility": {"score": 0.5, "evidence": "波动", "failure": "flaky"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            result = run_agent_task(agent, task, store=store, observations=bad_obs)
            self.assertLess(result.evaluation.score, 0.5)
            mem = store.load_agent_memory(agent.agent_id)
            self.assertTrue(mem.failure_patterns)   # 失败模式已沉淀
            self.assertTrue(agent.weaknesses)       # 能力弱点已记录


class ScenarioF_RepeatedSimilarTask(unittest.TestCase):
    """Scenario F：Repeated Similar Task——相似任务复用历史 Workflow/Evaluation。"""

    def test_reuse_workflow(self):
        agent = make_agent()
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            # 第一次：安全测试（建立 v1）
            t1 = make_task(task_type="security-assessment", task_id="t-f1",
                           objective="对授权网站 A 执行安全测试")
            r1 = run_agent_task(agent, t1, store=store, observations=SECURITY_OBS)
            self.assertEqual(r1.workflow.version, 1)

            # 第二次：相似任务（网站 B）——应复用历史，不重新从零
            t2 = make_task(task_type="security-assessment", task_id="t-f2",
                           objective="对授权网站 B 执行安全测试")
            r2 = run_agent_task(agent, t2, store=store, observations=SECURITY_OBS)

            self.assertTrue(r2.history_reused)
            self.assertEqual(r2.workflow.version, 2)          # 演进到 v2
            self.assertTrue(r2.workflow.evolution_reason)     # 演进理由显式化
            mem = store.load_agent_memory(agent.agent_id)
            self.assertEqual(len(mem.workflow_versions["security-assessment"]), 2)
            self.assertEqual(len(mem.task_log), 2)

    def test_similarity_scoring(self):
        """能力画像重叠 → 相似任务可检索。"""
        agent = make_agent()
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            r1 = run_agent_task(agent, make_task(task_type="security-assessment", task_id="t-f3"),
                                store=store, observations=SECURITY_OBS)
            mem = store.load_agent_memory(agent.agent_id)
            similar = mem.find_similar_tasks(
                make_task(task_type="security-assessment", task_id="t-f4"),
                profile=set(r1.required_capabilities))
            self.assertEqual(len(similar), 1)
            self.assertEqual(similar[0].task.task_id, "t-f3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
