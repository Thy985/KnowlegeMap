# 候选证据卡 · [cand] Microsoft RAMPART + Clarity（Agent 安全左移工具）
> 状态：`[cand]` ｜ 分类：AI 安全攻防（G1） ｜ 发现：2026-09-03（雷达 #2） ｜ 等级：**S**
## 一句话定位
Microsoft AI Red Team 于 2026-05-20 开源的两款 Agent 安全工具（MIT，PyRIT 生态之上）：**RAMPART**（Risk Assessment and Measurement Platform for Agentic Red Teaming，pytest 原生测试框架，内嵌 CI/CD）负责"运行时持续安全测试"，**Clarity**（设计审查助手）负责"写代码前质疑 agent 架构"——把安全左移到 Agent 开发全生命周期。
## 1. 它是什么 / 解决什么问题
- PyRIT 面向"系统建成后由安全研究员的黑盒发现"，RAMPART 则面向**开发者的开发工作流**——把红队技术变成可嵌入 CI/CD 的 pytest 测试["https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/"]
- 针对三类结构性弱点：prompt injection（CWE-20 不当输入验证）、工具滥用、数据外泄等 agent 特有风险["https://www.imtr.net/article/microsoft-storms-rampart-adds-clarity-to-agentic-ai-safety-5a63"]
- 目标：让 agent 从"生成文本"阶段就引入安全测试，而非事后补救
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-03）**：Microsoft Security Blog 官方发布文（2026-05-20）✅、MIT 开源、GitHub 公开（含 MS AI Tour 2026 动手实验仓库 microsoft/aitour26-LTG156）✅
- 建立在已成熟的 PyRIT（0.13+ 持续更新，2026-08-31 仍有新 Release）之上，生态可信["http://microsoft.github.io/PyRIT/"]
- 直接命中 **G1 最高优先缺口**（AI 安全与攻防），且是可落地工具的实证路线
## 3. 与我的连接
- **连接的项目**：**dsh-pentest**（内库 AI 攻防 Hub，可改造成基于 RAMPART 的 agent 安全 CI）、**silver-shield**（防诈骗=AI 安全应用，RAMPART 的输入验证思路可复用）、**E2E-CLI**（测试方法论同构：把安全测试当 CI 测试写）
- **连接的知识点**：EP-002（权限即安全边界）、AI 安全缺口（G1）、Validation 编译器（Claim→Evidence 结构可映射到安全测试断言）、OWASP Agentic 体系（增量对照）
- **潜在收益**：一条"把 AI 安全从知识缺口变成可运行 CI 测试"的落地路径，直接给 dsh-pentest 填骨架
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/ ｜ https://github.com/microsoft/aitour26-LTG156-safeguard-agentic-ai-solutions-with-ai-red-teaming-agent ｜ https://microsoft.github.io/PyRIT/ |
| 证据等级 | **FACT（MS 官方博客 + 官方 GitHub 仓库核验通过）** |
| 验证方式 | 读 RAMPART 文档 → 在 dsh-pentest 侧跑最小 CI 安全测试 → 对比 OWASP 体系覆盖 |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
