# 扫描日志
> 日期：2026-09-29 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 27 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index + Star 基准去重
## 1. 扫描范围
- Re-ground：git 状态（5d2cc18 已推送，干净）+ 06_expansion_index 去重基准（37 对象）+ 00_starred_reference.md（35 star）
- 今日聚焦三线：
  1. **Agent Memory**（agent-memory S 卡）——09-25 后 4 天
  2. **Computer/Browser Use**（computer-browser-use A 卡）——09-25 后 4 天
  3. **MCP**（mcp S 卡）——09-24 后 5 天
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **Synapse**（arXiv 2601.02744：扩散激活统一 episodic-semantic 记忆） | "图动力学替代向量相似度"——记忆研究新范式 | arXiv | → agent-memory 卡 |
| 2 | **REMem**（ICLR 2026：Hybrid Memory Graph + 跨事件时间推理） | episodic 推理结构化 | PaperNotes | → agent-memory 卡 |
| 3 | **HeLa-Mem**（Hebbian 学习+联想记忆双层级） | 生物启发联想巩固 | Moonlight | → agent-memory 卡 |
| 4 | **SEEM**（arXiv 2601.06411：Episodic Event Frames + Reverse Provenance Expansion） | 事件帧+溯源反推——与 EnSIMem 证据线同向 | arXiv | → agent-memory 卡 |
| 5 | **Jev-Mem**（arXiv 2609.23986：System-One 控制面记忆） | 快慢双系统分工落地记忆 | alphaXiv | → agent-memory 卡 |
| 6 | **Dual-Process Memory 实证**（arXiv 2605.17625：15k 消息×6 LLM） | 双过程解耦跨模型验证 | arXiv | → agent-memory 卡 |
| 7 | **Anthropic Computer Use/Skills/Files APIs GA + 原生 Browser Use**（09-18） | browser use 企业 GA（full SLA） | aicoder | → computer-browser-use 卡 |
| 8 | **toolsets 上 Google Cloud**（09-28） | 跨云可用性确认 | Claude release notes | → computer-browser-use 卡 |
| 9 | **Vercel Agent Browser**（09-24：零配置交互网页） | 免 driver 浏览器交互产品化 | ai-damn | → computer-browser-use 卡 |
| 10 | **Tencent BrowserSkill**（06-2026 开源 MIT） | 国内大厂开源浏览器 agent 桥 | aiwiki | → computer-browser-use 卡 |
| 11 | **AWS stateless MCP 部署实践**（InfoQ 09-25） | stateless 企业落地参考架构 | InfoQ/AWS | → mcp 卡 |
| 12 | **MCP 安全挑战量化**（50%/41% 组织列为首要挑战） | 安全成本 MCP 第一障碍 | Pulumi/Stacklok | → mcp 卡 |
| 13 | EnSIMem/Letta/Zep/Mem0、Claude for Chrome、Registry 破万/SEP-2640 | **已覆盖**（09-21~09-25 轮） | — | 去重 |
## 3. 筛选结果
- **无新卡**（三条均为既有卡增量）
- 增量更新 3 条：agent-memory（5 论文大增量）、computer-browser-use（GA+零配置）、mcp（stateless 落地+安全量化）
- 候选卡维持 37 张
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-29 雷达扫描段（无新对象，3 条 Changed 增量）
- `_INDEX.md`：日志索引补 09-29 行（candidates 保持 37）
- `04_connections/README.md`：无新卡，连接关系不变
## 5. 下一步
- 验证优先级更新：**记忆架构三主线（联想激活/双过程/事件溯源）纳入 Tafcm 本地记忆设计输入**＞ browser use 官方 API 对齐（E2E-CLI 浏览器自动化基线）＞ **MCP server 信任评估独立检测项**（silver-shield）
- 下次扫描聚焦：Agent Harness（Harness 自演化）、Multi-Agent/OpenClaw（两周一版节奏）、Agent Formal Verification
