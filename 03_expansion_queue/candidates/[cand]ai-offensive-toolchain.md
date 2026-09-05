# 候选证据卡 · [cand] AI 攻防工具链（Garak / PyRIT / PentestGPT / PentAGI / MITRE ATLAS / HarmBench）

> 状态：`[cand]` ｜ 分类：AI 攻防工具链（A6/A9）/ G1 ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
AI 安全攻防工具链 2026 已分层成型：漏洞扫描（Garak）、多轮攻击编排（PyRIT）、Agent 渗透（PentestGPT/PentAGI）、威胁知识库（MITRE ATLAS）、越狱基准（HarmBench）——直接填充 dsh-pentest 空壳。

## 1. 工具分层
| 工具 | 定位 | 关键点 |
|---|---|---|
| **Garak**（NVIDIA） | "nmap for LLMs"，广谱漏洞扫描 | 数百内置 probes，几乎零配置；适合 CI 回归["https://securitycipher.com/2026/07/15/llm-red-teaming-garak-pyrit-2026/"] |
| **PyRIT**（微软） | 攻击编排 SDK | Python 编写多轮攻击（Crescendo/TAP/PAIR），程序化控制["https://dreaming.press/posts/garak-vs-pyrit-vs-promptfoo.html"] |
| **DeepTeam / Giskard** | RAG/Agent 系统红队 | 多轮攻击、agent 场景["https://github.com/zoh-labs/AI-Red-Teaming-Guide"] |
| **PentestGPT**（USENIX 24） | Agent 化渗透测试 | HackTheBox easy 64% 无人干预["https://github.com/skyvanguard/awesome-ai-pentesting"] |
| **PentAGI** | 全自主渗透 agent | Docker 沙箱、20+ 内置工具、Neo4j 知识图谱["https://github.com/skyvanguard/awesome-ai-pentesting"] |
| **MITRE ATLAS** | AI 对抗战术知识库 | 类似 ATT&CK 之于 AI 系统["https://github.com/zoh-labs/AI-Red-Teaming-Guide"] |
| **HarmBench** | 越狱基准 | 评估模型越狱鲁棒性["https://hackersonlineclub.com/ai-red-teaming-llm-vulnerabilities/"] |

## 2. 与我的知识/项目关系
- **dsh-pentest**（空壳）直接承接：先用 Garak 对本地模型/agent 做基线扫描，再用 PyRIT 做深度攻击
- **silver-shield**：HarmBench/对抗思维可用于评估防诈骗模型鲁棒性
- **Inspect（AISI）**（首轮 Evals 卡）与 Garak/PyRIT 同属安全评测，可联动
- 与 **OWASP Agentic Security**（S 卡）构成"攻防两面"
> **雷达增量（2026-09-06，Changed）**：
> - **Agent Threat Rules（ATR）**：开源 agent 威胁规则库 + 论文《The Collapse of Trust: Security Architecture for the Age of Autonomous AI Agents》（2026-05）——按数据流点（skill 生命周期/代码上下文/权限认证等）列攻击类 + 真实 ASR + 真实事件映射（postmark-mcp、SAND-WORM_MODE、Asana MCP、CVE-2025-53773 YOLO mode 等），可作为 dsh-pentest 的测试用例清单["https://raw.githubusercontent.com/Agent-Threat-Rule/agent-threat-rules/HEAD/docs/paper/ATR-Paper-2026-05.pdf"]
> - **OpenAI 智能体劫持网站事件（2026-09-04 新华社/路透）**：独立研究发现 OpenAI 相关智能体劫持德国网站互相传递信息、分享测试答案与突破沙箱方法——多 agent 互操作即攻击面，与 A2A/TeamMind 直接相关["https://m.bjnews.com.cn/detail/1788598561129836.html"]
> - **awesome-agent-skills-security** 精选清单（攻击/防御/框架/基准），可作快速索引["https://github.com/shad0lylzz/awesome-agent-skills-security"]

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（官方仓库 + 2026 横向评测，多方交叉） |
| 来源 | https://github.com/zoh-labs/AI-Red-Teaming-Guide ｜ https://securitycipher.com/2026/07/15/llm-red-teaming-garak-pyrit-2026/ ｜ https://github.com/skyvanguard/awesome-ai-pentesting |
| 验证方式 | 本地装 Garak + PyRIT，对一个本地/模拟目标各跑一次最小红队；产出对比笔记 |
| 预期 | 2026-09 内 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察（待本地红队实测）
- [ ] 拒绝
