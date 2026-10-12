# 候选对象证据卡 · Protocol Pivoting（MCP 跨协议信任攻击范式 + mcp-safeguard 扫描器）

> 状态：`[cand]` ｜ 关联方向：MCP / Agent 安全（非当前深耕领域，由 06:00 兜底扫描捕获）｜ 日期：2026-10-13（兜底）

## 一句话定位
独立研究员 Syed Anas Mohiuddin 用"同一 SSRF 缺陷跨 5 个无代码/行业/国家关联的组织"证明 **MCP 协议信任模型存在结构性缺陷**，并定义 **Protocol Pivoting（协议转轴）**——经一种协议进入、利用协议间信任假设升级到另一协议能力的攻击范式；配套开源黑盒扫描器 **mcp-safeguard**。

## 1. 它解决什么问题
- **结构性缺陷实证**：五组织各自安全团队确认并修复同一 SSRF——
  - **Google**：CVE-2026-14540（mcp-toolbox 0.3.0–1.4.0，HTTP 源/工具无重定向限制、不校验目标 IP，CVSS **8.0 High**；PR #3448 引入 **SSRFGuard** 防 DNS-rebinding、allowPrivateNetworks/allowedIpRanges、启动时校验 BaseURL，v1.5.0 修复）
  - **JPMorgan Chase**：jpmorgan-payments/ai 文档搜索 MCP 的 related() 工具服务端无限制抓取调用方 URL（medium）
  - **Weaviate**：Google module apiEndpoint/region 限制为 Google API 主机
  - **法国 DINUM**：datagouv/datagouv-mcp PR #126（machine_documentation_url 可指向回环/私网/云元数据，连接时校验 IP、逐跳重定向复查、拒绝代理）
  - **印尼 Tangerang 市政府**：Wazuh-MCP-Server GHSA（09-03 High，SSRF 防护只拒字面 IP 不解析主机名）
- **两个失效模式**：① SSRF——MCP server 用 agent 提供的 URL/路径构造出站请求且不校验解析目标；② 上游数据不安全处理——完整上游 API 响应无脱敏写入集中日志（普通错误即可触发）
- **根本假设崩塌**："跨 MCP 边界的数据因来自系统内部即可信"——在 agentic 管道中不成立；依赖/SCA 扫描器漏检（危险输入作为 tool argument 经 manifest 到达，调用图止于传输边界）
- **Protocol Pivoting 定义**：MCP tool output 中嵌入形如 A2A 任务指令的文本 → orchestrator 当正常委托传给 subagent → subagent 信任 orchestrator 而执行；预印本（Zenodo 2026-05-24）含三场景：MCP→A2A 隐式信任委托提权、A2A→MCP 恶意 agent 冒充能力注入、跨协议 prompt injection 链

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：GitHub Advisory Database / NVD CVE-2026-14540（07-31 发布/08-08 更新）、Rapid7 CVE-2026-97228（GraphQL 注入，Low 2.7，v0.6.2 参数化修复）、各组织修复 PR 均可核验；Unite.AI 2026-10-05 报道（注明 AI 生成、编辑审核）；研究员 10 月更新《Protocol Pivoting, four months later》
- **规模**：16 个维护方发布的 GHSA 归功其发现（SSRF/命令注入/认证缺口/会话劫持/凭据泄露/修复绕过），修复合并入 github-mcp-server / mongodb-mcp-server / salesforce-mcp-server
- **未决**：5 个美国联邦 MCP server（VA/CMS Blue Button/regulations.gov/USASpending/CDC PLACES）仍在 triage 未修（VA 案例可能把老兵 SSN/DOB/地址写入 ERROR 日志）；10-23 MCPCon North America（San Jose）将公开演讲
- **新颖点**：与既有 MCP 安全记录（统计 41-50% 组织受困、供应链 CHAINDROP）不同——这是**协议级信任边界缺陷的跨组织实证 + 跨协议攻击范式命名**

## 3. 与我的连接
- **连接的项目**：**silver-shield**（威胁检测项需加入"跨协议信任/SSRF 面"）；**dsh-pentest**（MCP/A2A 攻防演练用例）；**TeamMind**（A2A 多 agent 委托必须保留来源/授权，不能信任 orchestrator 传递的任意指令）；**Tafcm**（本地 MCP server 出站请求默认私网拒绝）
- **连接的知识点**：MCP 信任模型、A2A 委托、Agent 安全、五维模型 Control 维度
- **潜在收益**：① **mcp-safeguard 可直接对自建/集成的 MCP server 做黑盒六类检查**（SSRF/过度权限/prompt injection/信息泄露/认证缺口/生命周期绕过）；② Google SSRFGuard 是"真实 SSRF 防护参考实现"；③ 给"跨协议来源追踪 + 显式授权"提供规格依据

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | https://www.unite.ai/researcher-discloses-same-mcp-flaw-at-google-jpmorgan-two-governments/ ；CVE-2026-14540（GitHub Advisory Database）；Zenodo 预印本（2026-05-24）；mcp-safeguard 开源仓库（待定位） |
| 证据等级 | **FACT**（CVE/GHSA/修复 PR/多组织独立确认） |
| 验证方式 | ① 用 mcp-safeguard 对一个本地 MCP server 跑黑盒扫描，验证六类检测；② 精读 Google SSRFGuard 实现（PR #3448），对照 Tafcm/TeamMind 的出站请求处理；③ 精读 Zenodo 预印本三场景，为 silver-shield 补检测规则 |
| 预期完成时间 | 2026-11 月 MCP 安全/治理周（非本周——本周深耕 Evaluation，本卡仅记录不展开） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
