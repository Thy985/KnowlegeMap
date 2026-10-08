# 03 · Tree + Graph 架构（v2 正式说明）

> 本文是 v2（24 节版）的正式架构说明。配套：`00_architecture_gap_report.md`
> （v1 缺口）、`01_agent_domain_model.md`（10 实体）、`02_tree_graph_gap_report.md`
> （v2 增量缺口）。

## 1. 为什么需要树与图分工

v1 能力是扁平 dict（26 个 capability），任务分解产出扁平 list，无法表达：
- "Reconnaissance 下含 Asset / Subdomain / Service / Fingerprint 四子能力"；
- 同一能力跨领域复用（HTTP Interaction 同时属于 Web Security / API Testing /
  Web Automation / Browser Agents）。

纯树无法表达多 parent（复用）；纯图缺少层级组织与任务分解的可读性。
**v2 采用树 + 图分工**：

| 结构 | 职责 | 生命周期 | 代码 |
|---|---|---|---|
| **Domain Tree** | 静态组织"领域由什么组成" | 长期稳定 | `trees.build_domain_tree` |
| **Capability Tree** | 任务动态实例化、JIT 展开 | 每任务一棵 | `trees.instantiate_capability_tree` / `jit_expand` |
| **Capability Graph** | 跨域复用、依赖、组合 | 全局唯一 | `capability_graph.CapabilityGraph` |

**树是图的"任务视图"**：同一图节点（如 http-interaction）可在不同任务的树中
出现，通过 `maps_to` 桥接到扁平能力（图节点）。

## 2. Domain Tree

3 个根域：
- `cybersecurity` → web-security（reconnaissance / web-mapping /
  vulnerability-assessment / validation / evidence / reporting）、api-security、
  red-teaming、defensive-security；
- `ai-agent-engineering` → runtime / memory / evaluation / orchestration /
  observability / governance / capability；
- `software-engineering` → testing / automation / developer-tools。

数据源：`knowledge.DOMAIN_TREE`。导出：`08_agent_centric/domains/README.md`。

## 3. Capability Tree（任务驱动 · 动态）

4 个任务型有完整层级模板（`knowledge.CAPABILITY_TREE_TEMPLATES`）：
- **security-assessment**：6 分支 23 叶子（4+4+5+4+3+3）；
- **e2e-web-testing**：3 分支（browser-interaction / http-interaction /
  result-aggregation）；
- **long-running-autonomous-agent**：5 分支（调度/状态/记忆/恢复/评估）；
- **agent-eval-harness**：2 分支（agent-evaluation / reporting）。

无模板的任务型（local-mobile-ai-assistant / multi-agent-team）从扁平
`TASK_TYPES` 投影一层树。

**关键行为：不同 Task 产生不同树**。"评估 Web 安全"与"修复 SSRF"同属
web-security 域，但 Capability Tree 不同——树不是固定百科，而是任务的
能力分解视图。

### 节点统一状态视图（v2 收敛 v1 散落状态）

每个 `CapabilityNode` 同时持有：
`current_state` / `gap` / `candidate_tools` / `selected_tool` /
`selection_reason` / `evidence`。v1 这些状态散落在 gap_analysis /
discovered_tools / chain 三处，v2 收敛到节点。

## 4. JIT Capability Expansion（按需展开）

不建完整百科，按需展开：
```
Task → Root Capability
     → 分支是否已具备（agent confidence ≥ threshold=0.5）？
         ├─ 是 → 剪枝（gap=False, expanded=False），不展开子能力
         └─ 否 → 展开到叶子，逐叶子判定 gap
```
测试 `test_jit_pruning_skips_covered_branch`：agent 已具备
reconnaissance 0.95 → 该分支剪枝、4 个叶子不展开；缺失分支仍展开。

## 5. Capability Graph（跨域复用）

节点 = 26 扁平能力；边 = 依赖（prerequisites）+ domain membership。

核心查询：
- `domains_of(cap)`：http-interaction → 4 领域；
- `shared_capabilities(d1, d2)`：两领域复用能力；
- `reusable_cross_domain(min_domains)`：≥2 领域的可复用能力；
- `dependents(cap)` / `removal_impact(cap)`：沿依赖边传递闭包 =
  "删掉该能力会损失什么"。

导出：`08_agent_centric/capabilities/graph.md`。

## 6. Capability → Skill → Tool → Project 分层

v1 的 Skill 是空壳，v2 补 8 个技能（`knowledge.SKILLS`）：

| 层 | 回答 | 示例 |
|---|---|---|
| Capability | What（做什么） | endpoint-discovery |
| Skill | How（怎么做） | discover → normalize → deduplicate → validate |
| Tool | With what（用什么） | playwright / browser-use |
| Project | 来源（哪个开源实现） | 对应 GitHub 项目 |

Workflow 是执行层（顺序/组合），不是 Capability 层。
导出：`08_agent_centric/skills/README.md`。

## 7. 闭环链路（v2 主流程）

```
Task（安全边界/approval）
 → 扁平 decompose（供组合/工作流/记忆）
 → instantiate_capability_tree + jit_expand（按 agent 状态剪枝）
 → tree gap → 节点级 discover_tools_for_tree（+ 扁平汇总）
 → compose（每能力选最佳 → 互斥裁决 → 回退 → 数据流）
 → annotate_selections（回填节点 selected_tool）
 → workflow（reuse → synthesize → evolve）
 → evaluate_run（每 criterion 证据保留）
 → update_agent_capabilities + apply_post_task_learning
 → 资产导出
```

## 8. v2 修复的 v1 真实缺陷

1. **互斥裁决无回退**：browser-use 被 playwright 排除后，其负责的
   http-interaction 没有回退到次优候选 → 新增 `composition._fallback`，
   现回退到 mcp（capability_tool_map 含 http-interaction→mcp）。
2. **成功证据丢失**：evaluate_run 只保留 failure 汇总，成功时 evidence 为
   "no observations" → 现每条 criterion 的证据文本都进 Evaluation.evidence。

## 9. 测试

17 个端到端测试（Test 1-5）全通过：
- Test 1 Human 不回归（3）；
- Test 2 Agent Task + 树结构/动态树（4）；
- Test 3 Composition（A→C→D 排除 B / 回退 / 弱信号）（4）；
- Test 4 Memory 复用（2）；
- Test 5 Evolution（unknown→validated / 失败塑形 / JIT 剪枝 / Graph 跨域）（4）。

## 10. 当前限制与下一步

- 树模板靠人工维护（4 型），新任务型走扁平投影；下一步可让 LLM 从任务
  自动生成树草稿并人工确认。
- 观察值由 demo 注入（模拟）；真实执行器（tool_observer）尚未接入。
- Graph 仅有依赖 + membership 两类边；可补数据格式 produces 边，让
  组合的数据流检查从字符串表升级为图查询。
- Skill 是静态 procedure；下一步让 usage_count / success_rate 自动驱动
  skill 版本演进（v1 已在 memory 留 tool_stats，可接到 skill 层）。
