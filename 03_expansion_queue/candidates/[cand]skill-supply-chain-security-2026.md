# 候选证据卡 · [cand] Agent Skill 供应链安全（SkillFortify 形式化验证 + Unit 42 BIV 实证）
> 状态：`[cand]` ｜ 分类：AI 安全攻防 / Agent 供应链（G1） ｜ 发现：2026-09-05（雷达 #4） ｜ 等级：**S**
## 一句话定位
2026 年新出现的 **Agent Skill 供应链安全**主题：SkillFortify（arXiv 2603.00195，形式化验证框架——基于 Dolev-Yao 攻击者模型的**静态分析保证**而非启发式扫描，540-skill benchmark F1 96.95%）+ Palo Alto Unit 42 的 **Behavioral Integrity Verification（BIV）**（审计 OpenClaw ClawHub 全部 49,943 个 skill，发现 **80% 偏离声明功能、5% 为恶意**）——"技能层"正在成为 Agent 供应链攻击的新前线。
## 1. 它是什么 / 解决什么问题
- 痛点：Agent skills 赋予 LLM 特权第三方能力（文件系统/凭据/网络/shell），现有安全只查恶意 prompt 与运行时行为，**skill 产物本身无人验证**["https://arxiv-troller.com/paper/3171240/"]
- **SkillFortify**：首个把形式化威胁模型（DY-Skill，Dolev-Yao 适配五阶段 skill 生命周期）+ 能力静态分析 + 依赖解析 + 公开基准合一的系统；五条数学定理保证 soundness（报告安全即证明不能超出声明能力）["https://arxiv.org/pdf/2603.00195v2"]["https://github.com/qualixar/skillfortify/wiki/Why-SkillFortify/Formal-Foundations"]
- **BIV（Unit 42）**：声明 vs 实际能力的有类型集合比较，跨 metadata/可执行代码/自然语言指令三面，29 能力 7 家族分类学；对 ClawHub 全量审计揭示 80% 偏离 + 5% 恶意["https://newclawtimes.com/articles/palo-alto-unit42-openclaw-skill-registry-supply-chain-audit/"]
- 同线：MalSkills（神经符号恶意 skill 检测，7 注册表大规模部署）["https://arxiv.org/html/2603.27204v1"]、SkillSafetyBench（skill-facing 攻击面评估）["https://arxiv.org/html/2605.12015v1"]、Agent Skill Security 威胁模型（Semantic Camouflage/Sybil Publication/Trigger Poisoning）["https://arxiv.org/html/2607.13987v1"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-05）**：arXiv 2603.00195 ✅（Bhardwaj 2026）、SkillFortifyBench（540-skill 公开基准，byte-identical 复现）✅、Unit 42 官方报告（2026-06-23，ClawHub 5 个恶意 skill 已 takedown）✅
- 实证冲击力强：49,943 个 skill 审计，80% 偏离声明——说明"下载即信任"的 skill 生态已系统性失守["https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/"]
- 与 OWASP Agentic Top10 **ASI04（Agentic Supply Chain Vulnerabilities）** 直接对应，2026 已形成"官方分类 + 形式化工具 + 实证审计"完整闭环["https://atlas.latticeflow.ai/framework/owasp_agentic_top10_2026/"]
- Slopsquatting（模型幻觉包名被武器化）等新攻击模式持续出现["https://codex.danielvaughan.com/2026/06/16/slopsquatting-hallucinated-packages-codex-cli-supply-chain-defence-pretooluse-hooks-lockfile-discipline/"]
## 3. 与我的连接
- **连接的项目**：**EP-002（Permission Is Security Boundary）**——skill 能力验证正是权限边界的声明侧保证；**campus_order（OpenClaw 生态）**——BIV 直接审计的就是 OpenClaw skill 注册表；**dsh-pentest**——供应链攻防测试方法；**agent-attention**——跨 Agent 通信面也是供应链面
- **连接的知识点**：AI 安全（G1）、Skills 体系（我的 Claude Code Skills 资产直接受此威胁模型约束）、五维模型 Tool 维度、OWASP Agentic 体系（ASI04 对应）
- **潜在收益**：给"AI 安全攻防"空白补上**可本地运行的形式化验证工具**（SkillFortify 支持 Claude Code skills / MCP server / OpenClaw manifests 三类输入）——这是我知识体系里"声明 vs 实际"验证纪律在安全侧的实证
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/pdf/2603.00195v2 ｜ https://github.com/qualixar/skillfortifybench ｜ https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/ ｜ https://arxiv.org/html/2603.27204v1（MalSkills） |
| 证据等级 | **FACT（arXiv 全文 + 公开基准仓库 + Unit 42 官方报告核验通过）** |
| 验证方式 | clone SkillFortify → 对一组 Claude Code skills 跑能力验证 → 对照 BIV 分类学做声明 vs 实际审计 → 评估纳入 dsh-pentest |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
