# 候选证据卡 · [cand] dsh-memory-evolve（DeepSeek Harness 跨会话记忆+自进化插件）
> 状态：`[cand]` ｜ 分类：Agent Memory × Harness（G2/G3 交叉）/ star 基准 B 级信号核验建卡 ｜ 发现：2026-10-01（雷达 #30，star 信号评估） ｜ 等级：**B→A 候选**
## 一句话定位
用户 star 过、且被 **dsh 官方 use-cases 收录**的 DeepSeek Harness 纯插件——为 dsh 带来"跨会话长期记忆 + 后台自我进化"（五轨记忆·git 分支感知·回合内自我审查·技能自我进化与技能管理器·COI 调度·会话广播），零核心修改、零运行时依赖——**直接解决 dsh"会话即忘"痛点**。
## 1. 它解决什么问题
- 痛点：dsh（DeepSeek Harness）会话间无记忆——跨会话上下文丢失、技能不沉淀、经验不积累；需要记忆/技能管理能力但不想改核心
- 方案：**纯插件实现**（零核心修改、零运行时依赖、随装随用卸载即净）——五轨记忆、git 分支感知、回合内自我审查、技能自我进化与技能管理器、四轨待办、COI 调度、会话广播、会话搜索、提示词管理器、临时信息便签["https://www.dsh.so/use-cases/memory/"]
## 2. 为什么现在值得关注（活跃度证据）
- **dsh 官方 use-cases 收录**（09-23 memory 页 / 09-30 GitHub 页）——插件生态官方背书 ✅["https://www.dsh.so/use-cases/memory/"]["https://www.dsh.so/use-cases/github/"]
- 作者 c@syangwen（dsh 社区开发者）；活跃度 **L5 Low Active**（中等偏低，需实测确认维护状态）
- 与同生态 dsh-evolve（chenzheshushi-commits，8★，zero-token 确定性召回 bigram-Jaccard+FTS5 BM25 RRF）对比——**dsh 记忆插件已有多实现**，选型需实测["https://awesome-dsh-plugin.com/p/chenzheshushi-commits/dsh-evolve/"]
## 3. 与我的连接
- **连接的项目**：**dsh（DeepSeek Harness，内库）**——直接可用插件，解决"会话即忘"；**GrowthOS**——"技能自我进化"与其能力沉淀语义同构；**agent-attention**——"COI 调度/会话广播"通知语义
- **连接的知识点**：Agent Memory（S4，EnSIMem/SEEM 证据线——五轨记忆是否"证据保留"需核验）、Harness 自我演化（HarnessDev/JIT-Agent——技能自进化对照）、五维模型 Memory/Control 维度
- **潜在收益**：最短路径给 dsh 补记忆+自进化能力（不用等自研）；作为"插件式记忆"与 agent-memory 卡各方案（Letta/Mem0/EnSIMem）的 dsh 侧对照实现
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://www.dsh.so/use-cases/memory/ ｜ https://www.dsh.so/use-cases/github/（官方收录页） |
| 证据等级 | **FACT（官方收录页核验通过）+ 活跃度待实测** |
| 验证方式 | 克隆插件 → 在 dsh 本地跑"跨会话记忆"最小场景（会话 A 写入事实→会话 B 召回）→ 核验五轨记忆是否证据保留（对照 EnSIMem 标准）→ 评估技能自进化是否可审计 |
| 预期完成时间 | 2026-10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察（B→A 候选：官方收录 + 用户 star + 直接可用，唯一风险是 Low Active 与多实现竞争）
- [ ] 拒绝（原因）
