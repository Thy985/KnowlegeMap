"""KnowlegeMap Agent-Centric Engine — Seed Knowledge Base.

种子知识库从仓库真实资产提取（38 张候选卡 + 35 star 基准 + 项目画像）：
- CAPABILITIES：能力定义 + 可实现工具候选（能力 ≠ 工具，一能力多工具）
- TASK_TYPES：任务类型 → 能力需求分解规则
- TOOLS：工具属性（接口/结构化/自动化/成本/权限/风险/证据来源）

证据字段 source_cards 指向 03_expansion_queue/candidates/ 或 00_bootstrap/00_starred_reference.md，
保证"发现"不凭空：每个工具/能力都有仓库内证据锚点。
"""
from __future__ import annotations

from typing import Dict, List

# ---------------------------------------------------------------- Capabilities
# capability_id -> {name, description, prerequisites, related_projects(种子候选), source}

CAPABILITIES: Dict[str, dict] = {
    "reconnaissance": {
        "name": "侦察与目标测绘",
        "description": "对授权目标进行信息收集、暴露面识别",
        "prerequisites": [],
        "candidate_tools": ["garak", "pyrit", "browser-use", "webwright"],
        "related_projects": ["dsh-pentest"],
        "source": "03_expansion_queue/candidates/[cand]ai-offensive-toolchain.md, [cand]agentic-attack-2026.md",
    },
    "endpoint-discovery": {
        "name": "端点发现",
        "description": "发现目标应用的端点/接口/路径",
        "prerequisites": ["reconnaissance"],
        "candidate_tools": ["browser-use", "webwright", "playwright"],
        "related_projects": ["dsh-pentest"],
        "source": "03_expansion_queue/candidates/[cand]browser-harness-2026.md",
    },
    "http-interaction": {
        "name": "HTTP 交互",
        "description": "构造与重放 HTTP 请求，处理会话",
        "prerequisites": ["endpoint-discovery"],
        "candidate_tools": ["mcp", "browser-use", "playwright"],
        "related_projects": ["dsh-pentest", "E2E-CLI"],
        "source": "03_expansion_queue/candidates/[cand]mcp-2026-07-28-stateless.md",
    },
    "vulnerability-detection": {
        "name": "漏洞检测",
        "description": "识别注入/越权/配置缺陷等安全漏洞",
        "prerequisites": ["http-interaction"],
        "candidate_tools": ["garak", "pyrit", "owasp-agentic-security"],
        "related_projects": ["dsh-pentest", "silver-shield"],
        "source": "03_expansion_queue/candidates/[cand]ai-offensive-toolchain.md, [cand]owasp-agentic-security.md",
    },
    "request-replay": {
        "name": "请求重放",
        "description": "将检测请求按轨迹重放用于验证与回归",
        "prerequisites": ["http-interaction"],
        "candidate_tools": ["playwright", "browser-use", "webwright"],
        "related_projects": ["E2E-CLI"],
        "source": "03_expansion_queue/candidates/[cand]webwright-2026.md",
    },
    "result-aggregation": {
        "name": "结果聚合",
        "description": "汇总多工具输出为统一结果集",
        "prerequisites": ["vulnerability-detection"],
        "candidate_tools": ["promptfoo", "langfuse", "agentevals"],
        "related_projects": ["silver-shield", "Validation 编译器"],
        "source": "03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md, [cand]otel-genai-observability.md",
    },
    "evidence-collection": {
        "name": "证据收集",
        "description": "为每个判定收集可追溯证据（请求/响应/轨迹）",
        "prerequisites": ["result-aggregation"],
        "candidate_tools": ["otel-genai", "langfuse", "promptfoo"],
        "related_projects": ["Validation 编译器", "silver-shield"],
        "source": "03_expansion_queue/candidates/[cand]otel-genai-observability.md, [cand]trace-based-agent-eval-2026.md",
    },
    "reporting": {
        "name": "报告生成",
        "description": "把结果+证据组织为可读报告",
        "prerequisites": ["evidence-collection"],
        "candidate_tools": ["promptfoo", "langfuse"],
        "related_projects": ["silver-shield"],
        "source": "03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md",
    },
    "browser-interaction": {
        "name": "浏览器交互",
        "description": "结构化浏览器操作（导航/点击/填表/提取）",
        "prerequisites": [],
        "candidate_tools": ["playwright", "browser-use", "webwright", "hermes-agent"],
        "related_projects": ["campus_order", "E2E-CLI", "agent-attention"],
        "source": "03_expansion_queue/candidates/[cand]browser-harness-2026.md, [cand]computer-browser-use-2026.md",
    },
    "sandbox-execution": {
        "name": "沙箱执行",
        "description": "在隔离环境执行不可信代码/工具",
        "prerequisites": [],
        "candidate_tools": ["e2b", "opencode"],
        "related_projects": ["TeamMind", "dsh-pentest", "EP-002"],
        "source": "03_expansion_queue/candidates/[cand]e2b-sandbox.md",
    },
    "agent-memory": {
        "name": "Agent 记忆",
        "description": "跨会话持久记忆：检索/写入/版本化",
        "prerequisites": [],
        "candidate_tools": ["mem0", "dsh-memory-evolve"],
        "related_projects": ["GrowthOS", "TeamMind", "dsh"],
        "source": "03_expansion_queue/candidates/[cand]agent-memory-2026.md, [cand]dsh-memory-evolve.md",
    },
    "agent-evaluation": {
        "name": "Agent 评测",
        "description": "以证据/执行真相评测 agent 行为与输出",
        "prerequisites": ["evidence-collection"],
        "candidate_tools": ["promptfoo", "agentevals", "deepseek-harness"],
        "related_projects": ["Validation 编译器", "silver-shield"],
        "source": "03_expansion_queue/candidates/[cand]agentic-benchmarks-2026.md, [cand]trace-based-agent-eval-2026.md",
    },
    "multi-agent-orchestration": {
        "name": "多 Agent 编排",
        "description": "多角色 agent 的任务分解/协作/状态管理",
        "prerequisites": [],
        "candidate_tools": ["openclaw", "langgraph", "a2a", "mcp"],
        "related_projects": ["TeamMind", "campus_order"],
        "source": "03_expansion_queue/candidates/[cand]multiagent-framework-2026.md, [cand]a2a-protocol-v1.md",
    },
    "local-inference": {
        "name": "本地推理",
        "description": "端侧/边缘模型推理与嵌入",
        "prerequisites": [],
        "candidate_tools": ["ollama", "glm-edge", "llamafile"],
        "related_projects": ["Tafcm", "silver-shield"],
        "source": "03_expansion_queue/candidates/[cand]local-edge-llm-2026.md",
    },
    "observability": {
        "name": "可观测性",
        "description": "日志/指标/追踪（含语义执行树）",
        "prerequisites": [],
        "candidate_tools": ["otel-genai", "langfuse"],
        "related_projects": ["Tafcm", "silver-shield", "TeamMind"],
        "source": "03_expansion_queue/candidates/[cand]otel-genai-observability.md",
    },
    "protocol-interop": {
        "name": "协议互操作",
        "description": "MCP/A2A 标准协议接入与互操作",
        "prerequisites": [],
        "candidate_tools": ["mcp", "a2a"],
        "related_projects": ["TeamMind", "agent-attention"],
        "source": "03_expansion_queue/candidates/[cand]mcp-2026-07-28-stateless.md, [cand]a2a-protocol-v1.md",
    },
    "security-governance": {
        "name": "安全治理",
        "description": "运行时权限边界/威胁清单/策略执行",
        "prerequisites": [],
        "candidate_tools": ["owasp-agentic-security", "agent-firewall"],
        "related_projects": ["EP-002", "silver-shield", "campus_order"],
        "source": "03_expansion_queue/candidates/[cand]owasp-agentic-security.md, [cand]agent-firewall-runtime-defense-2026.md",
    },
    "runtime-defense": {
        "name": "运行时防御",
        "description": "对越界/注入的实时拦截与告警",
        "prerequisites": ["security-governance"],
        "candidate_tools": ["agent-firewall"],
        "related_projects": ["silver-shield", "campus_order"],
        "source": "03_expansion_queue/candidates/[cand]agent-firewall-runtime-defense-2026.md",
    },
    "long-term-memory": {
        "name": "长期记忆",
        "description": "超长时域记忆：压缩/检索/版本回溯",
        "prerequisites": ["agent-memory"],
        "candidate_tools": ["mem0", "dsh-memory-evolve"],
        "related_projects": ["GrowthOS", "dsh"],
        "source": "03_expansion_queue/candidates/[cand]agent-memory-2026.md",
    },
    "state-persistence": {
        "name": "状态持久化",
        "description": "agent 运行状态可恢复（checkpoint/重启续跑）",
        "prerequisites": [],
        "candidate_tools": ["deepseek-harness", "openclaw", "langgraph"],
        "related_projects": ["TeamMind", "dsh"],
        "source": "03_expansion_queue/candidates/[cand]agent-harness-control-plane.md",
    },
    "scheduling": {
        "name": "任务调度",
        "description": "周期/延时/定时触发任务",
        "prerequisites": [],
        "candidate_tools": ["openclaw", "langgraph"],
        "related_projects": ["agent-attention", "TeamMind"],
        "source": "03_expansion_queue/candidates/[cand]multiagent-framework-2026.md",
    },
    "failure-recovery": {
        "name": "失败恢复",
        "description": "故障检测、重试、回滚",
        "prerequisites": ["state-persistence"],
        "candidate_tools": ["openclaw", "deepseek-harness"],
        "related_projects": ["TeamMind", "E2E-CLI"],
        "source": "03_expansion_queue/candidates/[cand]agent-harness-control-plane.md",
    },
    "monitoring": {
        "name": "运行监控",
        "description": "agent 运行状态/资源/成本监控",
        "prerequisites": ["observability"],
        "candidate_tools": ["otel-genai", "langfuse"],
        "related_projects": ["Tafcm", "TeamMind"],
        "source": "03_expansion_queue/candidates/[cand]otel-genai-observability.md",
    },
    "self-improvement": {
        "name": "自我改进",
        "description": "基于 evaluation 更新技能/工作流/选择规则",
        "prerequisites": ["agent-evaluation"],
        "candidate_tools": ["promptfoo", "agentevals"],
        "related_projects": ["Validation 编译器", "dsh"],
        "source": "03_expansion_queue/candidates/[cand]trace-based-agent-eval-2026.md",
    },
    "privacy-guard": {
        "name": "隐私防护",
        "description": "本地数据不出端、敏感信息脱敏",
        "prerequisites": ["local-inference"],
        "candidate_tools": ["ollama", "glm-edge"],
        "related_projects": ["Tafcm", "silver-shield"],
        "source": "03_expansion_queue/candidates/[cand]local-edge-llm-2026.md",
    },
    "embedding": {
        "name": "本地嵌入",
        "description": "本地 embedding 模型（文本/多模态）",
        "prerequisites": ["local-inference"],
        "candidate_tools": ["glm-edge", "ollama"],
        "related_projects": ["Tafcm"],
        "source": "03_expansion_queue/candidates/[cand]local-edge-llm-2026.md",
    },
    "assertion": {
        "name": "断言验证",
        "description": "对输出/行为做确定性断言",
        "prerequisites": ["result-aggregation"],
        "candidate_tools": ["promptfoo", "agentevals", "playwright"],
        "related_projects": ["Validation 编译器", "E2E-CLI"],
        "source": "03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md",
    },
}

