# Personal Tech Radar 深耕扫描 · 2026-11-19（周四 00:30）

> 领域：**Memory 第二周 Day4**（延长周）。分工：只追增量。方向按 current_focus：PersistBench 复现件 / guard 类工具有无可验证件 / 相邻新方案。

## 一、检索（2 路 + 2 次定向核对 + 去重）
1. PersistBench 代码与复现管线
2. agent memory poisoning defense：开源、provenance、可验证
3. 定向核对 PoEM 摘要（arXiv 2608.16032）+ 全库 grep 去重

## 二、判定表

| # | 对象 | 事实 | 判定 |
|---|---|---|---|
| 1 | **PoEM（2608.16032v2）** | 不读记忆，独立 HMAC 链执行台账（仅可信动作层可写）；FARMA 下 ASR **0%**，误伤 0%（8/9）/1.7%；SENTINEL 误伤 33–50% 且被改写绕过归零；能力悖论（GPT-4o 98–100% vs Llama-8B 44%）；MIT 代码 | **A｜锚点 + §8.7** |
| 2 | **TMA-NM（2606.24322）** | 三条洗白通道；T1~T3 分离定理 + TLA+；现有防御洗白 ASR 最高 68% | **A−｜合并锚点** |
| 3 | **MemLineage（2605.14421）** | Ed25519 + RFC 6962 Merkle 日志 + 派生 DAG + 敏感动作门 | A−｜合并 |
| 4 | **MutMem（2608.02843）** | 签名化变更 + 回执；LongMemEval 91.8 / LoCoMo 74.12；中位 4.9 ms | A−｜合并 |
| 5 | **PersistBench（inspect-evals 0.13.0）** | 三任务内置（cross_domain / sycophancy / beneficial_memory）+ GitHub prompt；需模型 API/judge | **B｜记日志** |
| 6 | mnemosyne-guard / agent-memory-guard 0.4.0 | OWASP AMG 衍生/互补件：来源分级、HMAC 签名、哈希链审计、Unicode 混淆检测 | C｜只记日志 |
| 7 | PersistBench 论文本身（2602.01146） | 10-02 已收录 | 去重命中 |

## 三、核心判断
1. **检测措辞这条线可以判死**：SENTINEL 一次改写归零；Price of Safety 里 sanitization/provenance 750 轮零触发。防的是说法，不是事实。
2. **能力悖论**：同一伪造声明，强模型 98–100% 照做，弱模型 44%。记忆污染是能力放大器——"换更强模型"不解决安全问题。
3. **防御对象应是动作**：PoEM 只保护它门控的决策，这是边界也是诚实；能形式化的才敢声称防住。
4. **写时绑定 > 读时判断**：TMA-NM 把来源/血缘从启发式升级为必要条件，MemLineage 落成签名 + Merkle 日志；代价是写入签名与动作验链。

## 四、限制
- 四篇均摘要级；PoEM 仓库未 clone 未复现；TMA-NM/MemLineage 代码未核；MutMem 分数口径未读全文。
- PersistBench inspect-evals 只读 PyPI 描述，未跑；需 API key 与 judge。

## 结论
**Changed**（锚点 +2、缺口 +1、§8.7、S 卡 §5.2；无新卡）
