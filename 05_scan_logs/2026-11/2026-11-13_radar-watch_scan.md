# Personal Tech Radar 深耕扫描日志 · 2026-11-13（00:30，Memory 周 Day5 验证日）

> 分工：周五 = 对 2-3 个高价值候选做实际验证/对比，拿证据。本日不追新资讯。

## 验证对象与证据

### 1) Mem0 OSS 本地端到端（`mem0ai 2.2.1`）
环境：`python3 -m venv` + `pip install mem0ai`；qdrant 本地路径 `path=/tmp/verify_mem/qd`；**不调用任何云服务**——用自写 FakeLLM（返回固定 JSON `{"memory":[{"text":...}]}`）与 FakeEmbedder（8 维确定性向量）替换 `Memory.llm` / `Memory.embedding_model`；`OPENAI_API_KEY=sk-dummy` 仅为绕过构造期 client 校验。

结果：
- `add("我偏好本地文件记忆，Tafcm 用 Markdown 不用向量库", user_id="u1")` → 返回 `{"results": []}`
- `get_all(filters={"user_id":"u1"})` → **2 条**（"用户偏好本地 SQLite 记忆，不上云"、"Tafcm 使用 Markdown 文件作为记忆层"）
- `search("Tafcm 记忆 存储方式", filters={"user_id":"u1"}, top_k=3)` → 2 条，top score **0.8374357893586238**

代码级事实：
- sync/async `add` 均走 **单次 `ADDITIVE_EXTRACTION_PROMPT`**（Phase 1 列既有记忆 → Phase 2 单次抽取 → Phase 3 批量 embed → Phase 4/5 逐条处理 + md5 hash 去重 → Phase 6 批量落库 → Phase 7 实体链接）。
- `Requires-Dist` **无 neo4j / neptune / kuzu / AGE**；`deps` 仅 httpx/openai/posthog/protobuf/pydantic/pytz/qdrant-client/sqlalchemy → 图存储确已移除。
- `expiration_date`（YYYY-MM-DD，过期默认隐藏、`show_expired` 可看）已进 OSS `add`；`timestamp` 标注 "Platform-only temporal parameter. Not supported in OSS"。
- **回执不一致**：docstring 声称返回 `{"results":[{"id","memory","event":"ADD"}]}`，实测 `{"results": []}`；写入确实发生（get_all 可读）。→ SDK 口径批判第四类证据（分数/写入回执均与平台口径不同）。
- 默认 `MemoryConfig.version='v1.1'`、vector store 默认 qdrant `path=/tmp/qdrant`、默认 llm/embedder 均为 openai；无 key 时构造函数即抛 `Missing credentials`。

### 2) EvolveLab 源码核对（`github.com/bingreeky/MemEvolve`，ICML'26）
- 仓库结构：`Flash-Searcher-main/{MemEvolve,EvolveLab,mini-swe-agent,FlashOAgents,model_eval}`。
- `EvolveLab/providers/` 共 **13 个 provider**：agent_kb、agent_workflow、cerebra_fusion、dilu、dynamic_cheatsheet、evolver、expel、generative、lightweight、memp、mobilee、skillweaver、voyager。
- `memory_types.py` 的 `PROVIDER_MAPPING` 显式登记 13 项 → 即论文口径 **12 基线 + Evolver 自身**。
- 统一接口：`BaseMemoryProvider.provide_memory(MemoryRequest) -> MemoryResponse` / `take_in_memory(TrajectoryData) -> (bool, str)`；数据结构 `MemoryRequest(query, context, status, additional_params)`、`MemoryItem`。
- 复现门槛：`requirements.txt` + `.env` API keys（`ANALYSIS_MODEL`/`GENERATION_MODEL`）+ GAIA(Feb 2025)/WebWalkerQA(subset 170)/xBench(DeepSearch) 数据集 → **本环境未跑**，判定为结构验证。

### 3) Zep Community Edition 事实修正
- `getzep.com/blog/announcing-zep-community-edition/`：**Daniel Chalef，Sep 26, 2024**，"open-sourced today, the first Zep product powered by a Knowledge Graph"；文内说明 CE runs Graphiti under the hood。
- `help.getzep.com/v3/faq`：**"Zep Community Edition ... is deprecated and no longer supported."** 替代 = Zep Cloud / Graphiti / BYOC。
- `getzep.com/blog/tag/context-graphs/`：10-29 文章为《How Zep Context Graphs keep two timelines for every fact》，非 CE 开源公告。
- `github.com/getzep/zep`（clone 核对）：README 自述 "This repository is **not** Zep's product or service"，内容为 examples/integrations/benchmarks/ingestion/ontology；**无 `legacy/` 目录**，指向 Zep Cloud + Graphiti。
- 结论：Day2「Zep CE 开源（2026-10-29）」为**误读 tag 页时间戳**，判定作废，降 B 观察。

## 判定
| 对象 | 等级 | 判定 |
|---|---|---|
| Mem0 OSS 本地可跑 + 回执不一致 | A | 已回写候选卡 Day5 段（不新建卡） |
| EvolveLab 12+1 providers 对照台 | A | 已回写；结构验证，未跑行为 |
| Zep CE 开源 | **作废** | 降 B；能力树锚点表待周六修正 |
| Letta 三级记忆 / Zep 本地服务 | — | 未执行（时间 / 前提消失），如实挂账 |

## 落位
- `[cand]agent-memory-2026.md` Day5 段 + Day2 Zep 行就地修正。
- `07_radar_watch/current_focus.md` 周五勾选 + 周六回灌待办 5 项。
- 06 index Day5 段、`_INDEX.md` 🔁 行、本日志。
- 未新建卡；未改 connections（留周六）；未改能力树（留周六统一回灌）。

## 结论
**Changed**
