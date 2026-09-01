# 扫描日志
> 日期：2026-09-02 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（首次运行） ｜ 来源：general_search ×6 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：读取 07_radar_watch/README.md、00_bootstrap/（4 份地图）、06_expansion_index/README.md（去重基准）
- 聚焦方向（按雷达规范"按当天聚焦、不全量"）：
  1. AI 安全/Agent 安全新框架（OWASP 生态）
  2. MCP / Agent 互操作协议新变化
  3. Agent Memory 实现层新动态（Mem0/Zep/Letta）
  4. A2A 协议与 AAIF
  5. Agent Harness / Computer Use / Browser 自动化新开源项目
  6. 本地/边缘/移动端 LLM 工具链（Flutter/Dart 方向）
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | OWASP Red Teaming Solutions Landscape + Red Teaming Taxonomy（2026 Q2/Q3） | 补齐 AI 安全（G1）红队侧的官方分类与工具景观 | genai.owasp.org | → 增量更新 [cand]owasp-agentic-security.md |
| 2 | OWASP Skills Top10 B1-B4 Trust Boundary Model（2026-05） | AI coding agent 流水线信任边界威胁模型，与 AgenticCI 资产直接相关 | owasp.org | → 增量更新 [cand]owasp-agentic-security.md |
| 3 | MCP 2026-07-28 final 后新 Roadmap（2026-08-22）+ go-sdk Stateless 发布 | 确认 MCP 无状态规范已 final 并进入下一阶段 | blog.modelcontextprotocol.io / GitHub | → 增量更新 [cand]mcp-2026-07-28-stateless.md |
| 4 | A2A 正式移交 AAIF（2026-08-17/18，250+ 成员）+ MS .NET 接 A2A v1 | 确认 A2A 治理落地、生态继续扩张 | dailyaiworld / devblogs.microsoft.com | → 增量更新 [cand]a2a-protocol-v1.md |
| 5 | Mem0 SDK 2.0 单遍抽取 + Platform v3 时间感知 + Letta Agents SDK/Mods | Memory 实现层重大演进，与 GrowthOS/TeamMind 直接相关 | mem0.ai / letta.com | → 增量更新 [cand]agent-memory-2026.md |
| 6 | **DeepSeek Harness v0.1（2026-08-13 开源，MIT，Cordis 全插件）** | 国产开源 harness 新样本，与 TeamMind 同构可对照 | deepseek 社区盘点 | → 新建 [cand]deepseek-harness-2026.md（S） |
| 7 | **Flutter 本地 LLM 工具链（ai_edge / flutter_gemma / Llamafu / llama_flutter）** | Tafcm 直接可用的离线 AI 能力，补 G3 本地/边缘空白 | pub.dev / GitHub | → 新建 [cand]flutter-local-llm-2026.md（A） |
| 8 | **Browser Harness（browser-use 生态，MIT，15.7k★）** | 自愈式 CDP 浏览器 harness，campus_order/E2E-CLI 可接 | github.com/browser-use | → 新建 [cand]browser-harness-2026.md（A） |
| 9 | **MS Research Webwright（Odysseys 60.1%）** | 脚本化浏览器 Web Agent 新范式，可复现/可审查 | aifuturefront（待核验一手） | → 新建 [cand]webwright-2026.md（B） |
| 10 | **hermes-agent（Nous Research，~57k★）** | 2026 增长最快开源 agent 框架，纳入选型对照 | ClawBench issue | → 新建 [cand]hermes-agent-2026.md（B） |
| 11 | GUI-Agent-Harness（桌面 GUI agent） | 个人仓库、证据弱 | GitHub | → 丢弃（低证据密度、知名度低） |
| 12 | DeepSeek 技术社区盘点文 | 二手整合，价值已并入主线 | DeepSeek 社区 | → 丢弃（二手来源） |
## 3. 筛选结果
- 进入 candidates：`[cand]deepseek-harness-2026`（S）｜ `[cand]flutter-local-llm-2026`（A）｜ `[cand]browser-harness-2026`（A）｜ `[cand]webwright-2026`（B）｜ `[cand]hermes-agent-2026`（B）
- 已覆盖/重复（增量更新不新建卡）：MCP / A2A / OWASP / Agent Memory 四条已知对象的重要变化
- 与主线无关丢弃：GUI-Agent-Harness（低证据）、DeepSeek 盘点文（二手）、各类低质量聚合文
## 4. 连接更新
- `04_connections/README.md`：新增 5 行连接卡（DeepSeek Harness / Flutter 本地 LLM / Browser Harness / Webwright / hermes-agent），总行数 17 → 22
- `06_expansion_index/README.md`：新增 2026-09-02 雷达扫描段（5 对象）+ Changed 增量段（4 条）
- `_INDEX.md`：candidates 17 → 22 张，S5/A8/B5 分档更新
## 5. 下一步
- 验证优先级：S 级 DeepSeek Harness（clone 源码/对照 TeamMind）＞ A 级 Flutter 本地 LLM（Tafcm 最小 demo）＞ Browser Harness（本地跑通）
- Webwright / hermes-agent 待一手来源核验（GitHub/论文）后再定是否深入
- 下次扫描聚焦：AI 安全（G1）红队工具实测、Tafcm 本地 LLM 选型实证进度

## 6. 追加：一手来源核验 + DeepSeek Harness 晋升 validated（2026-09-02 同日续做）
### 6.1 三对象一手来源核验（general_search ×3，全部确认 FACT 级）
| 对象 | 一手来源 | 证据等级 | 备注 |
|---|---|---|---|
| DeepSeek Harness | github.com/deepseek-ai/deepseek-harness ｜ deepseek.com/harness/en/ ｜ deepseek-harness.github.io ｜ 论文 arXiv 2608.25512 | FACT | 确认 MIT/TS/dev-preview/Cordis 全插件 |
| MS Webwright | github.com/microsoft/Webwright ｜ microsoft.github.io/Webwright ｜ MSR writeup ｜ arXiv 论文 | FACT | 确认 Terminal-native + skill_factory；Odysseys 60.1% / Online-Mind2Web 86.7% |
| hermes-agent | github.com/NousResearch/hermes-agent ｜ hermes-agent.nousresearch.com ｜ newreleases 记录 | FACT | **关键修正：stars ~57k → ~217k（v0.18.2，2026-07-07）**，远超雷达初记 |
### 6.2 DeepSeek Harness 源码级验证（S 级 → 晋升 validated）
- 验证动作：`git clone --depth 1 github.com/deepseek-ai/deepseek-harness`（~8800 文件，50+ packages）→ 精读 README.zh / docs/architecture.zh / docs/capability-seams.zh
- 验证结论（全部确证）：Cordis 插件树（无特权内核，一切皆插件）；profile（web/headless/sdk/sdk-minimal/acp）+ 组合包 + 有序 patch overlay 配置树；capability seam 三角色（Service Definition/Provider/Consumer）；配套论文 arXiv 2608.25512
- TeamMind 对照产出：五维模型逐项映射（Runtime=agent-loop/seam、Memory=session 事件日志+projection、Tool=guarded tools 流水线、Orchestration=subagent/agent-teams、Evaluation=invariants）→ 三点可借鉴：插件化 seam 化 / 事件溯源会话日志 / 把关工具流水线
- 归档：`03_expansion_queue/validated/[val]deepseek-harness-2026.md` + `validated/README.md`（连同首轮 promptfoo 共 2 张 validated）
- 相关文件同步更新：三张候选卡证据升级 FACT、06_expansion_index、04_connections、_INDEX.md
