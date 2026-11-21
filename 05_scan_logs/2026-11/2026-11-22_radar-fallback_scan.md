# 2026-11-22 Personal Tech Radar 兜底扫描

- 当前深耕领域：Computer Use / Browser（11-23 起）；本任务不收集该领域内容
- 范围：MCP / A2A / Harness / Runtime / Memory / Evals / AI Infra / 安全 / 本地边缘（只找重大突发事件）

## 扫到的东西（5 组）

| 项 | 判定 | 处置 |
|---|---|---|
| **LiteLLM 网关漏洞族**（40217 KEV + 42271×48710 10.0 链 + 42208 + 114612） | **A（在野利用 + KEV + 凭据集中）** | 并入既有卡 `[cand]litellm-double-supply-chain-2026-10.md` §7 |
| DeepSeek Harness 第三方安全测试（朱雀 5.6% / 撤销未验证） | A 级对象、二手数据 | 只记观察，不写卡（对象已在 `[val]deepseek-harness-2026.md`） |
| A2A SDK v1 迁移指南（MS Learn 11-18，JSON-RPC 绑定/端点映射） | 已知对象（A2A v1 GA 的迁移文档） | 不写 |
| AI Agent 挖出医疗影像 0Day（CVSS 9.8、root） | 攻击手法新闻，非 agent 工程实践 | 不写（B 以下） |
| FreeBuf 首页其他（ARTEX、CyberStrikeAI、GitHub 仓库投毒劫持编码 agent） | 前两者已入事件日 14/15；后者无一手细节 | 不写 |

## 去重核对
- `40217 / 42271 / 48710 / BadHost / 42208` 在 06 index、候选卡、日志中**命中 0**（首次入账）
- LiteLLM 对象已存在（10 月供应链投毒卡），故**不新建卡**，按"同一资产第二条路径"并入
- DeepSeek Harness 已有 `[cand]` + `[val]` 两张卡，故不建卡

## 关键事实与口径
- CVE-2026-40217：CISA KEV 2026-11-18，截止 2026-12-02；CVSS 3.1 8.8、PR:L；1.83.11 修（RestrictedPython）；GHSA-wxxx-gvqv-xp7p；X41 D-Sec 2-13 报送 → 5-07 公告 → 11-18 KEV。
- CVE-2026-42271 + CVE-2026-48710：未认证 RCE 10.0 链；42271 已 KEV（6-08）；SANS ISC 蜜罐 11-15/16 见探测 + 变种绕过。
- **二手纠错**：FreeBuf 标题"组合两漏洞可无认证 RCE"指 42271+48710，不是 40217。
- NVD 对 40217 的版本字段为日期式（through 2026-04-08），与 vendor 的 1.83.11 不一致，以 vendor 为准并记差异。

## 结论
**New / Changed**：领域外 A 级对象（LiteLLM 网关漏洞族）首次入账，印证"AI 网关是凭据集中点"这一与 Runtime 周同构的结论。
其余一律 No Action。
