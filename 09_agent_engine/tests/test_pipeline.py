"""KnowlegeMap Agent-Centric Engine — End-to-End Tests（Test 1-5）。

覆盖：
  Test 1  Human Cognitive Expansion（旧功能不回归）
  Test 2  Agent Task Expansion（Task → Capability Tree → Gap → Tools → Workflow）
  Test 3  Tool Composition（A/B/C/D → A→C→D，排除 B 并说明）
  Test 4  Agent Memory（两次相似任务，复用历史工作流）
  Test 5  Capability Evolution（unknown → validated，留 Evidence）

运行：cd 09_agent_engine && python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import knowledge                              # noqa: E402
from engine.capability_graph import CapabilityGraph      # noqa: E402
from engine.domain import Agent, Task                     # noqa: E402
from engine.memory import MemoryStore                     # noqa: E402
from engine.pipeline import PipelineResult, run_agent_task  # noqa: E402
from engine.trees import (instantiate_capability_tree,   # noqa: E402
                          jit_expand, render_tree)

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SECURITY_OBS = {
    "detection-accuracy": {"score": 0.92, "evidence": "garak 检出 17/18 已知漏洞", "failure": ""},
    "false-positive-rate": {"score": 0.85, "evidence": "playwright 重放验证 3 个候选", "failure": "2 个 false-positive 候选"},
    "evidence-completeness": {"score": 0.88, "evidence": "promptfoo 证据链完整 16/18", "failure": ""},
    "reproducibility": {"score": 0.90, "evidence": "两次运行结果一致", "failure": ""},
}


def make_agent(agent_id="test-agent", capabilities=None) -> Agent:
    return Agent(
        agent_id=agent_id, identity=f"{agent_id}（test）",
        role="generic executor", objective="按任务发现能力并构建工具链",
        capabilities=capabilities or {}, autonomy_level=3)


def make_task(task_type="security-assessment", objective="",
              task_id="t", risk="") -> Task:
    ttype = knowledge.get_task_type(task_type)
    return Task(
        task_id=task_id, task_type=task_type,
        objective=objective or ttype.get("desired_output", task_type),
        risk_level=risk or ttype.get("risk_level", "low"),
        desired_output=ttype.get("desired_output", ""),
        evaluation_criteria=list(ttype.get("criteria", [])))


# ============================================================
# Test 1 — Human Cognitive Expansion（不回归）
# ============================================================
class Test1_HumanCognitiveExpansion(unittest.TestCase):

    def test_human_assets_intact(self):
        for path in [
            "06_expansion_index/README.md", "03_expansion_queue/README.md",
            "99_templates/candidate_card.md", "07_radar_watch/README.md",
            "04_connections/README.md",
        ]:
            full = os.path.join(REPO_ROOT, path)
            self.assertTrue(os.path.exists(full), f"Human 资产缺失：{path}")
            with open(full, encoding="utf-8") as f:
                self.assertGreater(len(f.read()), 100)

    def test_human_dedup_reference_readable(self):
        idx = os.path.join(REPO_ROOT, "06_expansion_index/README.md")
        with open(idx, encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[cand]", content)
        self.assertIn("[validated]", content)

    def test_human_template_compatible(self):
        with open(os.path.join(REPO_ROOT, "99_templates/candidate_card.md"),
                  encoding="utf-8") as f:
            tpl = f.read()
        for required in ("一句话定位", "它解决什么问题", "证据与验证计划", "决策"):
            self.assertIn(required, tpl)


# ============================================================
# Test 2 — Agent Task Expansion（Capability Tree）
# ============================================================
class Test2_AgentTaskExpansion(unittest.TestCase):

    def test_full_chain(self):
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-b")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp),
                                    observations=SECURITY_OBS)
        self.assertIsInstance(result, PipelineResult)
        self.assertEqual(len(result.required_capabilities), 8)
        self.assertTrue(result.discovered_tools["vulnerability-detection"])
        self.assertTrue(result.chain)
        self.assertIsNotNone(result.workflow)
        self.assertEqual(len(result.workflow.stages), 8)
        self.assertGreater(result.evaluation.score, 0.5)
        self.assertTrue(result.approval_required)

    def test_capability_tree_structure(self):
        """树层级：分支 → 子能力数量与 maps_to 正确。"""
        nodes = instantiate_capability_tree("security-assessment")
        recon = nodes["reconnaissance"]
        self.assertEqual(len(recon.children), 4)          # Asset/Subdomain/Service/Fingerprint
        self.assertEqual(recon.maps_to, "reconnaissance")
        mapping = nodes["web-mapping"]
        self.assertEqual(len(mapping.children), 4)       # URL/Endpoint/API/JS
        self.assertEqual(nodes["vulnerability-assessment"].maps_to,
                         "vulnerability-detection")
        self.assertEqual(len(nodes["vulnerability-assessment"].children), 5)
        self.assertEqual(len(nodes["evidence"].children), 3)
        self.assertEqual(len(nodes["reporting"].children), 3)
        # 叶子点分路径
        leaf = nodes["reconnaissance.asset-discovery"]
        self.assertEqual(leaf.parent, "reconnaissance")
        self.assertTrue(leaf.is_leaf())

    def test_tree_dynamic_per_task(self):
        """不同 Task 动态产生不同 Capability Tree。"""
        sec = instantiate_capability_tree("security-assessment")
        e2e = instantiate_capability_tree("e2e-web-testing")
        self.assertNotEqual(
            sec["root.security-assessment"].children,
            e2e["root.e2e-web-testing"].children)
        # 同域不同任务：security 有 vulnerability-assessment，e2e 没有
        self.assertIn("vulnerability-assessment",
                      sec["root.security-assessment"].children)
        self.assertNotIn("vulnerability-assessment",
                         e2e["root.e2e-web-testing"].children)

    def test_unknown_capability_discovery(self):
        agent = make_agent()
        task = make_task(task_type="long-running-autonomous-agent",
                         objective="构建长期运行的自主 Agent（调度/记忆/恢复）",
                         task_id="t-u")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        self.assertTrue(result.unknown_capabilities)
        self.assertIn("scheduling", result.required_capabilities)


# ============================================================
# Test 3 — Tool Composition（A→C→D，排除 B）
# ============================================================
class Test3_ToolComposition(unittest.TestCase):

    def test_A_C_D_exclude_B(self):
        """候选 A=garak B=browser-use C=playwright D=promptfoo。

        期望组合 A→C→D，B 被互斥裁决排除并给出理由。
        """
        from engine.composition import compose
        task = make_task(task_type="security-assessment", task_id="t-3")
        caps = knowledge.get_task_type("security-assessment")["required_capabilities"]
        chain = compose(["garak", "browser-use", "playwright", "promptfoo"],
                        task, caps, {})
        self.assertEqual(chain.chain, ["garak", "playwright", "promptfoo"])
        self.assertEqual(chain.excluded, ["browser-use"])
        reason = chain.excluded_reasons["browser-use"]
        self.assertTrue(reason)
        self.assertIn("playwright", reason)
        self.assertIn("0.723 < 0.725", reason)

    def test_composition_reasons(self):
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-d")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        for name in result.chain.chain:
            r = result.chain.reasons[name]
            self.assertGreater(r.task_fit, 0)
            self.assertGreater(r.automation_friendliness, 0)
            self.assertTrue(r.note)
            self.assertTrue(r.security_risk)

    def test_fallback_after_exclusion(self):
        """互斥排除后，能力回退次优候选（http-interaction → mcp）。"""
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-d2")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        self.assertEqual(result.chain.capability_tool_map["http-interaction"],
                         "mcp")
        self.assertIn("mcp", result.chain.chain)

    def test_star_is_weak_signal_only(self):
        agent = make_agent()
        task = make_task(task_type="security-assessment", task_id="t-d3")
        with tempfile.TemporaryDirectory() as tmp:
            result = run_agent_task(agent, task, store=MemoryStore(tmp))
        self.assertIn("garak", result.chain.reasons)


# ============================================================
# Test 4 — Agent Memory（两次相似任务，复用历史）
# ============================================================
class Test4_AgentMemory(unittest.TestCase):

    def test_reuse_workflow(self):
        agent = make_agent()
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            t1 = make_task(task_type="security-assessment", task_id="t-f1",
                           objective="对授权网站 A 执行安全测试")
            r1 = run_agent_task(agent, t1, store=store, observations=SECURITY_OBS)
            self.assertEqual(r1.workflow.version, 1)

            t2 = make_task(task_type="security-assessment", task_id="t-f2",
                           objective="对授权网站 B 执行安全测试")
            r2 = run_agent_task(agent, t2, store=store, observations=SECURITY_OBS)

            self.assertTrue(r2.history_reused)
            self.assertEqual(r2.workflow.version, 2)
            self.assertTrue(r2.workflow.evolution_reason)
            mem = store.load_agent_memory(agent.agent_id)
            self.assertEqual(len(mem.workflow_versions["security-assessment"]), 2)
            self.assertEqual(len(mem.task_log), 2)

    def test_similarity_scoring(self):
        agent = make_agent()
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            r1 = run_agent_task(
                agent, make_task(task_type="security-assessment", task_id="t-f3"),
                store=store, observations=SECURITY_OBS)
            mem = store.load_agent_memory(agent.agent_id)
            similar = mem.find_similar_tasks(
                make_task(task_type="security-assessment", task_id="t-f4"),
                profile=set(r1.required_capabilities))
            self.assertEqual(len(similar), 1)
            self.assertEqual(similar[0].task.task_id, "t-f3")


# ============================================================
# Test 5 — Capability Evolution（unknown → validated）
# ============================================================
class Test5_CapabilityEvolution(unittest.TestCase):

    def test_unknown_to_validated_with_evidence(self):
        """连续成功执行：capability unknown(0) → validated(≥0.5)，留 Evidence。"""
        agent = make_agent()
        cap = "reconnaissance"
        self.assertNotIn(cap, agent.capabilities)      # unknown
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(tmp)
            for i in range(3):
                t = make_task(task_type="security-assessment",
                              task_id=f"t-e{i}", objective=f"安全测试 {i}")
                r = run_agent_task(agent, t, store=store,
                                   observations=SECURITY_OBS)
            self.assertGreaterEqual(agent.capabilities[cap], 0.5)  # validated
            self.assertTrue(r.evaluation.evidence)                 # 有证据
            self.assertTrue(any(
                "garak" in e.supporting_observation
                for e in r.evaluation.evidence))
            mem = store.load_agent_memory(agent.agent_id)
            self.assertGreater(mem.tool_stats["garak"].usage_count, 0)

    def test_failure_shapes_capability(self):
        """失败 → 弱点 + 失败模式 + 置信下降。"""
        agent = make_agent(capabilities={"reconnaissance": 0.6})
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
            self.assertTrue(mem.failure_patterns)
            self.assertTrue(agent.weaknesses)
            self.assertLess(agent.capabilities["reconnaissance"], 0.6)

    def test_jit_pruning_skips_covered_branch(self):
        """JIT：已具备分支剪枝不展开，只展开缺失分支。"""
        agent = make_agent(capabilities={"reconnaissance": 0.95})
        nodes = instantiate_capability_tree("security-assessment")
        jit_expand(nodes, agent)
        recon = nodes["reconnaissance"]
        self.assertFalse(recon.gap)
        self.assertFalse(recon.expanded)               # 剪枝：不展开
        leaf = nodes["reconnaissance.asset-discovery"]
        self.assertFalse(leaf.expanded)                # 子能力未被展开
        # 缺失分支仍展开
        self.assertTrue(nodes["web-mapping"].expanded)

    def test_capability_graph_cross_domain(self):
        """Graph：http-interaction 跨 4 领域复用；删它有传递影响。"""
        g = CapabilityGraph()
        self.assertEqual(
            set(g.domains_of("http-interaction")),
            {"web-security", "api-testing", "web-automation", "browser-agents"})
        shared = g.shared_capabilities("web-security", "api-testing")
        self.assertIn("http-interaction", shared)
        self.assertIn("browser-interaction",
                      g.shared_capabilities("web-automation", "browser-agents"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
