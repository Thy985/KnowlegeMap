# 扫描日志
> 日期：2026-10-08 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 36 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index + Star 基准去重
## 1. 扫描范围
- Re-ground：git 状态（152b3a3 已推送，干净）+ 06_expansion_index 去重基准（38 对象）+ 00_starred_reference.md（35 star）
- 今日聚焦三线：
  1. **Local Edge LLM**（local-edge-llm 卡）——10-02 后 6 天（月度轮）
  2. **Agentic Benchmarks**（agentic-benchmarks 卡）——10-02 后 6 天
  3. **OTel GenAI**（otel-genai 卡）——10-03 后 5 天
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **Google EmbeddingGemma 2**（10-06：740M 多模态 embedding，量化 191MB/567MB） | 本地检索基础设施产品化——Tafcm 本地 RAG 选型 | Zeniteq | → local-edge-llm 卡 |
| 2 | **Kolibri 1**（Aleph Alpha 10-03：78B 总参 MoE 3.46B/token） | 大模型 MoE 本地新档 | ModelFit | → local-edge-llm 卡 |
| 3 | **NVIDIA E2B/E4B + 26B/31B**（Jetson Nano 离线近零延迟 + 代理级） | 边缘模型家族化 | NVIDIA | → local-edge-llm 卡 |
| 4 | **Qwen3.8 27B open-weight 预告 + 小型 MoE 登顶**（Apsara 09-22） | 国产开放档预告 | LLMCheck | → local-edge-llm 卡 |
| 5 | GLM-Edge/Liquid/RTX Spark 十月/Prompt API | **已覆盖**（10-02） | — | 去重 |
| 6 | **ThinkingBox（MS+HF 10-03）**：数据库状态+副作用评分，67.24% 失败无报错、79.9% 失败源于工具处理 | **pass@1 幻觉终结——评测范式转折** | AI Breaking Wire/OpenAI Master | → agentic-benchmarks 卡 |
| 7 | **Agents' Last Exam 榜单**（GPT-6 Astra 59.3%/Qwen3.8 Max 52.4%） | 前端 vs 开放差距量化 | BenchLM | → agentic-benchmarks 卡 |
| 8 | OctoBench/HANDBOOK.md/KAMI/SWE-bench 批判 | **已覆盖**（10-02） | — | 去重 |
| 9 | **Google Cloud Agent Observability**（10-07：Gemini Enterprise/Agent Gateway/Model Armor） | 第三家云厂把 agent 观测做平台能力 | Google Cloud | → otel-genai 卡 |
| 10 | **阿里云 GenAI Utils**（09-21：手动 instrumentation + ARMS） | 国内云厂进 GenAI 观测 | 阿里云 | → otel-genai 卡 |
| 11 | **OTel GenAI 2.0 Run Tree**（span 映射执行树） | 约定 2.0 从打点升级为结构建模 | DEV | → otel-genai 卡 |
| 12 | Cloudflare/IETF/CloudWatch Omni | **已覆盖**（09-27/10-03） | — | 去重 |
## 3. 筛选结果
- **无新卡**（3 条既有卡增量）
- 增量更新 3 条：local-edge-llm（EmbeddingGemma 2 + Kolibri + NVIDIA 边缘家族 + Qwen3.8 预告）、agentic-benchmarks（ThinkingBox 范式转折 + Agents' Last Exam）、otel-genai（Google/阿里云厂 + OTel 2.0 Run Tree）
- 候选卡维持 38 张
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-10-08 雷达扫描段（3 条 Changed 增量）
- `_INDEX.md`：日志索引补 10-08 行（candidates 保持 38）
- `04_connections/README.md`：无新卡，连接关系不变
## 5. 下一步
- 验证优先级更新：**silver-shield Harness 引入"执行状态断言层"**（ThinkingBox——final answer 不可信，67% 静默失败）＞ **Tafcm 本地 embedding 选型 EmbeddingGemma 2**（191MB 量化）＞ **工具契约测试优先级再升**（79.9% 失败源于工具处理）
- 下次扫描聚焦：a2a/mcp（协议线，10-04 后 4 天）、agentic-graphrag、agent-harness
