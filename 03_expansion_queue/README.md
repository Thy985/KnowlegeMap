# 03 · Expansion Queue（探索队列）

> 本仓库的核心工作区。三级流水线：**inbox（原始线索）→ candidates（候选证据卡）→ validated（已验证）**。

## 工作流

```
inbox/          信号捕捉：URL + 一句话"为什么值得看"（原始，不筛选）
   │  筛选规则：
   │    ① 是否落在 01_known_territory 已覆盖领域？ → 标注"追新"或丢弃
   │    ② 是否与 Top20 / 主线 / 活跃项目相关？      → 不相关丢弃
   │    ③ 是否有一手证据可得（官方文档/源码/论文/Release）？
   ▼
candidates/     候选证据卡（用 99_templates/candidate_card.md）
   │  验证动作：跑通 demo / 精读源码 / 对照实验 / 精读论文
   ▼
validated/      已验证对象（标记证据强度）→ 更新 04_connections → 晋升飞书内库
```

## 状态标记

- 每条线索/候选卡统一在文件名前加状态：`[inbox]` / `[cand]` / `[val]` / `[reject]` / `[dup-已覆盖]`
- validated 对象需写明：验证了什么、证据在哪、与哪个项目/知识连接。

## 当前状态（Bootstrap 后）

- **inbox/ 空** —— 按用户指令，Bootstrap 本次不做大规模扩展，首轮扫描后再填充。
- **candidates/ 空** —— 待首轮扫描（建议从 MCP 与 Agent Evals 切入，见 05_auto_exploration_strategy.md §7）。
- **validated/ 空** —— 首条晋升待产生。

## 配额（防止数量幻觉）

| 阶段 | 单次扫描上限 |
|---|---|
| 周扫描收线 | 5–8 条 |
| 筛选进 candidates | 1–3 张卡 |
| 完成验证进 validated | 0–1 个 |
