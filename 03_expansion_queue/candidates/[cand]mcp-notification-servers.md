# 候选证据卡 · [cand] MCP 通知类 Server（对接 agent-attention）

> 状态：`[cand]` ｜ 关联方向：Top20 #1 + Project（agent-attention） ｜ 日期：2026-09-01

## 一句话定位
MCP 生态已出现一批"桌面通知"server（Windows toast / 跨平台音效 / 弹窗交互），与我的 `agent-attention` 项目定位高度重叠，是现成的参考实现与潜在的改造方向。

## 1. 它解决什么问题
- 让 AI Agent 完成长任务后主动通知用户（toast/声音/弹窗），把 Agent 从"静默后台"变成"桌面可见"。
- 与 `agent-attention` 解决的"Agent → 通知基础设施"是同一类问题。

## 2. 为什么现在值得关注（活跃度证据）
- 多个相关项目 2026-07/08 仍在更新：mcp-win-toast（Windows toast+对话框，2026-08-29 更新）、mcp-notifications（Go，跨平台，WSL 回退 Windows toast，2026-08-30 更新）、Notification MCP（跨平台音效，2026-08-30）、Popup MCP（Tauri+Vue 弹窗，2026-08-31）["https://github.com/ShigeruWakida/mcp-win-toast"]["https://github.com/angelcervera/mcp-notification/"]["https://github.com/pinkpixel-dev/notification-mcp"]["https://lobehub.com/mcp/chietears-popup-mcp"]
- 腾讯云 MCP 市场亦收录同类通知 server，说明进入主流生态目录["https://cloud.tencent.com/developer/mcp/server/11340"]

## 3. 与我的连接
- **连接的项目**：`agent-attention`（Windows Agent 通知基础设施：agent-notify → daemon → Toast/托盘/Center）——**直接同域**
- **连接的知识点**：Tool System / Agent 对外可见性 / Permission（通知属低风险可逆动作）
- **潜在收益**：① 把 agent-attention 改造成/兼容 MCP 通知 server，让任意 MCP 客户端（Claude/Cursor/Codex）直接复用；② 直接借鉴 mcp-win-toast / mcp-notifications 的 Windows toast 实现；③ 反哺"Agent 如何主动触达人类"的工程知识

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | mcp-win-toast、mcp-notifications、mcp-windows-notify、Notification MCP（GitHub） |
| 证据等级 | FACT（仓库 + 更新日志） |
| 验证方式 | 对照 agent-attention 现有架构，产出"改造为 MCP server"的设计方案（是否新增 `notifications/listen` 订阅） |
| 预期完成时间 | 2026-09 内 |

## 5. 关键观察
- 生态解法高度趋同：`send_notification(title, message)` + `play_sound` + 跨平台 fallback。
- 与 MCP 2026-07-28 的 `subscriptions/listen`（按通知类型订阅）可直接衔接——agent-attention 的 Center/事件模型可映射为订阅流。
- 差异化机会：现有实现多为"纯通知"，agent-attention 有聚合 Center + 历史事件，可做"通知中心型" MCP server。

## 6. 决策
- [ ] 晋升 validated（需先完成架构对照设计）
- [x] 维持观察（与 agent-attention 的改造决策绑定）
- [ ] 拒绝
