# 09_agent_engine · Agent-Centric Engine（可运行最小闭环）

> **定位**：KnowlegeMap 的 Mode B 执行引擎——纯 Python 标准库，无第三方依赖。
> 链路：**Task → Capability Tree（JIT）→ Capability Gap → Tool/Project Discovery
> → Tool Composition（带理由）→ Workflow → Evaluation → Agent Operational Memory → Capability Evolution**。
> 原则：Agent 一等公民；"需要什么"先于"推荐什么"；Tree 组织层级、Graph 跨域复用；
> Star 仅弱信号；高风险任务强制 approval 前置（EP-002）。

## 运行

```bash
cd 09_agent_engine

# 端到端测试（Test 1-5 + v3 Skill Evolution，24 用例）
python3 -m unittest discover -s tests

# CLI 最小闭环（安全测试演示：能力树→JIT→组合→工作流→评估→记忆→资产落盘）
python3 cli.py demo --agent pen-test-agent

# 指定任务
python3 cli.py run --task-type e2e-web-testing \
    --objective "对官网跑端到端回归" --task-id t-001 --write-assets
```

## 模块

| 模块 | 职责 |
|---|---|
| `engine/domain.py` | 一等实体：Agent / Capability / **CapabilityNode** / **DomainNode** / Tool / Skill / Workflow / Task / Evidence / Evaluation / SelectionReason / AgentMemory |
| `engine/knowledge.py` | 种子知识库：26 能力 / 6 任务类型 / 28 工具 / **DOMAIN_TREE** / **4 型 CAPABILITY_TREE_TEMPLATES** / **8 SKILLS**，全部带证据锚点 |
| `engine/trees.py` | **v2**：Domain Tree 构建 + Capability Tree 任务动态实例化 + JIT 展开 + 节点级发现/回填/渲染 |
| `engine/capability_graph.py` | **v2**：Capability Graph（跨域 membership + 依赖边；shared/removal_impact 查询） |
| `engine/discovery.py` | Task 分解 / Gap 分析（前置传递闭包）/ 能力驱动工具发现 / 未知能力发现 |
| `engine/composition.py` | 多维评分 → 互斥裁决（**含回退 _fallback**）→ 数据流兼容 → 有向链 + 理由 |
| `engine/workflow.py` | 阶段化工作流（checkpoint / failure_recovery / 角色 / 依赖序） |
| `engine/evaluation.py` | criterion 打分（**每 criterion 证据保留**）+ 能力 confidence 回写 |
| `engine/memory.py` | Agent Operational Memory（JSON 持久化；post-task learning；历史工作流复用；版本演进） |
| `engine/skill_evolution.py` | **v3**：tool_stats 驱动 Skill 版本演进（重排/剔除失败工具/插入失败检查；数据驱动理由） |
| `engine/pipeline.py` | Tree 驱动主流程 + 安全边界 + "删掉 Tool X 损失什么能力"查询 |
| `engine/store.py` | 产物 → 08_agent_centric/ Markdown（含 **domains / graph / skills / versions** 导出） |

## 树与图分工（v2 核心）

- **Domain Tree**：静态组织领域（3 根域）。
- **Capability Tree**：任务动态实例化；不同 Task 产生不同树；JIT 按 agent
  状态剪枝（已具备分支不展开）。
- **Capability Graph**：跨域复用（http-interaction 属 4 领域）+ 依赖边。
- 树是图的任务视图，`maps_to` 桥接节点与扁平能力。
- 分层：**Capability(What) → Skill(How) → Tool(With what) → Project(来源)**。

详见 `08_agent_centric/docs/03_tree_graph_architecture.md`。

## 测试场景（Test 1-5 + v3，24 用例）

| 场景 | 输入 | 输出 |
|---|---|---|
| Test 1 Human 认知扩展 | Human 资产 | 00-07 完整可读、模板兼容（不回归） |
| Test 2 Agent Task Expansion | Task + Agent | Capability Tree（层级/动态）+ Tools + Workflow |
| Test 3 Tool Composition | 候选 A/B/C/D | A→C→D，排除 B 并说明；回退；弱信号 |
| Test 4 Agent Memory | 两次相似任务 | 复用历史 Workflow，演进 v2 |
| Test 5 Capability Evolution | unknown→validated | 置信提升 + Evidence；失败塑形；JIT 剪枝；Graph 跨域 |
| v3 Skill Evolution | 多次任务 tool_stats | 失败工具剔除/重排/插检查；版本递增；持久化；pipeline 触发 |

## Skill Evolution（v3 核心）

让 Skill 从静态 procedure 变成可演进资产：

- 任务后用 `tool_stats`（usage_count / success_rate / failure_modes）：
  1. 按成功率重排 required_tools（成功率高优先）；
  2. 样本≥3 但成功率 <0.5 → 降级/剔除；
  3. 针对高频 failure_mode 插入检查步骤（timeout→超时重试、false-positive→二次重放…）。
- 版本化，演进理由引用真实成功率（非 LLM 生成）；
  样本不足或表现稳定不产生新版本（防膨胀）。
- 版本存 Agent Memory，未来相似任务用 `latest_skill` 复用，不重新从零。

## 运行结果示例（demo）

安全测试任务 → 8 项能力需求 → 6 分支 23 叶子能力树（JIT 展开）→ 工具链
`garak → playwright → mcp → promptfoo`（browser-use 被互斥排除附 fit 对比；
http-interaction 回退 mcp）→ 8 阶段工作流 → Evaluation score=0.887 →
记忆落盘；资产导出 domains / capabilities(graph) / skills。
