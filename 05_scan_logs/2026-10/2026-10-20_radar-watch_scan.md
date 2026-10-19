# 深耕扫描日志 · 2026-10-20（Personal Tech Radar · Harness/治理 周 Day2 · 增量扫描）

> 周二~周四分工：只追增量（新 release/新工具/相邻项目），写候选卡（S/A/B）。

## 本次动作
1. **Re-ground**：读 current_focus.md（领域 active、周一基线已建）、README 每日分工、06_expansion_index 去重基准（47 张候选卡 + 10-19 事件集群标注）、04_connections 尾部。
2. **增量扫描（Harness/治理 领域 2 路搜索 + 1 次精读）**：
   - 发现 **AWS Strands Box**（2026-10-07 开源，Apache 2.0，OS 级行为遏制沙箱）→ 精读 AWS Open Source Blog 确认机制
   - 发现 **agent-aegis 0.4.0**（PyPI，2026-10-15，guardrails+策略引擎+AGEF/AGP）
   - 其余命中（NVIDIA OpenShell / MS Agent Governance Toolkit / AgentGuard by Lictorate / 复旦 AgentGuard）均在既有卡覆盖，去重
3. **评估 10-19 兜底移交事件集群**（Anthropic 越权披露 / CERT-In CIAD-2026-0049 / OpenAI 100+ 组织）→ 达 **A 级**建卡门槛（三方独立权威证据：官方披露+政府 advisory+第三方取证；生产环境失控真实案例，直接支撑 E/B 层），建威胁模型事件卡
4. **建候选卡 3 张**：
   - `[cand]strands-box-os-containment-2026.md`（A）：AWS OS 级遏制沙箱，Dogwood/Cedar 时间性策略 + 凭证外挂网关；与 MXC 同域对照
   - `[cand]agent-containment-breach-2026.md`（A）：2026-10 越权/沙箱逃逸事件集群威胁模型基准
   - `[cand]agent-aegis-governance-2026.md`（B）：Guardrails+Policy+Protocol 一体化开源框架
5. **更新**：04_connections 新增 3 条连接（Strands Box→TeamMind/Tafcm/silver-shield/campus_order；事件集群→TeamMind/silver-shield/campus_order；agent-aegis→TeamMind/silver-shield/引擎 eval 层）；06_expansion_index 追加 Day2 段 + 去重基准追加 3 对象；_INDEX 追加日志行。

## 本周缺口进展
- 缺口①（MXC 实测）→ **升级为 MXC × Strands Box 双对照**（周五验证计划①，两大云厂商 OS 级遏制方案差异）
- 缺口②（无状态策略引擎/确定性 guardrail 对比）→ 对比池扩展为 **Aigis / MS AGT / agent-aegis**（周五验证计划②）
- 缺口③（评测隔离落地核查）→ Strands Box 凭证外挂网关 = 引擎 eval 层凭据注入白名单的**可运行参考实现**

## 周五验证计划（10-23，更新）
1. MXC × Strands Box 双对照（隔离后端/策略语言/凭证处理/时间性能力；对照 Tafcm/TeamMind 权限模型）
2. 确定性 Guardrail / 策略引擎三选对比（Aigis / MS AGT / agent-aegis）
3. 评测隔离落地核查（引擎 eval 默认不出网/凭据注入白名单；对照 Box 网关模式）
4. 事件集群精读（越权技术路径/缓解清单 → 回灌 E 层）

## 结论
**New**（Strands Box A / 事件集群 A / agent-aegis B 三张新候选卡；周五验证计划升级为双对照+三选对比）。
