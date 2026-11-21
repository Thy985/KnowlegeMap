# 候选对象证据卡 · LiteLLM 双重供应链投毒（2026-10-21/22）

> 状态：`[cand]` ｜ 关联方向：**领域外重大事件（安全 / AI 基础设施供应链）**｜ 日期：2026-10-27（兜底扫描捕获）

## 一句话定位
LiteLLM（企业 AI 栈最广泛部署的推理网关/路由库）2026-10-21 发布流水线被攻破——v1.107.0 的 7 个编译 wheel 植入 credential stealer + RCE 后门（任何 Python 进程启动即激活），GitHub 源码与 sdist 保持干净；48 小时内第二起独立攻击借 GitHub token 泄露发布第二个恶意包。微软 Defender 与 Datadog 均独立取证，确认"AI 基础设施负载组件"已成为高优先级供应链目标。

## 1. 它解决什么问题
- 不解决什么问题——它是**事故与风险基线**：LLM 网关位于企业应用与所有模型之间，被投毒的 LiteLLM 实例能触达每个 prompt、每个模型 API key、每个模型响应；credential stealer 可批量收割模型 key/数据库连接串/企业数据
- 对 AI-Native 工程实践的警示：**发布流水线本身是最薄弱环节**（源码干净≠交付物干净），可信依赖链校验（wheel/sdist/镜像哈希、签名的 SBOM、透明构建）从"可选"变"必需"
- Python startup hook 投毒（`sitecustomize`/`usercustomize` 类机制）是低检测成本、高收益的持久化方式——运行时安全需要验证"加载了什么"，而非只验证"跑的是什么"

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（LiteLLM 官方安全公告，2026-10-21）**：v1.107.0 compromised，受影响 release 已拉取；enterprise 私有 release 不受影响 ["https://www.litellm.ai/blog?post=security-incident-oct-21-2026"]
- **FACT（LiteLLM 官方根因分析，2026-10-23）**：完整攻击链——被盗 GitHub CLI token → 恶意 workflows → 7 个 wheel 全部带毒 + RCE 后门；对 PyPI 与 Docker 镜像发布 ["https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain"]
- **FACT（微软 Defender 独立取证，2026-10-23）**：Python startup hooks 凭据窃取技术细节 + IOC ["https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/"]
- **FACT（Datadog Security Labs，2026-10-21）**：恶意版本在 PyPI + 官方 Docker 镜像约 2 小时，credential stealer 随 Python 启动运行 ["https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/"]
- **FACT（第二起独立攻击，10-21/22，THN/HelpNet 报道）**：AI gateway 日志泄露 GitHub token → 第二个恶意包发布；两家独立攻击者一周内先后得手——"高优先级目标"地位实证
- **不与已有知识重复**：OpenCode 泄露（10-17，开发者工具）与 AgentCorruption（10-08，Bedrock IMDS）同属"供应链/凭据旁路"家族但对象不同；php2shell（PHP 运行时）同属供应链风险但不同域；**LiteLLM 是全新对象**（去重基准无此条目）

## 3. 与我的连接
- **连接的项目**：
  - **silver-shield（AI 安全）**：LLM 网关/推理路由层是用户项目调用模型的中枢——依赖校验（哈希/SBOM/镜像签名）+ 最小权限（gateway 不应持有全部模型 key）是可直接落地的加固点
  - **TeamMind（多 Agent 运行时）**：Agent 工具/模型网关供应链清单=运行时身份与信任基线的一部分（R 层身份：代码与依赖的 verifiable provenance）
  - **Tafcm（本地优先）**：本地推理默认自托管→减少供应链暴露面（与"本地边缘"方向的天然优势互证）
- **连接的知识点**：能力树 agent-runtime.md E 层（身份/信任：运行时加载物可信性）；Harness 周事件集群"供应链投毒"证据线（与 Archon CVE 控制面、php2shell 运行时形成三类供应链事故样本）；MXC/Strands Box"隔离不解决供应链"边界
- **潜在收益**：用户项目生产化的供应链加固检查清单（wheel 哈希校验、GitHub Actions 最小 token、日志脱敏——LiteLLM 第二击正是 gateway 日志泄露 token）

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | LiteLLM 官方公告 ["https://www.litellm.ai/blog?post=security-incident-oct-21-2026"]；根因分析 ["https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain"]；微软 Defender ["https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/"]；Datadog ["https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/"]；汇总 ["https://threatlandscape.io/blog/litellm-1-107-0-supply-chain-compromise-october-2026"] |
| 证据等级 | FACT（官方公告 + 官方根因分析 + 微软/DataDog 双独立取证） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 精读官方根因分析核对攻击链（token 窃取→workflow 注入→wheel 植入→PyPI/镜像发布）；② 检查 silver-shield/TeamMind 依赖树中 LLM 网关类依赖的可信发布校验现状；③ 输出"AI 依赖供应链加固清单"（哈希/签名/SBOM/minimal token/日志脱敏） |
| 预期完成时间 | 2026-10-30（周五验证日）或随深化顺延 |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 7. 雷达增量（2026-11-22 兜底扫描 · A 级 · 一手核验）
**不是新对象，是同一资产的第二条攻击路径**：10 月是发布流水线被投毒，11 月是网关自身漏洞族被在野利用。

