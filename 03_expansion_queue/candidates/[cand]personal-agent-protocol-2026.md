# 候选对象证据卡 · Personal Agent Protocol（PAP/Poppy，Agent-to-Business 开放标准）

> 状态：`[cand]` ｜ 关联方向：Control 维度（Agent 身份/授权协议）｜ 日期：2026-10-21（兜底扫描捕获，领域外——非 Harness/治理深耕）

## 一句话定位
Sierra（Bret Taylor/Clay Bavor）与 Meta 牵头、Genesys/Shopify/Stripe/Walmart/Instinct/Rocket 共建的**个人 Agent 到企业系统的开放认证授权标准**：基于 OAuth，定义消费者 agent 如何发现企业能力、以访客会话行动、并在用户授予的只读/写权限内经企业网站或 API（MCP/OpenAPI）办事——填补 MCP（连工具）与 A2A（agent 互操作）之外的**第三块协议拼图：人→agent→企业的身份与授权**。

## 1. 它解决什么问题
- 个人 agent 走向商业落地（下单/客服/查询/办理）时，没有统一的"agent 代表我是谁、能干什么"的标准：企业无法识别来访 agent、无法区分访客与授权动作、无法审计
- 现有方案的缝隙：OAuth 解决人对应用的授权，不解决"用户的 agent 以最小权限访问企业"；MCP 解决工具连接，不解决跨企业的发现与授权；A2A 解决 agent 间通信，不解决消费者侧身份
- PAP 给出标准路径：企业发布 `/.well-known/poppy.json`（能力发现）→ agent 自标识（agent identity）→ 客户显式批准访问（read-only/write）→ 经企业既有 API 执行

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（2026-10-06 宣布）**：Sierra 联合创始人 Bret Taylor（OpenAI 前董事长）、Clay Bavor 公布 Personal Agent Protocol，Meta 及 Genesys、Instinct、Rocket、Shopify、Stripe、Walmart 为首批共建伙伴；基于 OAuth，支持 guest session 与用户授权的读写访问，底层可走企业网站/MCP/OpenAPI ["https://aicoder.com/news/news-20261007-sierra-meta-personal-agent-protocol-open-standard"]
- **FACT（2026-10-09 Poppy 草案）**：首版草案（昵称 Poppy）发布，企业发布 `/.well-known/poppy.json`、agent 自标识、客户批准访问的机制成型；v0.1 规范承诺 10 月内交付 ["https://openaimaster.com/personal-agent-protocol-explained/"]["https://www.metirai.com/blog/personal-agent-protocol-meta-sierra-agent-to-business-standard-2026"]
- **与已覆盖对象不重复**：MCP（工具/上下文连接，已建卡）、A2A（agent 间，已建卡）、MCP 2026-07-28 授权强化（RFC 9207/CIMD——服务端侧）；PAP 是**消费者侧 agent-to-business 身份与授权**的独立标准，且为支付/电商/电信等商业场景的落地协议（Stripe/Shopify/Walmart 站台即信号）

## 3. 与我的连接
- **连接的项目**：
  - campus_order（OpenClaw 智能体/高校点餐）：agent 代表用户下单的授权链路参照——PAP 是此类"agent 替用户办事"场景的标准范式
  - TeamMind（多 Agent 运行时）：多 agent 体系对外（企业/第三方系统）的身份层与最小权限授权设计
  - silver-shield：agent 自标识与显式授权可用于识别"冒充/越权"的 agent 行为
- **连接的知识点**：Control 维度新增**协议层 Agent 身份与授权**节点（与 MCP 信任边界、A2A 身份互通并列）；与 Harness 能力树 C 层（权限策略）相邻——PAP 是跨组织边界的授权，C 层是单 harness 内的权限
- **潜在收益**：为 Runtime/协议方向储备锚点；poppy.json 发现机制+显式授权可直接迁移到 campus_order/TeamMind 的对外交互设计

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | Sierra/Meta 宣布报道 ["https://aicoder.com/news/news-20261007-sierra-meta-personal-agent-protocol-open-standard"]；Poppy 草案解读 ["https://openaimaster.com/personal-agent-protocol-explained/"]；标准分析 ["https://www.metirai.com/blog/personal-agent-protocol-meta-sierra-agent-to-business-standard-2026"] |
| 证据等级 | FACT（多方报道+草案已发布；规范本体待 v0.1 正式交付） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | v0.1 规范 10 月内交付后：① 精读 poppy.json 字段与授权流程；② 对照 OAuth/MCP 授权机制画出差异；③ 试写一个最小 poppy.json 发现端点，验证 agent 发现→授权链路 |
| 预期完成时间 | 待 Runtime/协议方向深耕（或 v0.1 发布后周五验证） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
