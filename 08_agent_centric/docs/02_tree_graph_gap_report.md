# Architecture Gap Report（v2 · Tree + Graph 增量）

> 日期：2026-10-08（在 v1 双模式基础上的增量缺口分析）
> 代码依据：`09_agent_engine/engine/`（v1 已交付：domain / knowledge / discovery / composition / workflow / evaluation / memory / pipeline / store）

## 一、v1 已具备（复核，避免重复造轮子）

| 能力 | 位置 | 状态 |
|---|---|---|
| 双模式入口（Mode A/B） | pipeline.py + README | ✅ |
| 扁平能力库（26 个，带证据锚点） | knowledge.CAPABILITIES | ✅ |
| 任务类型分解规则（6 型） | knowledge.TASK_TYPES | ✅ |
| 工具库（28 个，12 维属性） | knowledge.TOOLS | ✅ |
| 12 维 Selection Reason + 评分 | composition.py | ✅ |
| 互斥组 / 数据流兼容 / 有向链 | composition.py | ✅ |
| 阶段化工作流 + 失败恢复 | workflow.py | ✅ |
| Evaluation + 能力 confidence 回写 | evaluation.py | ✅ |
| Agent Operational Memory（JSON 持久化 / 事后学习 / 工作流版本演进） | memory.py | ✅ |
| 安全边界（risk→approval） | pipeline.py | ✅ |

## 二、相对"树 + 图"要求的缺口（v2 必须补）

1. **能力是扁平 dict，任务分解产出扁平 list**。
   无法表达"Web Security Assessment → Reconnaissance 下含 Asset / Subdomain / Service / Fingerprint 四个子能力"。
   代码依据：`knowledge.TASK_TYPES[...]["required_capabilities"]` 是一维列表；`discovery.decompose_task` 直接返回它。

2. **没有 Domain Tree**。领域知识没有层级组织（Cybersecurity → Web Security → Reconnaissance / Mapping / ...）。
   现有 `capabilities/*.md` 只是注册表，没有 domain 归属。

3. **没有 Capability Graph**。跨域复用无法表达：
   `http-interaction` 同时属于 Web Security / API Testing / Web Automation / Browser Agents，
   但 v1 只有 `prerequisites` 单向依赖边，没有 domain membership / 复用边。

4. **没有 JIT 展开**。v1 一次性产出全部能力需求，不按 agent 状态剪枝；
   无法"只展开缺失分支、已具备的分支不深入"。

5. **Skill 是空壳**。`domain.Skill` 已定义但 `knowledge` 无任何 Skill 数据，
   Capability → Skill → Tool → Project 分层断在 Skill 这一层。

6. **节点没有统一状态视图**。用户要求每个能力节点携带 Current State / Gap / Candidate Tools / Selected Tool，
   v1 这些信息散落在 gap_analysis / discovered_tools / chain 三个不同结构里。

7. **测试缺"树"的断言**。v1 测试断言的是扁平 list 长度，无法验证树的层级与 JIT 剪枝行为。

## 三、v2 设计（树与图分工）

```
Domain Tree（领域组织，静态）
   组织"领域由什么组成"，不随任务变化
        │
        ▼ 任务查询
Capability Tree（任务动态实例化，JIT 展开）
   组织"完成这个任务需要什么能力层级"，随任务变化
   每个节点：current_state / gap / candidate_tools / selected_tool
        │ 叶子节点映射
        ▼
Capability Graph（跨域复用 + 依赖，底层）
   表达"能力跨领域复用 / 依赖 / 产出"，树是它的视图
        │
        ▼
Capability → Skill → Tool → Project（分层）
   Capability=What / Skill=How / Tool=With what / Project=来源
        │
        ▼
Tool Composition（复用 v1）→ Workflow（复用 v1）→ Evaluation → Memory（复用 v1）
```

**分工原则**：
- Tree 用于层级组织与任务分解（Domain Tree 静态、Capability Tree 动态）。
- Graph 用于跨领域复用、依赖关系与组合（底层不丢复用关系）。
- 树是图的"任务视图"：同一图节点（如 http-interaction）可在不同任务的树中出现。

## 四、新增/改造文件

| 文件 | 动作 | 内容 |
|---|---|---|
| `engine/domain.py` | 改造 | 新增 CapabilityNode（树节点，含 state/gap/candidates/selected）、DomainNode |
| `engine/trees.py` | 新增 | Domain Tree + 6 任务型 Capability Tree 模板 + JIT 展开算法 |
| `engine/capability_graph.py` | 新增 | Capability Graph（domain membership / 依赖 / 复用 / 产出边 + 查询） |
| `engine/knowledge.py` | 扩充 | DOMAIN_TREE、CAPABILITY_TREE_TEMPLATES、SKILLS（叶子能力证据锚点） |
| `engine/pipeline.py` | 改造 | Tree 驱动：JIT 展开 → 节点级发现 → 组合 → 工作流 → 评估 → 记忆 |
| `engine/store.py` | 扩充 | 导出 Domain Tree / Capability Tree / Capability Graph 资产 |
| `tests/test_pipeline.py` | 改造 | Test 1-5（含树层级断言、JIT 剪枝、A→C→D 排除 B） |
| `08_agent_centric/docs/02_tree_graph_architecture.md` | 新增 | 本文档的正式架构说明 |

## 五、可直接复用（不重写）

- TOOLS 28 个工具属性 → 树叶子节点的工具发现数据源。
- composition.evaluate_candidate / fit_score / compose → 节点级选择与组合。
- workflow.synthesize_workflow → 阶段化。
- evaluation / memory（MemoryStore、post-task learning、workflow 版本演进）→ 直接复用。
- 候选卡/star 证据纪律 → 叶子节点与 Skill 的证据锚点。

## 六、验收口径（对照用户第 19 节）

- Test 1 Human 认知扩展不回归。
- Test 2 Task → Capability Tree（层级）→ Gap → Tools → Workflow。
- Test 3 候选 A/B/C/D → A→C→D，B 被排除且有理由。
- Test 4 两次相似任务：第二次复用历史 Workflow。
- Test 5 Capability：unknown → validated + Evidence。