### 7.1 CVE-2026-40217（已进 CISA KEV）
- **FACT（CISA KEV 条目）**：2026-11-18 加入 KEV，整改截止 **2026-12-02**；KEV 归类 "Unprotected Alternate Channel"；引用 advisory `GHSA-wxxx-gvqv-xp7p`。["https://cve.circl.lu/known-exploited-vulnerabilities-catalog/09a710b1-7e8c-4525-8d90-6257f3df1616"]
- **FACT（NVD）**：`/guardrails/test_custom_code` 通过 bytecode rewriting 执行任意代码；CVSS 3.1 **8.8**（AV:N/AC:L/**PR:L**/UI:N/S:U/C:H/I:H/A:H），CWE-420/94。["https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-40217"]
- **FACT（vendor advisory 转述）**：默认配置下需 **proxy-admin 凭据**；**1.83.11 修复**，手写沙箱替换为 RestrictedPython；X41 D-Sec 2026-02-13 报送，4-08 禁运到期，5-07 出公告。["https://i10x.ai/news/cve-2026-40217-litellm-guardrail-sandbox-escape"]
- **后果不是"一个洞"**：admin 凭据 → `LITELLM_MASTER_KEY` + 全部 provider key（OpenAI/Anthropic/Bedrock/Vertex）→ 在野 LLMjacking（烧额度、刷账单）；CISA 确认已利用，未标注勒索软件用途。
- **口径差异（须记）**：NVD 版本字段写 "through 2026-04-08"（日期式、无区间语义），vendor 说 1.83.11 修复——以 vendor advisory 为准。

### 7.2 同族三件（此前未入账）
- **CVE-2026-42271**：MCP test 端点（`/mcp-rest/test/tools/*`）spawn 用户可控子进程配置，无 command allowlist、无 admin 角色门 → 任意持 proxy key 者可在宿主执行命令；CVSS 8.7，影响 1.74.2–1.83.6，1.83.7 修；**KEV 2026-06-08**。
- **CVE-2026-48710（Starlette "BadHost"）**：<1.0.1 的 Host 头未校验（`/ ? # [ ]`），鉴权逻辑可被绕过 → 与 42271 组合成**未认证 RCE，CVSS 10.0**；SANS ISC 蜜罐在 **11-15/16** 观测到针对 `/mcp-rest/test/tools/list` 的探测，且攻击者已在做**变种字符绕过 PoC 过滤器**。["https://gridthegrey.com/posts/cve-2026-42271-litellm-rce-exploited-via-host-header-bypass/"]
- **CVE-2026-42208**：proxy API key 校验 SQLi（调用方 key 直接拼进查询），**未认证**、CVSS 9.8，1.81.16–<1.83.7，1.83.7 修。
- **CVE-2026-114612**：salt key 跨域复用（既封存密钥又签会话令牌）→ internal_user 提交伪造 admin 密文当 bearer，提权 proxy_admin 并经 MCP stdio 执行命令；1.91.0+ 默认可利用，1.87–1.90.x 需 `EXPERIMENTAL_UI_LOGIN=true`；1.100.4/1.101.3/1.102.2/1.103.1 修。
- **二手纠错**：FreeBuf 的"组合两漏洞可无认证 RCE"指的是 42271 + 48710（4–6 月线），**不是** 11-18 新进 KEV 的 40217（后者需 admin 凭据）。两条不要混。

### 7.3 判断
1. **供应链投毒与网关漏洞是同一资产的两条路径，共同点是凭据集中**：gateway 是"一把钥匙开全部模型"的位置，碰一次即全量交出。
2. **加固顺序**（按杠杆排序，不是按 CVSS）：① 网关不持有长期 provider key（外注凭据 / 短时令牌——与 Runtime 周 Substrate "零凭据执行 + egress PEP" 同构）；② 管理面与推理面网络/身份分离；③ 生产关闭管理测试端点（`/guardrails/test_custom_code`、`/mcp-rest/test/*`）；④ 版本 ≥1.83.11 **且** Starlette ≥1.0.1（只升一个，10.0 链仍在）。
3. **披露到 KEV 用 7 个月**（2-13 报送 → 4-08 禁运到期 → 5-07 公告 → 11-18 KEV）：vendor 公告不等于有人在打；KEV 才是"已经有人在打"的信号。这与 MCP 事件族里"策略存在 ≠ 策略生效"是同一类认识错误。

### 7.4 与项目连接
- **silver-shield**：LLM 网关应列入"凭据集中点"清单，检查项=是否持有长期 key、管理端点是否对外、Starlette 版本。
- **Tafcm / 本地边缘**：本地推理绕开了 gateway 的 key 集中，但同时引入本地控制面裸露（对照 Computer Use 周事件 22/24）——两条路都要"最小凭据 + 管理面不外露"。
- **TeamMind**：多 agent 运行时的模型网关属于运行时身份基线（R 层），网关凭据应短时、可吊销、可审计。

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
