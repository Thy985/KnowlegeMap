# 候选证据卡 · [val] DeepSeek Harness v0.1（开源 Agent Harness）
> 状态：`[val]` ｜ 分类：Agent Runtime / Harness（S5） ｜ 发现：2026-09-02（雷达） ｜ 等级：**S**
## 一句话定位
DeepSeek 于 2026-08-13 开源的 Agent Harness 开发者预览版（`deepseek-ai/deepseek-harness`，MIT，TypeScript）：主打"**Everything is a plugin** / Agent = Model + Harness"，基于 **Cordis 内核**（插件挂载/卸载/依赖管理），模型/工具/技能/会话/沙箱/存储/循环/调度/UI 全部由插件组合而成，可自由替换重组。
## 1. 它是什么 / 解决什么问题
- 解决"如何把 LLM 能力组织成可插拔、可复用的 Agent 运行时"——从单点工具走向 harness 层统一抽象；"Agent 版 Spring"（能力即插件、内核只做装配）["https://deepseek.com/harness/en/"]
- 与 Omnigent（meta-harness）、MS Agent Framework 同属 2026 Harness/Control Plane 范式收敛，但路线不同：**Cordis 元框架 + 全组件可替换插件**
- `core/` 是产品 API 骨架（session/system-prompt/tools），AGENTS.md 明示 pre-release 立场（foundation over blast radius）["https://github.com/deepseek-ai/deepseek-harness/blob/master/AGENTS.md"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-02）**：官方主页 deepseek.com/harness/en/ ✅、GitHub 仓库 deepseek-ai/deepseek-harness ✅（发布即 13k+★，社区报道称已 ~87k★）、官方文档 deepseek-harness.github.io ✅、CLI `npx @deepseek-ai/dsh web` ✅
- 2026-08-13 开源，MIT，developer preview（破坏性变更预期）；TypeScript 实现
- 安装/跑通路径已有社区实证：pnpm install → build → `pnpm dsh web`["https://developer.aliyun.com/article/1755877"]
## 3. 与我的连接
- **连接的项目**：TeamMind（Java 多 Agent 运行时）——同为"项目级 harness"，可借鉴其插件化架构与运行模式设计；agent-attention（可作 harness 的协作/通知插件）；Tafcm（TS 生态，可参考其 CLI/插件机制）
- **连接的知识点**：Harness/Control Plane 候选方向（agent-harness-control-plane.md）、五维模型（本质/架构/Runtime/Orchestration）、EP-002 权限边界（沙箱作为可替换插件）
- **潜在收益**：一个可本地跑通的开源 harness 参考实现，用于 TeamMind 架构对照与"如何模块化 agent 运行时"的实证
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/deepseek-ai/deepseek-harness ｜ https://deepseek.com/harness/en/ ｜ https://deepseek-harness.github.io/deepseek-harness/ |
| 证据等级 | **FACT（官方仓库+主页+文档三处核验通过）**；架构主张为 DESIGN |
| 验证方式 | clone 源码 → 通读 Cordis 插件机制 → 对照 TeamMind 模块划分 → 评估是否可跑 quickstart |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
**✅ 已源码级验证（2026-09-02，clone + 精读 docs/architecture + capability-seams + README）**
- **仓库确证**：`deepseek-ai/deepseek-harness`（MIT，TS，pnpm monorepo，~8800 文件，50+ packages），dev-preview 阶段（明示将有破坏性变更）
- **Cordis 确认**：底层框架为 Cordis；产品每一部分都是插件（模型适配器/工具注册表/会话日志/agent loop 本身），"不存在需要打补丁的特权内核"；profile（web/headless/sdk/sdk-minimal/acp）+ 组合包 + 有序 patch overlay 构成配置树（`dsh --profile web --dump-config` 可见）
- **能力 seam 三角色确证**：Service Definition / Provider / Consumer；替换一个提供方即改变整个产品行为（如 `ctx.fs` 换成远程沙箱 → Bash/PTY/LSP 一起搬走）
- **配套论文**：《A Programming Paradigm for Spatiotemporal Composability》arXiv 2608.25512
- **关键架构亮点（与我的知识连接）**：
  - **Runtime**：`core/agent-loop`（默认驱动器）、turn/step 事件模型（`agent/pre-step` 决定模型所见）
  - **Memory**：`ctx.sessions` 仅追加 SessionEvent 日志 + "模型可见即已记录" 不变量 + `session-projection` 投影 seam + compaction seam
  - **Tool**：`ctx.tools` 作用域化注册表 + 把关流水线（PTC mode 传输、策略前后处理、单调守卫）
  - **Orchestration**：subagent（spawn/fork/ACP/Codex/Claude Code 驱动）+ 实验性 Agent Teams + workflow + jobs
  - **EP-002 权限**：`ctx.sandbox`/`sandbox-policy`/`approval`/`permission-presets`/`credentials` 全套 seam
  - **可观测**：`session-telemetry-otel`（OpenTelemetry 后端）
  - **互操作**：内置 `mcp`、`acp`（Agent Client Protocol）、`e2b` 沙箱
- **TeamMind 对照结论**：dsh 的"能力 seam + 插件树"即我五维模型的工程化样本——Runtime=agent-loop/seam、Memory=session 日志+projection、Tool=guarded tools、Orchestration=subagent/agent-teams、Evaluation=invariants；TeamMind 可从"插件化 seam 化 + 事件溯源会话日志 + 把关流水线"三点直接借鉴。验证达标（≥2 独立证据：官方仓库+架构文档+论文）
> **雷达增量（2026-09-07，Changed）**：
> - **版本快速迭代至 v0.1.3（2026-08-31/09-01 发布）**：v0.1.0-rc.8（08-19）起 14 项升级——**原生图片输入**（/goal、/plan 等核心命令直接看图）、**Claude Code / Codex 可安装为 sub-agent bundles 并编排**（异构 agent 组合）；v0.1.2-alpha.1（08-27）支持**每个 subagent 独立选 provider/模型/effort** + Python SDK Windows x64 包；v0.1.2-alpha.3/v0.1.3 改进长会话导航渲染、修复排队图片投递、移除可选 SQLite Session 后端["https://deepseekv4pro.com/news/deepseek-harness-0-1-2-alpha-3-update"]["https://deepthink.ltd/blog/deepseek-harness-rc8-claude-codex-subagent-2026/"]
> - **星数增长验证**：发布两周突破 **200k+ stars**（09-01 快照），社区对比评测（vs Claude Code/Codex CLI）持续产出["https://pasqualepillitteri.it/news/13654/deepseek-harness-200mila-stelle-claude-code-codex"]["https://rohitraj.tech/en/notes/deepseek-harness-vs-claude-code-codex-cli-2026"]
> - **含义**：① dsh 迭代速度极快且已具备"异构 agent 编排"（Claude Code/Codex 作 sub-agent）能力——这正是 TeamMind 多运行时编排的直接参考；② 图片输入支持让 Tafcm 本地多模态对照价值上升；③ 需在后续轮次核实 v0.1.3 是否仍保持"无特权内核"架构承诺
> **雷达增量（2026-09-11，Changed）**：
> - **v0.1.5（2026-09-10 发布，同日 DeepSeek-V4.1-Flash 正式发布）**：与 **V4.1 Flash 联合训练**——模型针对 Harness 的标准模式、程序化工具调用（PTC）模式、极简模式专项训练优化（"模型与 Harness 一起训练，强化连续工作能力"）；新增文件上传、侧栏预览、标准化 UI 扩展入口["https://www.zonaintegritas.news/deepseek-harness-releases-version-0-1-5"]["https://technode.com/2026/09/10/deepseek-releases-harness-0-1-5-with-v4-1-flash-support-file-uploads-and-sidebar-previews/"]["https://36kr.com/p/3977300285174021"]
> - **生态持续膨胀**：awesome-deepseek-harness 收录 **181 个项目**（09-07，⭐214k+）——插件生态已成规模["https://github.com/Rodert/awesome-deepSeek-harness/blob/main/README.fr.md"]
> - **含义**：① "模型×Harness 联合训练"是全新信号——harness 成为模型专项优化的运行时，反向印证 Agent Harness 是 Agent 工程主战场；② TeamMind 的模型适配层设计可参考 dsh 的 PTC/极简多模式专项优化；③ v0.1.3→v0.1.5 两周两版，迭代速度持续验证"无特权内核"承诺需再核实
## 6. 决策
- [x] 晋升 validated（源码级验证通过，可作 TeamMind 架构参考）
- [ ] 维持观察
- [ ] 拒绝
