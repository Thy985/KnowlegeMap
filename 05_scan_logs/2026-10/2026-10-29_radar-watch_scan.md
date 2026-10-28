# 深耕扫描日志 · 2026-10-29（Personal Tech Radar · Runtime 周 Day4 增量扫描）

> 定位：周二~周四只追增量（新 release/新工具/相邻项目）；S/A/B 写卡、C 级记日志、普通 release 一律不写。

## 扫描范围
Runtime 领域两路增量检索（agent runtime 新发布 + Dapr/Substrate 锚点动态），去重基准比对后判定。

## 发现与判定

### 建卡 1 张（B 级，领域内新工具）
- **[cand]aws-infinity-agent-runtime-2026-10.md**（AWS Infinity，10-23 开源，Apache 2.0，Hydro 项目 AWS×UC Berkeley）：**第三条 runtime 设计路线**——stackless coroutine 式 agent 挂起（tool call=await 点，slice 语义），挂起 agent 只占 history 内存（8GB/75k 并发），serverless step 模式等待零计算，synthetic tool calls（`receive_event__injected`）+ 父子线程消息（无需独立消息系统）。与 durable 品类（步骤持久化）互补而非重复；TeamMind 并发模型直接对照 ["https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/"]
- 判级理由：官方开源（Apache 2.0）+ 学术合作背书 + 设计独特（slice/step 模式）；research early release 故 B 级非 A

### 去重命中 / 不写（B 级以下、已覆盖、普通增量）
- Vercel durable-harness 开源（10-21/22 报道）——durable 品类卡已覆盖
- Azure SDK Agent bindings preview（10-17 feed）——MS Agent Framework durable 已覆盖
- Dapr Agents v1.0 GA 文档确认（10-25 docs 更新）——锚点已建卡
- Pi 1.0 + Pi Durable（10-02 发布）——27 天前旧闻，B- 不写
- Cloudflare Agents SDK Browser Run（10-28 changelog，internal hostnames 隔离容器内 dev server 预览）——SDK 普通增量，记日志

## 文件变更
- **新建** `03_expansion_queue/candidates/[cand]aws-infinity-agent-runtime-2026-10.md`（B 级新卡）
- **修改** `06_expansion_index/README.md`（新增 2026-10-29 深耕段 + 去重基准加 Infinity）
- **修改** `_INDEX.md`（追加本日志行）
- **新建** `05_scan_logs/2026-10/2026-10-29_radar-watch_scan.md`（本日志）

## 结论
**Potentially Relevant**（B 级新卡 1 张：AWS Infinity——极端并发挂起 runtime，周五验证日对照池扩充为 Dapr Agents × Infinity × Restate 三路线）
