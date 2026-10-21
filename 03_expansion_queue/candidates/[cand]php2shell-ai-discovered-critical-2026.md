# 候选对象证据卡 · php2shell：AI 工具发现 PHP 潜伏十年关键漏洞（2026-10 基础设施级事件）

> 状态：`[cand]` ｜ 关联方向：AI Infra / 安全（AI-for-Security 里程碑 + Web 基础设施）｜ 日期：2026-10-22（兜底扫描捕获，领域外）

## 一句话定位
PHP 语言两处潜伏超十年的**无认证远程 RCE** 漏洞（CVE-2026-109618/109619，合称 "php2shell"），由安全公司借助**谷歌与 OpenAI 旗下 AI 工具发现**，2026-10-21 PHP Foundation 发布紧急补丁、NSA 紧急警告、全球多国政府网站下线——既是近十年来最严重 Web 基础设施漏洞事件，也是 **AI 辅助漏洞挖掘首次命中全球级关键基础设施** 的标志性案例。

## 1. 它解决什么问题
- **对生态**：PHP 支撑全球约 70%（Fortune 口径）/75%（华尔街见闻口径）网站与大量 CMS（含 WordPress）；两漏洞"直接通向服务器文件系统或数据库"、无认证即可远程接管服务器，攻击者无需密码即可控制 web server
- **对 Agent 工程实践**：证明 **AI 工具（Google/OpenAI 系）在漏洞发现上已具备国家队级产出**——AI-for-Security 从"辅助审计"跃迁到"发现潜伏十年 0day"；同时"AI 修复与 AI 攻击同速"（Fortune 指出补丁发布即面临 AI 黑客利用竞速）——agent 安全研究同时要关注 AI 防御侧能力曲线与 AI 武器化利用侧的竞速
- **对用户项目**：用户画像含 PHP 靶场/CTF（弱类型、SQL 注入、assert 注入训练环境）——本事件是 PHP 安全训练素材的最高时效真实案例；也是 silver-shield（反诈骗判定）之外"Web 基础设施威胁模型"的增量输入

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（PHP Foundation 官方，2026-10-21）**：发布紧急安全更新修复两处 "php2shell" 关键漏洞，称其为"非常非常严重"，呼吁"所有 PHP 用户立即更新" ["https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/"]
- **FACT（NSA 官方警告，2026-10-21）**：NSA 声明漏洞"常提供直达服务器文件系统或数据库的路径"，无法及时打补丁的组织应下线系统；荷兰/法国/丹麦/芬兰多国政府网站与 BBC 紧急下线 ["https://www.france24.com/en/live-news/20261021-websites-go-dark-worldwide-as-ai-exposes-critical-security-flaws"]；BBC 报道（10-21）["https://1lq1mek.mask.com.ua/video/newsfeed/2026/10/21/macrons-surprise-solidarity-visit-to-saudi-arabia"]
- **FACT（CVE 编号，10-21）**：CVE-2026-109618 + CVE-2026-109619；发现者=美国网络安全公司借助 Google/OpenAI AI 工具；华尔街见闻/今日头条中文报道同细节（10-21 22:58）["http://m.toutiao.com/group/7699135630558773803/"]
- **发现时间线**：报告先于官方补丁发布流出（Fortune 提到 opportunists 借势），10-21 下午补丁发布、同日晚全球下线潮
- **与已覆盖对象不重复**：去重基准中无 PHP 语言层漏洞/无 AI-for-Security 漏洞发现事件（agentic-attack 卡为 agent 攻击侧，本卡为语言基础设施漏洞 + AI 防御/发现侧，机制不同）

## 3. 与我的连接
- **连接的项目**：
  - dsh-pentest（PHP 靶场/CTF 训练）：php2shell 是"真实 PHP 漏洞如何被 AI 发现"的第一手教学案例，可作为 PHP 安全训练环境的最新威胁模型输入
  - silver-shield（反诈骗判定）：与"AI 能力被武器化"（AI 黑客竞速利用）同源风险信号的又一实证
  - campus_order / TeamMind：任何 PHP 后端部署的 patch 优先级与下线预案参考
- **连接的知识点**：AI-for-Security 能力曲线（发现→利用竞速）；AI Infra / 本地边缘（Tafcm 周）的"Web 基础设施依赖面"；威胁模型 E 层外部依赖攻击面
- **潜在收益**：① 用户 PHP 学习/靶场的最新真实漏洞教材；② 为"AI 能发现也能攻击"的 Agent 安全叙事提供基础设施级证据；③ 补 AI Infra 周的前置锚点

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | Fortune（CVE 编号+php2shell+70% 口径）["https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/"]；France24（NSA 原话+多国下线）["https://www.france24.com/en/live-news/20261021-websites-go-dark-worldwide-as-ai-exposes-critical-security-flaws"]；华尔街见闻（Google/OpenAI AI 发现细节）["http://m.toutiao.com/group/7699135630558773803/"]；HyperAI 摘要 ["https://hyper.ai/en/stories/c344635e541c5f19aab9064386a9d9d4"] |
| 证据等级 | FACT（多方独立：金融媒体+国际媒体+中文财经+聚合源，核心事实一致） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | 待补：① 查 PHP 官方 Release 页确认补丁版本与 CVE 详情；② 若用户 PHP 靶场环境可复现，构造最小触发验证（按官方披露机制）；③ 追踪后续利用/补丁覆盖情况一周 |
| 预期完成时间 | 2026-10-25（本轮周内跟进；不阻塞 Harness 周主线） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
