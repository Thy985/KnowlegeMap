# 候选对象证据卡 · ToFu（LLM–Orchestrator–Tool 信任边界的工具感知 Fuzzing 框架）

> 状态：`[cand]` ｜ 关联方向：安全（MCP/Agent 工具信任边界，非 Evaluation 深耕；兜底捕获）｜ 日期：2026-10-15（兜底 06:00 安全网）

## 一句话定位
arXiv 2610.13651（2026-10-09，Penn State / Université Montpellier / Dartmouth）开源的 **ToFu**：工具感知（tool-aware）fuzzing 框架，从 tool metadata + CWE 指导的 sanitizer 语料自动推导语义安全检查；实测 273 个开源 MCP server / 3,405 个工具，发现 **253 个已验证漏洞（343 个工具 / 118 个 MCP server）**。

## 1. 它解决什么问题
- **schema-valid ≠ safe**：LLM 生成的工具调用格式正确，不代表参数安全或被授权；orchestrator 把"格式正确"误当作"可执行"
- **依赖/SCA 扫描器漏检 tool argument 到达面**：传统 crash-based fuzzing 抓不到"契约违反但不崩溃"（如声称只访问 workspace 却接受路径穿越读外部文件）
- **tool description 与实现不一致**：工具声明的限制在代码里不成立；prompt 过滤和模型行为改进无法替代执行层（文件/网络/命令）的安全检查

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：arXiv 2610.13651，2026-10-09 发布；GBHackers 10-13 报道
- **大规模实证**：273 MCP servers / 3,405 tools / 253 verified bugs（对应 CWE 弱点类）
- **"Repeat-After-Me"攻击跨 6 个编排框架复现**：LangGraph、Microsoft MAF、Google ADK 2.0、AutoGen、AWS Strands、CrewAI
- **方法论**：74 个语义感知 sanitizer（参数语义→CWE 属性）+ LLM 解释 metadata/生成 seed，但**漏洞判定不由 LLM 做**（可执行 sanitizer 评估运行时观察）；Atheris coverage-guided fuzzing；对 opaque tool 用 outcome check
- **与 Protocol Pivoting（10-13 卡）互补**：Pivoting 揭示跨协议信任攻击范式（MCP tool output→A2A 指令）；ToFu 提供大规模系统化**审计/测试框架**——一个是攻击路径，一个是审计能力，同属"agent 信任边界"结构性问题
- **同谱系背景**：ChainFuzzer（arXiv 2603.12614，工作流级多工具漏洞，3 月）、OrchJail（2605.07414，5 月）

## 3. 与我的连接
- **连接的项目**：
  - **dsh-pentest / silver-shield**：工具参数安全审计、MCP server 渗透测试可直接使用 ToFu 思路
  - **引擎 security-assessment 能力树**：ToFu 是"工具层契约违反测试"的可执行实现，补 Security 能力树
  - **Tafcm / TeamMind**：本地工具/多 agent 工具调用的执行层强制检查（把 schema-valid 参数当不可信输入）
- **连接的知识点**：架构原则（agent 不能成为自身安全权威，执行层强制）；与 MXC（OS 层隔离）、Protocol Pivoting（跨协议信任）构成"隔离+信任+审计"三角
- **潜在收益**：① 用 ToFu 的 74 sanitizer 方法论审计自建工具描述与实现的一致性；② 周五/安全周验证时跑通 demo，作为 MCP server 安全测试的标准工具

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/abs/2610.13651 ｜ 报道：https://gbhackers.com/researchers-discover-253-security-vulnerabilities/ |
| 证据等级 | FACT（arXiv 一手 + 安全媒体） |
| 验证方式 | ① 精读论文确认 74 sanitizer / Repeat-After-Me / 运行时 tracer 机制；② 检查代码仓库开源状态并尝试对 1-2 个自建/第三方 MCP server 跑通；③ 与 Protocol Pivoting 卡做交叉对照 |
| 预期完成时间 | 留待 MCP 安全/治理周（或 Harness 治理周）验证 |

## 5. 验证结果
<!-- 验证后回填 -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
