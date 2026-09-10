# 候选证据卡 · [cand] Agent 防火墙 / 运行时防御品类（Aigis + ClawKeeper + AgentGuard + Pipelock）
> 状态：`[cand]` ｜ 分类：AI 安全防御侧 / Agent 运行时治理（G1） ｜ 发现：2026-09-11（雷达 #10） ｜ 等级：**A**
## 一句话定位
2026-09 一周内"Agent 防火墙/运行时防御"品类密集涌现：**Aigis**（确定性零依赖 Python 防火墙：MCP rug-pull/memory poisoning/indirect injection/exfil 检测 + 44 合规模板）、智源 **ClawKeeper v1.0**（Skill/Plugin/Watcher 三位一体，面向 OpenClaw 全生命周期）、**AgentGuard**（Prompt/Tool/Command 三层运行时防火墙）、**Pipelock v3.5**（扫描 HTTP/MCP/A2A/WebSocket 流量 + 可验证签名 receipts）——Agent 安全从"检测工具"走向"运行时治理层"。
## 1. 它是什么 / 解决什么问题
- 痛点：Agent 工具调用/文件写入/代码执行/agent 互信缺运行时监管——一次 prompt injection 即数据外泄；chatbot 时代的"文本过滤"已不够["https://github.com/gaebalai/aigis-kr"]
- **Aigis（pyaigis v1.1.11，Apache-2.0，零运行时依赖）**：每次工具调用的确定性 guardrail + 防篡改审计日志 + 生成的 IT 审批包；覆盖 MCP rug-pull、记忆投毒、间接注入、外泄通道；内置**事件生命周期管理**（威胁自动建 incident + 全时间线）；44 合规模板（US/CN/JP/EU）["https://github.com/gaebalai/aigis-kr"]["https://pypi.org/project/pyaigis/"]
- **ClawKeeper v1.0（智源 + 北邮 + 信通院，2026-09）**：面向 OpenClaw 的实时安全框架，**Skill/Plugin/Watcher 三位一体**防御架构，覆盖 agent 全生命周期，适配局域网 agent 集群监控["https://blog.csdn.net/FENGQIYUNRAN/article/details/161616195"]
- **AgentGuard（0xrem）**：桌面/开发机 AI Agent 运行时防火墙——Prompt Guard（输入/检索/工具参数：warn/mask/block/ask）+ Tool Guard（文件/浏览器/HTTP/DB/邮件：allow/deny/ask/sandbox）+ Command Guard（shell：suspend/block/confirm/kill）["https://github.com/0xrem/agentguard"]
- **Pipelock v3.5.0（2026-09-01）**：开源 AI agent 防火墙，扫描 HTTP/MCP/A2A/WebSocket 流量防外泄/SSRF/prompt injection，**可验证签名 action receipts** 供审计["https://kitploit.com/en/posts/github-luckypipewrench-pipelock-v350"]
- 同线：Agent Guard（Avveerayy，运行时治理层）、NeuralGuard（FastAPI 中间件）、LlamaFirewall（arXiv 2505.03574，open source guardrail 框架）["https://github.com/Aveerayy/agent-guard"]["https://arxiv.org/pdf/2505.03574"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-11）**：Aigis GitHub/PyPI ✅、ClawKeeper 多源报道 ✅、AgentGuard GitHub ✅、Pipelock release ✅
- 时间密集：09-01 Pipelock → 09-02 AgentGuard → 09-04 ClawKeeper/Aigis PyPI → 09-05 Aigis 更新——一周内至少 4 个独立项目发布，品类成形信号
- 与 Agentic Attack（09-09 S 级）同一安全叙事的两面：攻击链 agent 化 → 防御必须运行时化
## 3. 与我的连接
- **连接的项目**：**silver-shield**（防诈骗/风险检测——Aigis 的确定性 guardrail + 事件生命周期可直接借鉴）；**EP-002**（Permission Is Security Boundary——AgentGuard 的 Tool/Command Guard 正是"权限边界"的工程实现）；**campus_order**（OpenClaw——ClawKeeper 直接针对 OpenClaw）；**TeamMind**（工具调用治理层参考）；dsh-pentest（可攻击测试这些防火墙）
- **连接的知识点**：AI 安全攻防（G1）、Agent 运行时治理、Skill 供应链安全（S 级卡同线）
- **潜在收益**：silver-shield 可评估引入 Aigis 类确定性 guardrail 作为防线；为 TeamMind 提供"运行时防火墙"选型池
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/gaebalai/aigis-kr ｜ https://blog.csdn.net/FENGQIYUNRAN/article/details/161616195 ｜ https://github.com/0xrem/agentguard ｜ https://kitploit.com/en/posts/github-luckypipewrench-pipelock-v350 |
| 证据等级 | **FACT（GitHub/PyPI + 多源报道核验通过）** |
| 验证方式 | 装 Aigis 对一个 agent 工具调用链跑确定性 guardrail → 对照 silver-shield 防线设计 → 评估 AgentGuard 三层模型是否入 TeamMind 工具治理 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
