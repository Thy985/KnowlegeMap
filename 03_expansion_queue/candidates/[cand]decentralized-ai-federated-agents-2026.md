# 候选证据卡 · [cand] 去中心化 AI / Agent 联邦学习（IETF 草案 + 2026 框架）
> 状态：`[cand]` ｜ 分类：去中心化 AI / 联邦学习（G4 兴趣未接入） ｜ 发现：2026-09-07（雷达 #6） ｜ 等级：**B**
## 一句话定位
2026 年"去中心化 AI + Agent 化"出现标准化信号：**IETF 正式草案《Privacy-Preserving Federated Learning Architecture for Multi-Tenant Agent Systems》（draft-kale-agntcy-federated-privacy）**——把 agent 通信与学习协调分离、跨租户协作训练同时保持数据隔离；同线有 UnlinkableDFL（mixnet 去匿名 DFL）、gspDAG-FL（gossip+虚拟投票安全 DFL）等框架，方向从"学术设想"走向"协议草案 + 可运行系统"。
## 1. 它是什么 / 解决什么问题
- 痛点：多租户 agent 系统需要跨组织/跨租户协作学习，但原始数据不能出域；传统 FL 依赖中心聚合器（单点故障+信任风险），区块链化 DFL 又低吞吐高延迟["https://datatracker.ietf.org/doc/html/draft-kale-agntcy-federated-privacy-00"]
- **IETF draft-kale-agntcy-federated-privacy**：参考架构 = 联邦平均 + 差分隐私 + 安全聚合，实现跨租户知识迁移而不暴露敏感行为数据；**关键设计：agent 通信（可用 A2A/MCP 等现有协议）与学习协调（FL 聚合层）解耦**["https://datatracker.ietf.org/doc/draft-kale-agntcy-federated-privacy/"]
- **UnlinkableDFL**：peer-based mixnet + 分片模型聚合，全去中心化下不可链接性（relay 无法识别参与者身份）["https://arxiv.org/html/2602.21343v1"]
- **gspDAG-FL**：gossip 历史同时用于模型传播与最终性（origin tuple + 虚拟投票 + 证书），去中心化与安全最终性兼顾["https://arxiv.org/html/2607.08651v1"]
- **SoraChain AI**：区块链原生 FL 协议（on-chain 协调/溯源/激励/验证），开源实现["https://github.com/0xtigerclaw/sorachain_ai"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-07）**：IETF Datatracker 草案 ✅（draft-kale-agntcy-federated-privacy，2026-07 创建、09-06 更新）、UnlinkableDFL arXiv ✅、gspDAG-FL arXiv ✅
- IETF 进入标准流程 = 领域从"论文概念"升级为"行业架构讨论"；草案明确对接 agent 协议生态（A2A/MCP）
- 学术侧 2026 持续产出：DAG 区块链异步 FL（ACM 2026）、轻量 INFL 隐式神经表示密钥嵌入（智源社区）["https://dl.acm.org/doi/10.1145/3821820.3821825"]["https://hub.baai.ac.cn/paper/ecaeebfa-b51d-49c4-bb57-919bf95f584c"]
## 3. 与我的连接
- **连接的项目**：**TeamMind**（多 Agent 编排——若未来需跨租户协作学习，此架构是隐私侧方案）；**silver-shield**（隐私/数据隔离原则延伸）；EP-002（权限边界在数据协作域的扩展）
- **连接的知识点**：去中心化 AI / 联邦学习（G4 空白）、多 Agent 互操作（A2A 连接）、隐私保护
- **潜在收益**：补 G4 空白的最小入口；IETF 草案与 A2A/MCP 的解耦设计可作为 TeamMind"协作面与执行面分离"的类比参考
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://datatracker.ietf.org/doc/draft-kale-agntcy-federated-privacy/ ｜ https://arxiv.org/html/2602.21343v1 ｜ https://arxiv.org/html/2607.08651v1 ｜ https://github.com/0xtigerclaw/sorachain_ai |
| 证据等级 | **FACT（IETF 草案 + arXiv 全文 + GitHub 仓库核验通过）** |
| 验证方式 | 精读 IETF 草案架构 → 对照 TeamMind 是否需要跨租户学习 → 评估解耦设计是否可借鉴 |
| 预期完成时间 | 观察期（G4 兴趣层，不设硬期限） |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
