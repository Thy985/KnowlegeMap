# 扫描日志
> 日期：2026-09-20 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 18 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：git 状态（6dd241d 已推送，干净）+ 06_expansion_index/README.md 去重基准（36 对象）
- 今日聚焦（未跟进领域三线）：
  1. **Computer/Browser Use**（computer-browser-use A 卡）——09-14 后首次跟进
  2. **MCP 生态**（mcp-2026-07-28-stateless 首轮卡）——长期未跟进
  3. **AI Infra × Agent 推理基础设施**（知识库空白区）——首次系统扫描
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **Anthropic Computer Use/Skills/Files API GA（09-18）** + 新 Browser Use 工具 + 单调用多动作 | computer use 企业级 GA | aicoder / ai-damn | → computer-browser-use 卡增量（Changed） |
| 2 | **Vercel Agent Browser（09-15）** + Browserbase Stagehand 重建（09-09） + **Skyvern 3.0 验证码原生处理** + Gemini Spark 降价（$249→$19） | 基础设施商入场 + 验证码突破 + 产品普及 | ai-damn / releasebot / agenticindex / toolbit | → computer-browser-use 卡增量 |
| 3 | **MCP Roadmap 统一传输**（Streamable HTTP over stdio）+ **SEP-2663 Tasks 扩展**（08-28）+ MCP Apps UI 扩展 + AWS 企业部署指引 | 扩展框架成熟 + 传输统一 | blog.modelcontextprotocol / modelcontextprotocol.io | → mcp 卡增量 |
| 4 | **NVIDIA Dynamo Agentic Inference**（KV-aware 路由三机制 + KV 卸载存储） | **agentic 工作负载推理调度新范式** | NVIDIA docs | → **新卡 agentic-inference-infra-2026（A，37）** |
| 5 | **AWS HyperPod Inference Gateway（09-18，TTFT -82%）** + **prefix-aware routing（09-10，P50 -77%）** + vLLM KV offload + **Unified AI Gateway（arXiv）** + 阿里 TokenWorks | 全栈 agentic-aware 推理基础设施成型 | unite.ai / AWS blog / vllm.ai / arXiv / 阿里云 | → 新卡 |
| 6 | MCP 2026-07-28 规范本身 / GPT-6 Astra computer use / Claude Cowork | **已覆盖**（09-01/09-14 轮） | — | 去重 |
## 3. 筛选结果
- **新建 1 张 A 级卡**：agentic-inference-infra-2026（36→37）——AI Infra×Agent 是知识库明显空白区（G3/G5），且与 Tafcm/TeamMind/dsh 均有直接连接
- 增量更新 2 条：computer-browser-use（6 对象）、mcp（4 对象）
- 无新范式丢弃：AdsPower AI Agent（多账号浏览器自动化，商业产品）、agent-browser.dev v0.37（工具更新）
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-20 雷达扫描段（**1 新对象** + 2 条 Changed 增量）
- `04_connections/README.md`：连接地图加 1 行（agentic-inference-infra-2026）
- `_INDEX.md`：candidates 36→37 张，日志索引补 09-20
## 5. 下一步
- 验证优先级更新：**Tafcm 端边云联合路由设计（新卡验证项）** ＞ campus_order OpenClaw 升级 ＞ Plugin4Shell 威胁建模
- 下次扫描聚焦：Agentic Attack 新事件（事件驱动）、agent-memory 增量、OpenClaw 生态
