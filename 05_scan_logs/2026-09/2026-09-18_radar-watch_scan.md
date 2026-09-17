# 扫描日志
> 日期：2026-09-18 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 17 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：git 状态（6d5e030 已推送，干净）+ 06_expansion_index/README.md 去重基准（36 对象）
- 今日聚焦（项目直接相关 + 核心研究 + Core 领域）：
  1. **OpenClaw 生态**（campus_order 主线，multiagent 卡）——09-16 记录 2026.9.2 后查新版本
  2. **Agent Memory**（agent-memory S 卡）——09-13 覆盖后首次跟进
  3. **Context Engineering 工具/机制**（Core 领域 × harness 卡）——harness 层实现
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **OpenClaw 2.0（2026.9.4，09-11 发布）**：隔离预演回滚/read-only 配置/慢会话诊断 | 09-16 轮漏网的新版本，升级风险面收敛 | openclaw-lab / appcast.xml | → multiagent 卡增量（Changed） |
| 2 | **OpenClaw SECURITY.md Operator Trust Model（09-08）**：单 gateway 非多租户对抗性边界 + 认证调用者=可信操作者 | campus_order 部署先答"谁能访问 gateway" | raw.githubusercontent SECURITY.md | → multiagent 卡增量 |
| 3 | OpenClaw exec-approvals：sandbox host 默认 deny | 沙箱执行默认拒绝 | docs.openclaw.ai | → multiagent 卡增量 |
| 4 | **Apple Shared Selective Persistent Memory（09-16）**：四类可复用上下文 + 跨用户共享 RBAC | 记忆=选择性+共享新维度 | machinelearning.apple.com | → agent-memory 卡增量 |
| 5 | **MS AF × Cosmos 原生记忆（09-04）** + **MemForest（arXiv 2605.23986）** | 框架级原生记忆 + 记忆=数据管理问题 | devblogs.microsoft / arXiv | → agent-memory 卡增量 |
| 6 | **OKF Agent Memory（09-05）** Git-native Markdown 记忆 + **Grok Build 跨会话记忆（09-16）** + Anthropic /mnt/memory | **"记忆=文件仓库"路线成型**——与 KnowlegeMap 同构 | aitoolly / unite.ai / opentools | → agent-memory 卡增量 |
| 7 | **"Context Engineering Inside the Harness"（09-12）**：compaction/memory/budgeting/todo-state 四机制 + 五 harness 阈值对比 | context 工程下沉为 harness 机制，六职责互证 | marktechpost | → agent-harness 卡增量 |
| 8 | TrueFoundry 网关会话管理（09-11） | context 编排下沉到网关 | truefoundry | → agent-harness 卡增量 |
| 9 | Hindsight（开源代理记忆）/ Mem0/Letta/Zep 新动态 | Hindsight 未核实一手（a2a-mcp.org 二手）；Mem0/Letta/Zep 已覆盖 | — | 跳过/已覆盖 |
## 3. 筛选结果
- 无 S/A/B 级新对象需建卡（全部落入已有 S/A/B 卡增量）
- 增量更新 3 条（不新建卡）：multiagent（OpenClaw 2.0/信任模型）、agent-memory（Apple/MS AF/MemForest/OKF/Grok Build）、agent-harness（4 机制对比）
- 无新范式丢弃：vivo 蓝心 Harness（端侧厂商发布）、讯飞 AStudio（国内产品发布）、Hindsight（二手来源未核验）
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-18 雷达扫描段（0 新对象 + 3 条 Changed 增量）
- `04_connections/README.md`：无新连接对象，连接地图保持 36 行
- `_INDEX.md`：candidates 保持 36 张，日志索引补 09-18
## 5. 下一步
- 验证优先级更新：**campus_order OpenClaw 升级路径评估（2026.9.2→2026.9.4 + gateway 信任模型审查）** ＞ MCPTox 威胁建模 ＞ "记忆=Markdown 仓库"低成本试验（OKF 模式，与 KnowlegeMap 同构）
- 下次扫描聚焦：Agentic Attack 新事件（事件驱动）、eval 新基准、Edge LLM（本地模型）