# ---------------------------------------------------------------- Task Types
# task_type -> {required_capabilities（按依赖序）, risk_level, criteria, desired_output}

TASK_TYPES: Dict[str, dict] = {
    "security-assessment": {
        "required_capabilities": [
            "reconnaissance", "endpoint-discovery", "http-interaction",
            "vulnerability-detection", "request-replay", "result-aggregation",
            "evidence-collection", "reporting",
        ],
        "risk_level": "high",
        "desired_output": "漏洞清单 + 每个判定的证据链 + 复现步骤",
        "criteria": ["detection-accuracy", "false-positive-rate", "evidence-completeness", "reproducibility"],
        "note": "授权范围内的安全测试（EP-002：权限即边界；approval 前置）",
    },
    "e2e-web-testing": {
        "required_capabilities": [
            "browser-interaction", "http-interaction", "assertion",
            "evidence-collection", "reporting",
        ],
        "risk_level": "low",
        "desired_output": "E2E 测试报告 + 失败用例证据",
        "criteria": ["pass-rate", "coverage", "flakiness", "evidence-completeness"],
    },
    "long-running-autonomous-agent": {
        "required_capabilities": [
            "scheduling", "state-persistence", "long-term-memory", "failure-recovery",
            "monitoring", "multi-agent-orchestration", "tool-orchestration",
            "agent-evaluation", "self-improvement",
        ],
        "risk_level": "medium",
        "desired_output": "可持续运行的 agent 架构 + 恢复/评估机制",
        "criteria": ["uptime", "recovery-time", "memory-retention", "evaluation-loop"],
        "note": "tool-orchestration 由 multi-agent-orchestration 覆盖",
    },
    "local-mobile-ai-assistant": {
        "required_capabilities": [
            "local-inference", "embedding", "privacy-guard", "agent-memory", "observability",
        ],
        "risk_level": "low",
        "desired_output": "端侧离线可用的助手方案（推理/记忆/隐私）",
        "criteria": ["offline-capability", "latency", "privacy", "memory-retention"],
    },
    "multi-agent-team": {
        "required_capabilities": [
            "multi-agent-orchestration", "protocol-interop", "observability",
            "agent-memory", "security-governance",
        ],
        "risk_level": "medium",
        "desired_output": "多角色 agent 团队拓扑 + 协作协议 + 治理边界",
        "criteria": ["collaboration-efficiency", "protocol-interop", "governance-coverage"],
    },
    "agent-eval-harness": {
        "required_capabilities": [
            "agent-evaluation", "sandbox-execution", "evidence-collection",
            "observability", "reporting", "self-improvement",
        ],
        "risk_level": "medium",
        "desired_output": "以执行真相（数据库状态/副作用）评测 agent 的 harness",
        "criteria": ["truth-checking", "silent-failure-detection", "reproducibility"],
    },
}

