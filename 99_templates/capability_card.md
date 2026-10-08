# Capability Card（能力卡）

> 能力是 Mode B 的**发现单位**：先发现"需要什么能力"，再找实现工具。
> 能力 ≠ 工具：一个能力可由多个工具实现；一个工具可实现多个能力。
> 存放：`08_agent_centric/capabilities/`（注册表由 `cli.py` 从种子知识库导出）。

- capability_id：
- name：
- description：
- prerequisites：（依赖链，Gap 分析会展开传递闭包）
- candidate_tools：（实现候选，各带 Selection Reason）
- related_projects：（与本仓库项目画像的连接）
- confidence：（Agent 侧掌握程度 0-1）
- evidence：（FACT / DESIGN / EXPERIMENT，锚点指向 03_expansion_queue 或 00_starred_reference）

## 为什么这个能力值得建模
（回答：它覆盖哪个任务需求、缺失时任务会卡在哪一步）
