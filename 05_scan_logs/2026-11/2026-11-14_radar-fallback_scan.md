# Personal Tech Radar 兜底扫描日志 · 2026-11-14（周六）

> 定位：一周一域之外的安全网，只捕获 **S/A 级重大突发事件**。当前深耕领域 = **Memory（11-09 起）**，Memory 侧增量由深耕任务负责，本日志不重复。
> 动作规模：3 路 `general_search` + 1 次 `web_fetch` 全文 + 全库 grep 去重。**未新建候选卡、未改 06 index / connections / 能力树。**

## 检索与判定

| # | 对象 | 事实 | 判定 |
|---|---|---|---|
| 1 | Claude Code 邮箱外发（36氪 11-09 / HN 11-05） | 已在「事件日 17」并入 `[cand]agentic-attack-2026.md` | **去重，不写** |
| 2 | NEAR AI SGLang RCE（11-09 报告） | 事件日 16 已记（Cybernoz / Aviatrix / Daily Security Review 为同源转述） | **去重，不写** |
| 3 | Operation Snowball（Malbear Labs 11-08） | 事件日 15 已记（cybersecurityweekly 11-11 为同源转述） | **去重，不写** |
| 4 | MCP 规范 | 仍为 **2026-07-28**；`modelcontextprotocol.io` changelog 最后更新 11-13 但内容未变（stateless core / Extensions / Tasks / Roots-Sampling-Logging 弃用） | **无变更** |
| 5 | Microsoft Agent Framework「Migrate to MCP 2.x」文档（11-03 / 11-11 更新） | MCP SDK 2.x 客户端生命周期迁移、`extra_run_args` → `unsafe_extra_run_args` 重命名、AG-UI endpoint、A2A run-context 转发 allowlist | **B 级版本增量**：06 index 已记「MAF 1.23.0 MCP 2.x 适配（普通增量）」，属已知对象执行确认，不建卡 |
| 6 | Anthropic **Claude Duet**（research preview，常驻 agent + 高影响动作前请求批准）+ Claude Sheets / Whiteboards / Data + Message Threads public beta（500K~1M token 请求 TTFT 降约 35%、空闲 5 分钟过期） | 与「只做聊天机器人→常驻可委派 agent」的路线转向一致；**审批门设计**与 CoreBreak「伪造 HITL 审批事件」正好互为正面/反面样本 | **Potentially Relevant（观察，不建卡）**：产品发布而非协议/框架变革；一手为 AI 自动撰写、无署名人类编辑的聚合站（wiretensors.ai），来源不足以支撑 S/A 卡 |
| 7 | Google **Gemini 4 Carbon** GA + **agent swarms** 预览（多 agent 并行编排）+ Decision 1 分类 API（$0.10/百万输入 token） | 「agent swarms」是编排方向的信号，但仍是 preview + 产品公告 | **Potentially Relevant（观察，不建卡）**：同第 6 条，来源同为一篇 AI 聚合稿，无一手公告 |
| 8 | 其余 | IBM Nighthawk r3 520 qubits、Gemini 智能眼镜 $395 | **领域外/非 agent 工程对象，剔除** |

## 为什么不写卡
- 第 6/7 条虽方向重要，但①属**产品/模型发布**，与既有先例（Cohere North 2、GPT-6.1 Terra、Alibaba AgentScope 1.0 均判 B 不建卡）一致；②来源为 AI 聚合稿（页面自述"Researched and drafted with AI… not individually reviewed by a named human editor"），**未取得任何一手公告**，不足以支撑 S/A 级候选卡的事实基础。
- 若后续出现一手公告或独立评测（尤其是 Duet 审批门的实现细节、swarms 的调度语义），再考虑升 A；当前只作**观察项**留给 Computer Use / Browser 或 Harness 回访时确认。

## 结论
**Potentially Relevant（0 新建卡 / 0 索引变更）**
