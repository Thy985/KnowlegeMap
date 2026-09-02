# 扫描日志
> 日期：2026-09-03 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 2 次运行） ｜ 来源：general_search ×5 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：07_radar_watch/README.md、01_personal_tech_map.md、02_knowledge_gap_map.md、06_expansion_index/README.md（去重基准）
- 今日聚焦（按雷达规范"按当天聚焦、不全量"）：
  1. **G1 AI 安全/Agent 安全新框架与新论文**（最高优先缺口，PyRIT 生态 / prompt injection 审计）
  2. **G3 本地/边缘/移动 AI 新工具**（Tafcm 直接相关）
  3. 已知 harness 生态增量（DeepSeek Harness / hermes-agent 新 Release）
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **MS RAMPART + Clarity（2026-05-20 开源，MIT，PyRIT 之上）** | Agent 安全左移到 CI/CD 的可落地工具，直接命中 G1 最高缺口 | microsoft.com/security/blog | → 新建 [cand]rampart-clarity-2026.md（S） |
| 2 | **PI-Hunter（arXiv 2606.12737）** | 注入审计从"攻击是否成功"转向"摄入路径定位"，与 Validation 编译器思维同构 | arXiv | → 新建 [cand]pi-hunter-injection-audit-2026.md（A） |
| 3 | ARGUS（arXiv 2605.03378）+ PI SoK（2602.10453）+ PISmith（2603.13026） | 注入防御因果溯源 / 威胁分类学 / RL 红队——PI-Hunter 同线论文族 | arXiv | → 并入 [cand]pi-hunter-injection-audit-2026.md（同线） |
| 4 | **hermes-agent v0.20.x 系列（The Herald 08-03 / v0.20.3 08-16）** | 已知对象重要变化：版本 4 个月 0.11→0.20，增速极快，新增 Windows/DeepSeek V4 | hermesagent.org.cn / release 记录 | → 增量更新 [cand]hermes-agent-2026.md |
| 5 | **flutter_litert_lm / LiteRT-LM 取代 MediaPipe LLM** + llx_flutter / flutter_native_ai / Flutter Local AI | Tafcm 本地 LLM 选型新增 3 派候选，Android 官方路线已切换 | GitHub / pub.dev | → 增量更新 [cand]flutter-local-llm-2026.md |
| 6 | CSA Agentic AI Red Teaming Guide（2025） | 云安全联盟 12 类风险攻防框架 | CSDN 解读 | → 已覆盖（OWASP 体系已含同类），暂不建卡 |
| 7 | awesome-agent-skills-security（TAB benchmark / Proteus 自进化红队） | Agent skill 生态安全资源清单 | GitHub | → 观察（信息密度高但为聚合清单，待深入时再收） |
| 8 | DeepSeek Harness | 无新版本（仍 2026-08-13 发布） | — | → 无动作 |
## 3. 筛选结果
- 进入 candidates（新 2 张）：`[cand]rampart-clarity-2026`（S）｜ `[cand]pi-hunter-injection-audit-2026`（A）
- 增量更新（不新建卡，2 条）：hermes-agent（v0.20.x + Windows/DeepSeek V4 等）｜ flutter-local-llm（LiteRT-LM 取代 + 新插件）
- 与主线无关/已覆盖：CSA 指南（并入 OWASP 体系）、awesome-agent-skills-security（待深入）、DeepSeek Harness（无新版本）
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-03 雷达扫描段（2 新对象 + 2 Changed 增量）
- `04_connections/README.md`：新增 2 行连接卡（RAMPART/Clarity、PI-Hunter），共 22 → 24 行
- `_INDEX.md`：candidates 22 → 24 张，S 级更新
## 5. 下一步
- 验证优先级：RAMPART/Clarity（S，可在 dsh-pentest 跑最小 CI 安全测试）＞ PI-Hunter 方法精读（A）＞ hermes-agent 升 A 评估
- 下次扫描聚焦：G1 AI 安全工具实测进展、Tafcm 本地 LLM 三派选型实证、DeepSeek Harness 新版本
