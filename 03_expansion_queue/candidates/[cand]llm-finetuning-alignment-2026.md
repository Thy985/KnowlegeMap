# 候选证据卡 · [cand] LLM Fine-tuning 对齐新范式（DPO/ORPO/KTO + Agentic SLM）

> 状态：`[cand]` ｜ 分类：Fine-tuning/对齐（B14） ｜ 发现：2026-09-01 ｜ 等级：**B**

## 一句话定位
2024-2026 对齐范式已定：RLHF 基本退役，DPO/ORPO/KTO 成为主流；出现面向 Agent 的"工具调用对齐"工具链（Agentic SLM Toolkit），并与边缘小模型（TinyLLM）交汇。

## 1. 它是什么 / 解决什么问题
- **DPO/ORPO/KTO**：免奖励模型/免 PPO 的偏好对齐（Bradley-Terry 分类式 loss）；ORPO 省 SFT 阶段；KTO 无需成对数据["https://localaimaster.com/blog/dpo-orpo-kto-guide"]
- **Agentic SLM Toolkit**：自动生成 ReAct 工具调用轨迹 + DPO 偏好对，**惩罚工具幻觉与 malformed JSON**，QLoRA 4-bit + 本地 ReAct executor——专为"让 SLM 正确用工具"设计["https://github.com/RavaniRoshan/llm-finetuning-toolkit"]
- **TinyLLM**：边缘 SLM agent 的评测与优化，DPO 是 SLM agent 对齐核心手段["https://arxiv.org/html/2511.22138v1/"]
- 实践配方：SFT 1-3 epochs、DPO 1 epoch、混 10-30% 通用数据防遗忘、GRPO 用于可验证推理任务、vLLM 热切换 adapter["https://github.com/bidyashish/ai-basics/blob/main/20-fine-tuning-recipes.md"]

## 2. 与我的知识/项目关系
- **ML 实验方法论**（weather-recognition 母矿）可外推到 LLM 微调层：训练配方/防遗忘/评估纪律一致
- **silver-shield**：对诈骗风险模型可做对齐/鲁棒性实验
- **Agentic SLM Toolkit** 与我的 Agent 栈直接相关：工具调用对齐是"让 Agent 可信"的底层
- 边缘 SLM（TinyLLM）与本地/边缘卡交叉

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（arXiv + GitHub + 实践指南） |
| 来源 | https://github.com/RavaniRoshan/llm-finetuning-toolkit ｜ https://localaimaster.com/blog/dpo-orpo-kto-guide ｜ https://arxiv.org/html/2511.22138v1/ |
| 验证方式 | 评估性试跑：用一个小 SLM + 工具调用数据跑一次 DPO 最小实验（本地 GPU 可行时） |
| 预期 | 2026-10/11 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
