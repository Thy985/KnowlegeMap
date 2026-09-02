# 候选证据卡 · [cand] PI-Hunter 线：Prompt Injection 注入路径审计（论文族）
> 状态：`[cand]` ｜ 分类：AI 安全攻防 / Agent 红队（G1） ｜ 发现：2026-09-03（雷达 #2） ｜ 等级：**A**
## 一句话定位
2026 年出现的 prompt injection 审计新范式论文族：**PI-Hunter**（arXiv 2606.12737）把 Agent 安全审计从"攻击是否成功"转向"**注入摄入路径（Ingestion Path）定位**"——不再只问"这个 prompt 会不会攻破"，而是问"恶意指令从哪个外部源、经哪个工具、在哪一步被信任、可能触发什么动作"。
## 1. 它是什么 / 解决什么问题
- 传统红队只优化攻击成功率；PI-Hunter 构建 source-aware 测试用例，通过 feedback-driven 迭代让 agent 主动暴露潜伏在外部环境中的恶意指令，并**局部化注入进入点**["https://arxiv.org/pdf/2606.12737"]
- 解决"开发者对潜在注入如何产生、如何在 agent 流水线中传播没有可见性"的核心盲区["https://arxiv.org/html/2606.12737"]
- 同线相关：ARGUS（arXiv 2605.03378，Influence-Provenance Graph 因果溯源审计，问"这个动作有没有完整良性的理由"而非"这段文本危险吗"）["https://www.alphaxiv.org/audio/2605.03378"]；PI SoK（arXiv 2602.10453，PI 威胁分类学系统综述）["https://www.arxiv.org/pdf/2602.10453"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-03）**：arXiv 2606.12737 ✅（作者 Pengfei He 等，2026-06-10 发布）、51CTO/LLM-Hacking/Codex 知识库等多方解读
- PI-Hunter 是 2026 年注入审计从"攻击优化"转向"暴露定位"的标志性方法，且**与我的 Validation 编译器"Claim→Evidence"思维完全同构**（把"有注入"变成可定位、可追踪的证据链）["https://codex.danielvaughan.com/2026/06/30/pi-hunter-automated-red-teaming-prompt-injection-localization-codex-cli-pretooluse-posttooluse-defence/"]
- 已有人将其方法映射到 Codex CLI 的 pre-tool-use/post-tool-use 防御硬化，说明方法论可迁移到具体 harness
## 3. 与我的连接
- **连接的项目**：**dsh-pentest**（注入审计方法论直接可用）、**TeamMind**（多 Agent 运行时 = 注入传播链放大面，PI-Hunter 定位方法可用于其安全设计）、**silver-shield**（可信边界）
- **连接的知识点**：AI 安全（G1）、Validation 编译器（证据链思维）、EP-002（权限边界）、Context Engineering（注入本质=不可信上下文混入可信指令）
- **潜在收益**：把"注入路径定位"思维吸收进 dsh-pentest 的审计设计，与 RAMPART（工具层）互补——一个提供 CI 测试框架，一个提供"如何定位"的方法论
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/pdf/2606.12737 ｜ https://arxiv.org/pdf/2603.13026（PISmith：RL 红队注入防御评估） ｜ https://www.arxiv.org/pdf/2602.10453（PI SoK） |
| 证据等级 | **FACT（arXiv 论文全文可读，多方独立解读）** |
| 验证方式 | 精读 PI-Hunter 方法 → 复现其"摄入路径"分析到一个最小 agent 上 → 与 RAMPART 工具对照 |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
