# 兜底扫描日志 · 2026-10-20（Personal Tech Radar · 轻量全领域安全网）

> 定位：一周一域深耕之外的安全网，只捕获领域外重大突发事件，刻意轻量。
> 当前深耕领域：**Harness / 治理**（Day2 已于 10-20 凌晨完成）；该领域细节由深耕任务负责，本任务不重复收集。

## 扫描动作
3 路轻量搜索（MCP/A2A 协议安全、框架/Runtime/Memory/Computer Use 重大发布、重大 CVE）+ 1 次官方文档精读（Dapr Agents Getting Started）。

## 捕获结果

### 领域外 A 级 → 建卡 1 张
- **Dapr Agents**（CNCF Dapr Foundation × NVIDIA，2026-10-16 launch）：开源分布式 Agent 运行时 `github.com/dapr/dapr-agents`。官方文档精读确认：`DurableAgent` workflow-backed 执行模型（每步推理/工具调用持久化）、双 state store（agent-memory 会话记忆 / agent-workflow 执行状态 actorStateStore）、进程中断后按 WORKFLOW_ID 从最后完成步骤恢复不重放、AgentRunner HTTP（/agent/run、/agent/instances/{id}）、pub/sub 驱动 agent、Dapr sidecar + Conversation API（Ollama 本地默认）。
- **评级 A**：CNCF graduated 基础设施基金会的官方新方向（非小工具）；属 Runtime 领域（下一深耕领域，接 TeamMind），与 TeamMind durable state/actor 并发/多 agent 恢复强连接；与 MS Agent Framework（编排框架）不重叠（基础设施运行时层）；公开代码可复现（Runtime 周可跑 quickstart 验证）。
- 建卡：`[cand]dapr-agents-distributed-runtime-2026.md`；连接 1 条（TeamMind/Tafcm/引擎）。

### 领域内（Harness/治理）→ 移交深耕 Day3，不建卡
- **CVE-2026-111322 Archon**（CVSS 9.8；al-ice.ai 10-16、NVD 10-15、AIToolsRecap 10-17）：coleam00/Archon（23,692 stars）控制面默认无认证绑 0.0.0.0，0.2.13–0.11.1，未授权 RCE。与 10-19 越权事件集群同线（默认配置失控），E 层威胁模型素材；Day3 增量扫描可判断是否并入事件集群卡。
- **HaiND/VulnCheck 七 CVE 批量**（10-10 NVD 四小时内发布，al-ice.ai 10-10 精读）：agent/MCP 信任边界批量图谱；B 级 CVE 集群。
- **CVE-2026-108756**（Abilityai Trinity ≤0.9.5 Telegram router 授权缺失，agent-scoped MCP API key 可做人机绑定操作，NVD 10-17）；**CVE-2026-101065**（Obot 关认证时 nobody 持 Owner/Admin + docker.sock 挂载，可注册恶意 MCP server）：B 级。
- **MCP 2.0 首个流式 CVE**（9-22 起：未绑定生命周期 SSE 流拖垮客户端+外泄 Delegation Token；CSDN 10-11）：MCP 2.0 草案（9-19）协议级安全增量，B 级。
- **agent-audit-kit 0.3.80**（PyPI 10-17 更新，State of MCP Security 2026：2,303 个公开 MCP server config 可复现报告）：B 级领域内工具，与 ToFu 同线，留深耕判断。

### 领域外 B 级及以下 → 记日志不建卡
- Cohere North 2（10-05 企业 agent 平台：跨会话记忆+harness 重设计+成本管控，商业发布）
- Alibaba AgentScope 1.0（10-14 通义实验室多 agent 框架 GA，三层架构，同品类无新范式证据）
- Tencent Hy Memory 2.0（10-16 三层开源：Hy-Memory-30A3B 模型+框架+评测 55.49%）——**10-19 兜底已记日志，去重**
- NVIDIA NemoClaw（OpenClaw 开放蓝图集合页面，10-09 更新，B 级）
- MS Agent Framework memory/resilient execution 新特性（10-07 博文，已知对象增量，不建卡）

## 结论
**New**（1 张领域外 A 级候选卡：Dapr Agents，Runtime 周锚点；其余领域内重大 CVE 已移交深耕，B 级一律记日志）。
