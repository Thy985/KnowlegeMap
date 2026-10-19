# 候选对象证据卡 · agent-aegis（开源 AI 治理框架：Guardrails + Policy + Protocol）

> 状态：`[cand]` ｜ 关联方向：Harness/治理 C 层（权限与策略治理）/ D 层（运行时防御）｜ 日期：2026-10-20（Harness 周 Day2 增量扫描）

## 一句话定位
PyPI 开源 AI 治理框架 **agent-aegis**（0.4.0，2026-10-15 更新）：`aegis.init()` 一键接入，运行时 guardrails（PII/注入检测）+ **YAML 声明式策略引擎**（approval gates）+ 开放标准（AGEF/AGP）三合一，面向"确定性 guardrail + 策略引擎"一体化的 agent 治理。

## 1. 它解决什么问题
- 本周能力树缺口②："无状态策略引擎 / 确定性 guardrail 对比（Aigis 或 MS AGT）"——多数方案（Aigis/Guardian/AI Protector/AgentGuard 等）为**单一品类**（防火墙或 guardrail），策略引擎+guardrail+协议标准一体化的开源框架稀缺
- agent-aegis 试图以**一个入口**（`aegis.init()`）提供：运行时 guardrails（PII、注入）+ Policy engine（YAML 规则、审批门）+ 开放标准（AGEF/AGP），降低"拼装多工具"的治理成本

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（PyPI）**：`agent-aegis 0.4.0`，2026-10-15 更新，开源 ["https://pypi.org/project/agent-aegis/0.4.0/"]
- **FACT（能力面）**：三大支柱——Pillar 1 Runtime guardrails（PII/注入）、Pillar 2 Policy Engine（声明式 YAML 规则 + 完整治理 pipeline + approval gates）、Pillar 3 Open standards（AGEF/AGP 开放格式）
- **B 级**：有 PyPI 包与活跃更新时间戳，但**无第三方验证/社区规模证据**（星标、采用者、评测数据未知）；"AGEF/AGP 开放标准"为厂商自述，未证实质采纳
- **与已覆盖对象不重复**：agent-firewall 品类卡（Aigis/ClawKeeper/AgentGuard/Pipelock/MS AGT/Proof-of-Guardrail/Falcon Guardian/OWASP Agent Memory Guard 等）为既有对象，agent-aegis 为新出现的一体化框架；与 Aigis（确定性防火墙）最接近但多了策略引擎+协议支柱

## 3. 与我的连接
- **连接的项目**：
  - TeamMind（Java 多 Agent 运行时）：YAML 策略引擎 + approval gates 模式可对照 TeamMind 权限模型；AGEF/AGP 若成标准则影响多 agent 策略互通
  - silver-shield（反诈骗判定）：PII/注入 guardrails 可作为判定管线前置过滤
  - 引擎 evaluation 层：确定性 guardrail 的落地选项之一
- **连接的知识点**：能力树 **C2 无状态策略引擎**（YAML/OPA/Cedar <0.1ms → agent-aegis 为 YAML 线候选）；**D1 确定性 guardrail**（无 LLM 判定线候选）——与周五验证计划②（确定性 Guardrail/策略引擎对比：Aigis 或 MS AGT）形成**第三候选**
- **潜在收益**：周五验证对比池扩展（Aigis / MS AGT / agent-aegis 三选对比）；若其 AGEF/AGP 开放标准有实质证据，可升级为 A 级观察

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | PyPI ["https://pypi.org/project/agent-aegis/0.4.0/"]（0.4.0，2026-10-15） |
| 证据等级 | FACT（PyPI 包+更新时间戳）；AGEF/AGP 标准为厂商自述（DESIGN） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① pip install agent-aegis 跑 `aegis.init()` 最小 demo（guardrails + YAML 策略 + approval gate）；② 对照 Aigis/MS AGT 做确定性判定对比；③ 核 AGEF/AGP 是否有独立文档/采用证据 |
| 预期完成时间 | 2026-10-23（周五验证日，并入 guardrail-策略引擎对比） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
