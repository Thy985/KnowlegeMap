# 候选证据卡 · [cand] Agentic CLEAR（IBM 自动多层级 Agent 评估框架）
> 状态：`[cand]` ｜ 分类：Agent Evaluation / 评估方法论（G2） ｜ 发现：2026-09-04（雷达 #3） ｜ 等级：**A**
## 一句话定位
IBM Research 开源的自动、动态、易用的 agent 评估框架（arXiv 2605.22608 + Python 包）：在可观测层之上，把 agent trace 按 **system / trace / node 三级粒度**自动评估，无需预定义错误分类学，动态挖掘反复出现的失败模式并生成文本级洞察——正是"Validation 编译器"从手动到自动化的实证样本。
## 1. 它是什么 / 解决什么问题
- 痛点：可观测平台捕获 trace 但缺乏有意义评估；研究驱动的错误分类学是静态的、需大量人工标注、无法适配新领域["https://arxiv.org/pdf/2605.22608"]
- 做法：在 observability 之上运行 judge（step/trace/rubric 三级 J_s/J_t/J_r），生成每步 critique 与打分，聚合为 node 级与 system 级摘要，并用自然语言动态呈现循环失败模式；交互式 dashboard 呈现["https://ibm.github.io/CLEAR/"]
- 实验结果：跨 4 个基准 + 7 种 agent 配置，与人工标注错误对齐，对任务成功有预测信号["https://arxiv.org/pdf/2605.22608"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-04）**：arXiv 2605.22608 ✅、IBM 官方页 ibm.github.io/CLEAR ✅（开源 Python 包，说明"构建于 observability 之上"）、论文作者 Asaf Yehudai / Lilach Eden / Michal Shmueli-Scheuer（IBM Research）✅
- 同线（2026 评估方法论收敛方向）：AgentEval（ACL 2026，把 agent 轨迹建模成评估 DAG、逐节点打分 + 贪心父节点根因追溯 + 21 类失败类目 + CI/CD 集成，production trace 上 failure recall +2.1×）["https://papernotes.org/ACL2026/llm_evaluation/agenteval_dag-structured_step-level_evaluation_for_agentic_workflows_with_error_/"]、Agentic Skills Evaluation（KDD 2026，自动合成真实任务评估 agent skills）["https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/assets/papers/35_A_Framework_for_Evaluating_.pdf"]
- 与我的"Validation 编译器"（Claim→Operationalization→Evidence→Judgment→Done）**直接同构**：judge 多级 + 证据聚合 + 自动判断 = 编译器自动化形态
## 3. 与我的连接
- **连接的项目**：**silver-shield**（Benchmark Harness 可借鉴自动失败模式挖掘）、**Tafcm ADI**（评估与诊断接口可升级为自动 trace 评估）、**dsh-pentest**（红队结果自动分级）
- **连接的知识点**：Validation 编译器（验证维度）、Evals 框架格局（evals-framework-landscape.md 的补充——从"工具"到"自动 trace 评估方法论"）、五维模型 Evaluation 维度
- **潜在收益**：验证编译器的"自动判断"环节有了可参考的工程实现；silver-shield 的 Benchmark Harness 可从"人工看报告"升级为"自动挖掘失败模式"
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/pdf/2605.22608 ｜ https://ibm.github.io/CLEAR/ ｜ https://papernotes.org/ACL2026/llm_evaluation/agenteval_dag-structured_step-level_evaluation_for_agentic_workflows_with_error_/ |
| 证据等级 | **FACT（arXiv 全文 + IBM 官方项目页 + 开源包核验通过）** |
| 验证方式 | 读 CLEAR 源码 → 在 silver-shield Benchmark 或一个最小 agent 上跑三级评估 → 对照"验证编译器"的 Evidence→Judgment 环节 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
