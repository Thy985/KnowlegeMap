# 候选对象证据卡 · Langflow 双 9.8 未授权漏洞（AI 编排平台的「功能即执行面」）

> 状态：`[cand]` ｜ 分类：AI 安全（G1）/ AI 平台供应链 ｜ 发现：2026-11-23（兜底补漏；CVE 发布于 2026-10-29）｜ 等级：**A**

## 一句话定位
主流开源 AI agent / 工作流编排器 **Langflow** 的 **1.0.0–1.12.8 全部版本**存在两个 CVSS **9.8** 未授权漏洞（认证绕过 CWE-287 + 代码生成失控 CWE-94），公网可达即可以无账号身份取得"能生成并执行代码"的平台控制权，**只有 1.13.0 修复、官方未给 workaround**；其根因不是边角缺陷，而是"平台本职工作就是执行生成代码"。

## 1. 它解决什么问题 / 为什么是问题
- AI 编排层（agent builder / workflow builder）正被大量组织当作"内部工具"快速上线，安全审查标准低于传统生产系统，却常直接监听网络。
- 一旦认证被绕过，攻击者拿到的不是一个只读面板，而是**一个设计上就要执行任意生成代码的执行面**——这是 Langflow 这类产品的核心功能，不是可选插件。
- 同类通病可对照：pandas-ai `Agent.chat` 默认 `sandbox=None` 直接把 LLM 生成代码送 `exec`（CVE-2026-51898）；「AI 编排层的默认配置 = 代码执行」是品类级问题。
- 对防御方的实际含义：补丁之外必须回答三个问题——是否暴露公网 / 认证是否唯一屏障 / 生成代码是否默认沙箱化。

## 2. 为什么现在值得关注（一手证据）
- **FACT（NVD，2026-10-29 发布）CVE-2026-93680**：IBM Langflow OSS `1.0.0` 至 `1.12.8`（配置区间 `<1.13.0`）** improper authentication（CWE-287）**，CVSS 3.1 **9.8**（`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`），远程无账号可绕过安全限制；CISA SSVC：`automatable=yes`、`technicalImpact=total`、`exploitation=none`（截至 10-30）。["https://nvd.nist.gov/vuln/detail/cve-2026-93680"]["https://www.ibm.com/support/pages/node/7294467"]
- **FACT（NVD，同日）CVE-2026-110186**：同版本区间，**improper control of code generation（CWE-94）**，CVSS **9.8**，同向量，远程无账号可执行任意代码。["https://nvd.nist.gov/vuln/detail/cve-2026-110186"]
- **FACT（Rapid7 Metasploit，2026-10-23）**：一次发布 **6 个模块**指向 Langflow——1 个认证绕过（CVE-2026-93680）+ 3 个未授权 RCE（CVE-2026-0768 / 0769 / 10134）+ 2 个已认证代码执行（7873 / 93674），覆盖 1.0.0–1.11.4。["https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-langflow-mongodb-and-more/"]
- **FACT（工具能力边界，2026-11-02 复核）**：CVE-2026-93680 的 Metasploit 模块是 `auxiliary/gather`，作用是**无凭据连上 MCP 端点并枚举工具**，**不执行代码**；因此"公网一键 RCE"不成立，"公网可无账号探测并取得立足点"成立。["https://www.rescana.com/post/langflow-oss-cve-2026-93680-110186-unauthenticated-critical-prepare-now"]
- **FACT（PyPI 版本线）**：1.13.0 于 **2026-10-23** 发布（修复线起点），1.13.1 于 11-04，**1.13.3 于 11-18（当前最新）**。["https://pypi.org/project/langflow/"]
- **FACT（历史 KEV 面）**：CISA KEV 中已有 Langflow 条目（可见 CVE-2025-3248 缺认证、CVE-2025-34291 CORS+SameSite 凭据跨域、CVE-2026-33017 未授权构建 flow 的代码注入）。["https://www.cisa.gov/known-exploited-vulnerabilities-catalog"]
- **未核（二手）**：乌干达 CERT 称 KEV 中共有 **6 个** Langflow CVE（最近一条 8 月），我只逐条核对到 3 条；Aviatrix 称第三个漏洞可让低权用户借 Agentic Assistant 在服务端执行 OS 命令；两家均未给出该两条新 CVE 的"在野利用"一手证据。

## 3. 与我的连接
- **连接的项目**：
  - silver-shield：新增检测项——"AI 编排/工作流平台暴露面"（无认证的管理/执行端点、默认沙箱关闭、公开 exploit 模块可枚举）。
  - TeamMind / campus_order：平台选型清单加三条硬问（默认沙箱？认证是否唯一屏障？是否有公开 exploit 工具链？）。
  - Tafcm：本地部署同类平台时，默认 `localhost` 绑定与独立 profile/账户，不沿用共享管理员态。
- **连接的知识点**：
  - `[cand]agent-containment-breach-2026` 第四类「控制面配置缺失 / 默认不安全」——Langflow 是**平台自身的功能即执行面**，比 Archon 的默认 0.0.0.0 无认证更根本。
  - `[cand]litellm-double-supply-chain-2026-10` 网关漏洞族——同为"AI 中间层成为 CVE 面"，但 Langflow 的风险来自**设计功能**而非沙箱实现瑕疵。
  - 本周 Computer Use 能力树 E 层（本地控制面）与 F 层（不可信输入）——认证绕过 + 代码生成 = 输入侧与执行侧同时失守。
- **潜在收益**：给"AI 平台默认安全"一条可复用判据：**能执行生成代码的平台，认证不是边界、沙箱才是**；这条判据可直接落到 silver-shield 的规则与 campus_order 的部署清单。

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | NVD 两条 CVE（含 IBM PSIRT 引用）+ IBM 安全公告 node/7294467 + Rapid7 Metasploit 模块清单 + PyPI 版本线 + CISA KEV 目录 |
| 证据等级 | FACT（CVE 编号、CVSS、版本区间、修复版本、Metasploit 模块均一手核验）；DESIGN（品类级判据"认证不是边界、沙箱才是"） |
| 验证方式 | ① 静态：读 `auxiliary/gather/langflow_auth_bypass_cve_2026_93680.rb` 确认其只做 MCP 工具枚举（不实跑）；② 结构：核对 1.13.0 变更日志中认证与 sandbox 相关修复；③ 若后续有本地需求，再在隔离网络起 1.12.8 容器复现（本轮不做） |
| 预期完成时间 | 本轮仅完成静态核验；实跑不排期（非当前项目依赖） |

## 5. 验证结果
<!-- 待回填 -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（等 1.13.x 修复细节与是否有在野利用的一手确认）
- [ ] 拒绝（原因）