# ---------------------------------------------------------------- Tools
# name -> Tool 属性（证据在 source_cards）

TOOLS: Dict[str, dict] = {
    "playwright": {
        "category": "browser", "interface": "CLI+SDK", "input_format": "script", "output_format": "structured",
        "environment_requirements": ["node/python"], "permissions": ["local-process"],
        "strengths": ["生态最成熟", "headless 脚本化", "跨浏览器"], "weaknesses": ["selector 脆弱", "页面变化敏感"],
        "cost": "low", "reliability": 0.85, "security_implications": ["需沙箱防滥用"],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.9,
        "capabilities": ["browser-interaction", "request-replay", "endpoint-discovery", "assertion"],
        "source_cards": ["[cand]browser-harness-2026", "[cand]computer-browser-use-2026"],
    },
    "browser-use": {
        "category": "browser", "interface": "CLI+SDK", "input_format": "task", "output_format": "structured",
        "environment_requirements": ["python"], "permissions": ["local-process"],
        "strengths": ["LLM 原生", "多模态", "agent 友好"], "weaknesses": ["较新", "token 消耗", "成本"],
        "cost": "med", "reliability": 0.7, "security_implications": ["需授权范围约束"],
        "automation_friendly": 0.95, "structured_output": 0.85, "ecosystem_maturity": 0.75,
        "capabilities": ["browser-interaction", "reconnaissance", "http-interaction", "request-replay"],
        "source_cards": ["[cand]browser-harness-2026", "[cand]computer-browser-use-2026"],
    },
    "webwright": {
        "category": "browser", "interface": "CLI", "input_format": "research-task", "output_format": "structured",
        "environment_requirements": ["ms-stack"], "permissions": ["local-process"],
        "strengths": ["研究型浏览器 agent", "可复现验证"], "weaknesses": ["微软系", "较新"],
        "cost": "low", "reliability": 0.65, "security_implications": [],
        "automation_friendly": 0.85, "structured_output": 0.8, "ecosystem_maturity": 0.5,
        "capabilities": ["browser-interaction", "reconnaissance", "endpoint-discovery", "request-replay"],
        "source_cards": ["[cand]webwright-2026"],
    },
    "e2b": {
        "category": "sandbox", "interface": "SDK+CLI", "input_format": "code", "output_format": "structured",
        "environment_requirements": ["cloud"], "permissions": ["isolated-exec"],
        "strengths": ["隔离执行", "一键环境", "可审计"], "weaknesses": ["云端依赖", "成本"],
        "cost": "med", "reliability": 0.8, "security_implications": ["沙箱边界 = 安全边界（EP-002）"],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.8,
        "capabilities": ["sandbox-execution"],
        "source_cards": ["[cand]e2b-sandbox"],
    },
    "mem0": {
        "category": "memory", "interface": "SDK", "input_format": "text", "output_format": "retrieved",
        "environment_requirements": ["api-key"], "permissions": ["memory-store"],
        "strengths": ["跨会话记忆成熟", "多后端"], "weaknesses": ["托管成本", "隐私外送"],
        "cost": "med", "reliability": 0.8, "security_implications": ["记忆污染面（PersistBench）"],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.85,
        "capabilities": ["agent-memory", "long-term-memory"],
        "source_cards": ["[cand]agent-memory-2026"],
    },
    "dsh-memory-evolve": {
        "category": "memory", "interface": "插件", "input_format": "text", "output_format": "retrieved",
        "environment_requirements": ["dsh-ecosystem"], "permissions": ["memory-store"],
        "strengths": ["与 dsh 生态契合", "harness 外记忆插件路线"], "weaknesses": ["新", "证据有限"],
        "cost": "low", "reliability": 0.5, "security_implications": ["记忆即证据库需版本回溯"],
        "automation_friendly": 0.85, "structured_output": 0.7, "ecosystem_maturity": 0.4,
        "capabilities": ["agent-memory", "long-term-memory"],
        "source_cards": ["[cand]dsh-memory-evolve（00_starred_reference）"],
    },
    "promptfoo": {
        "category": "evals", "interface": "CLI", "input_format": "config", "output_format": "structured",
        "environment_requirements": ["node"], "permissions": ["local-run"],
        "strengths": ["本地可跑", "matrix 评测", "断言丰富"], "weaknesses": ["agent 场景需自定义"],
        "cost": "low", "reliability": 0.85, "security_implications": [],
        "automation_friendly": 0.95, "structured_output": 0.95, "ecosystem_maturity": 0.9,
        "capabilities": ["agent-evaluation", "result-aggregation", "evidence-collection", "reporting", "assertion", "self-improvement"],
        "source_cards": ["[cand]promptfoo-agent-evals（validated 卡）"],
    },
    "agentevals": {
        "category": "evals", "interface": "SDK", "input_format": "trace", "output_format": "structured",
        "environment_requirements": ["python"], "permissions": ["local-run"],
        "strengths": ["trace-based 评测", "agent 轨迹即证据"], "weaknesses": ["较新"],
        "cost": "low", "reliability": 0.7, "security_implications": [],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.55,
        "capabilities": ["agent-evaluation", "evidence-collection", "assertion", "self-improvement"],
        "source_cards": ["[cand]trace-based-agent-eval-2026"],
    },
    "deepseek-harness": {
        "category": "harness", "interface": "CLI+SDK", "input_format": "agent-config", "output_format": "structured",
        "environment_requirements": ["local"], "permissions": ["local-run"],
        "strengths": ["多模态 agent harness", "sub-agent 编排", "插件生态"], "weaknesses": ["单一 provider 系"],
        "cost": "low", "reliability": 0.85, "security_implications": ["harness 权限面需治理"],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.85,
        "capabilities": ["state-persistence", "failure-recovery", "agent-evaluation", "self-improvement"],
        "source_cards": ["03_expansion_queue/validated/[val]deepseek-harness-2026"],
    },
    "openclaw": {
        "category": "orchestration", "interface": "CLI+Server", "input_format": "task", "output_format": "mixed",
        "environment_requirements": ["local/server"], "permissions": ["broad（需最小化）"],
        "strengths": ["多 agent 生态", "skills 体系", "活跃迭代"], "weaknesses": ["复杂度", "权限面大需审查"],
        "cost": "low", "reliability": 0.8, "security_implications": ["Operator Trust Model", "每版权限 diff"],
        "automation_friendly": 0.85, "structured_output": 0.7, "ecosystem_maturity": 0.85,
        "capabilities": ["multi-agent-orchestration", "scheduling", "failure-recovery", "state-persistence"],
        "source_cards": ["[cand]multiagent-framework-2026"],
    },
    "langgraph": {
        "category": "orchestration", "interface": "SDK", "input_format": "graph", "output_format": "structured",
        "environment_requirements": ["python"], "permissions": ["local-run"],
        "strengths": ["状态机编排", "可检查点"], "weaknesses": ["学习曲线"],
        "cost": "low", "reliability": 0.85, "security_implications": [],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.9,
        "capabilities": ["multi-agent-orchestration", "scheduling", "state-persistence"],
        "source_cards": ["[cand]multiagent-framework-2026"],
    },
    "a2a": {
        "category": "protocol", "interface": "SDK", "input_format": "agent-card", "output_format": "structured",
        "environment_requirements": ["net"], "permissions": ["service-auth"],
        "strengths": ["标准互操作", "AAIF 治理"], "weaknesses": ["生态成熟度"],
        "cost": "low", "reliability": 0.75, "security_implications": ["Agent Card supportedInterfaces 需对齐"],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.7,
        "capabilities": ["protocol-interop", "multi-agent-orchestration"],
        "source_cards": ["[cand]a2a-protocol-v1"],
    },
    "mcp": {
        "category": "protocol", "interface": "SDK", "input_format": "tool-schema", "output_format": "structured",
        "environment_requirements": ["net"], "permissions": ["tool-scope"],
        "strengths": ["工具标准化", "生态大"], "weaknesses": ["安全边界需治理"],
        "cost": "low", "reliability": 0.85, "security_implications": ["MCP03 Tool Poisoning / Supply Chain（AST↔MCP）"],
        "automation_friendly": 0.95, "structured_output": 0.95, "ecosystem_maturity": 0.9,
        "capabilities": ["protocol-interop", "http-interaction"],
        "source_cards": ["[cand]mcp-2026-07-28-stateless", "[cand]mcp-notification-servers"],
    },
    "otel-genai": {
        "category": "observability", "interface": "SDK", "input_format": "span", "output_format": "traces",
        "environment_requirements": ["otel-collector"], "permissions": ["telemetry"],
        "strengths": ["标准语义", "执行树建模", "IETF 化"], "weaknesses": ["配置复杂"],
        "cost": "low", "reliability": 0.85, "security_implications": ["敏感数据脱敏（redaction）"],
        "automation_friendly": 0.9, "structured_output": 0.95, "ecosystem_maturity": 0.85,
        "capabilities": ["observability", "evidence-collection", "monitoring"],
        "source_cards": ["[cand]otel-genai-observability"],
    },
    "langfuse": {
        "category": "observability", "interface": "SaaS+SDK", "input_format": "trace", "output_format": "dashboards",
        "environment_requirements": ["cloud/self-host"], "permissions": ["telemetry"],
        "strengths": ["全栈 trace+eval 一体化"], "weaknesses": ["托管成本"],
        "cost": "med", "reliability": 0.85, "security_implications": [],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.85,
        "capabilities": ["observability", "result-aggregation", "evidence-collection", "monitoring", "reporting"],
        "source_cards": ["[cand]otel-genai-observability"],
    },
    "garak": {
        "category": "redteam", "interface": "CLI", "input_format": "model-target", "output_format": "structured",
        "environment_requirements": ["python"], "permissions": ["target-auth（授权）"],
        "strengths": ["LLM 漏洞扫描", "插件化"], "weaknesses": ["检测深度有限"],
        "cost": "low", "reliability": 0.75, "security_implications": ["仅授权目标使用"],
        "automation_friendly": 0.9, "structured_output": 0.9, "ecosystem_maturity": 0.8,
        "capabilities": ["reconnaissance", "vulnerability-detection"],
        "source_cards": ["[cand]ai-offensive-toolchain"],
    },
    "pyrit": {
        "category": "redteam", "interface": "SDK", "input_format": "attack-plan", "output_format": "structured",
        "environment_requirements": ["python"], "permissions": ["target-auth（授权）"],
        "strengths": ["微软对抗工具", "可编排"], "weaknesses": ["需适配"],
        "cost": "low", "reliability": 0.75, "security_implications": ["仅授权目标使用"],
        "automation_friendly": 0.85, "structured_output": 0.85, "ecosystem_maturity": 0.75,
        "capabilities": ["reconnaissance", "vulnerability-detection"],
        "source_cards": ["[cand]ai-offensive-toolchain"],
    },
    "owasp-agentic-security": {
        "category": "governance", "interface": "framework", "input_format": "threat-model", "output_format": "guidance",
        "environment_requirements": [], "permissions": [],
        "strengths": ["权威威胁清单", "AST↔MCP 映射", "AIVSS 评分"], "weaknesses": ["需工程落地"],
        "cost": "low", "reliability": 0.9, "security_implications": ["标准基座"],
        "automation_friendly": 0.5, "structured_output": 0.6, "ecosystem_maturity": 0.85,
        "capabilities": ["security-governance", "vulnerability-detection"],
        "source_cards": ["[cand]owasp-agentic-security"],
    },
    "agent-firewall": {
        "category": "runtime-defense", "interface": "service", "input_format": "traffic", "output_format": "alerts",
        "environment_requirements": ["runtime"], "permissions": ["intercept"],
        "strengths": ["运行时拦截", "品类成熟（Aigis/Guardian/AgentGuard）"], "weaknesses": ["部署较重"],
        "cost": "med", "reliability": 0.75, "security_implications": ["拦截面需白名单"],
        "automation_friendly": 0.6, "structured_output": 0.8, "ecosystem_maturity": 0.7,
        "capabilities": ["runtime-defense", "security-governance"],
        "source_cards": ["[cand]agent-firewall-runtime-defense-2026"],
    },
    "ollama": {
        "category": "local-inference", "interface": "CLI+API", "input_format": "model", "output_format": "text",
        "environment_requirements": ["local-gpu"], "permissions": ["local-run"],
        "strengths": ["本地一键跑", "生态好"], "weaknesses": ["大模型硬件门槛"],
        "cost": "low", "reliability": 0.9, "security_implications": ["数据不出端"],
        "automation_friendly": 0.95, "structured_output": 0.7, "ecosystem_maturity": 0.95,
        "capabilities": ["local-inference", "privacy-guard", "embedding"],
        "source_cards": ["[cand]local-edge-llm-2026"],
    },
    "glm-edge": {
        "category": "local-inference", "interface": "model", "input_format": "model", "output_format": "text",
        "environment_requirements": ["edge-hardware"], "permissions": ["local-run"],
        "strengths": ["国产 agentic 边缘", "函数调用定位"], "weaknesses": ["新", "硬件依赖"],
        "cost": "low", "reliability": 0.65, "security_implications": ["数据不出端"],
        "automation_friendly": 0.75, "structured_output": 0.7, "ecosystem_maturity": 0.6,
        "capabilities": ["local-inference", "privacy-guard", "embedding"],
        "source_cards": ["[cand]local-edge-llm-2026"],
    },
    "llamafile": {
        "category": "local-inference", "interface": "CLI", "input_format": "model", "output_format": "text",
        "environment_requirements": ["local"], "permissions": ["local-run"],
        "strengths": ["单文件分发"], "weaknesses": ["生态较窄"],
        "cost": "low", "reliability": 0.7, "security_implications": [],
        "automation_friendly": 0.85, "structured_output": 0.6, "ecosystem_maturity": 0.7,
        "capabilities": ["local-inference", "privacy-guard"],
        "source_cards": ["[cand]flutter-local-llm-2026"],
    },
    "hermes-agent": {
        "category": "agent-framework", "interface": "SDK", "input_format": "task", "output_format": "structured",
        "environment_requirements": ["python"], "permissions": ["local-run"],
        "strengths": ["开源 agent 框架", "高 star"], "weaknesses": ["与 OpenClaw 生态竞争"],
        "cost": "low", "reliability": 0.7, "security_implications": [],
        "automation_friendly": 0.85, "structured_output": 0.8, "ecosystem_maturity": 0.75,
        "capabilities": ["browser-interaction"],
        "source_cards": ["[cand]hermes-agent-2026"],
    },
    "opencode": {
        "category": "coding-agent", "interface": "headless-http", "input_format": "task", "output_format": "structured",
        "environment_requirements": ["node"], "permissions": ["local-run"],
        "strengths": ["headless 服务化", "agent 可调用"], "weaknesses": ["编码域聚焦"],
        "cost": "low", "reliability": 0.8, "security_implications": ["执行域需沙箱"],
        "automation_friendly": 0.9, "structured_output": 0.85, "ecosystem_maturity": 0.8,
        "capabilities": ["sandbox-execution"],
        "source_cards": ["[cand]opencode-agent-2026"],
    },
}

# ---------------------------------------------------------------- 弱信号声明
STAR_SIGNAL_NOTE = (
    "Star 数仅作弱信号（原则：不因知名自动加分）。工具的 reliability/ecosystem_maturity "
    "综合自候选卡证据（FACT/DESIGN）+ star 基准（00_bootstrap/00_starred_reference.md）。"
)


def get_capability(cap_id: str) -> dict:
    return CAPABILITIES[cap_id]


def get_task_type(task_type: str) -> dict:
    return TASK_TYPES[task_type]


def get_tool(name: str) -> dict:
    return TOOLS[name]


def all_tool_names() -> List[str]:
    return sorted(TOOLS.keys())


def capability_candidates(cap_id: str) -> List[str]:
    """某能力的所有可实现工具候选（含未知能力发现的扩展钩子）。"""
    return list(CAPABILITIES.get(cap_id, {}).get("candidate_tools", []))
