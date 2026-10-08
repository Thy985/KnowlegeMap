# Skills（技能库 · How 层）

> Capability=What / Skill=How / Tool=With what / Project=来源。

## Endpoint Discovery Procedure（endpoint-discovery）
- purpose: 从目标中发现并确认有效端点/API
- trigger: 需要枚举 URL / API / 端点
- capability: endpoint-discovery
- procedure: crawl 与被动收集 URL → normalize 归一化路径 → deduplicate 去重 → validate 探测有效性
- required_tools: browser-use, playwright
- prerequisites: http-interaction

## Vulnerability Detection Procedure（vulnerability-detection）
- purpose: 检测漏洞并排除 false-positive
- trigger: 需要发现注入/越权/配置类漏洞
- capability: vulnerability-detection
- procedure: 加载授权测试基线 → 运行检测器 → 标记 candidate finding → 重放验证 false-positive
- required_tools: garak, playwright
- prerequisites: http-interaction

## Reconnaissance Procedure（reconnaissance）
- purpose: 测绘目标资产与暴露面
- trigger: 需要了解目标资产/服务/技术栈
- capability: reconnaissance
- procedure: 资产枚举 → 子域/服务发现 → 技术指纹识别
- required_tools: garak, browser-use
- prerequisites: -

## HTTP Interaction Procedure（http-interaction）
- purpose: 构造并执行 HTTP 会话
- trigger: 需要发请求/构造会话
- capability: http-interaction
- procedure: 构造请求 → 建立会话 → 执行并捕获响应
- required_tools: playwright, mcp
- prerequisites: -

## Request Replay Procedure（request-replay）
- purpose: 重放请求验证漏洞可复现性
- trigger: 需要复现/验证影响
- capability: request-replay
- procedure: 构造重放请求 → 注入 payload 重放 → 验证可复现与影响
- required_tools: playwright
- prerequisites: http-interaction

## Evidence Collection Procedure（evidence-collection）
- purpose: 收集并链接证据链
- trigger: 需要请求/响应/复现证据
- capability: evidence-collection
- procedure: 捕获请求/响应 → 保存复现产物 → 链接到 finding
- required_tools: otel-genai, promptfoo
- prerequisites: -

## Reporting Procedure（reporting）
- purpose: 生成可追溯评估报告
- trigger: 需要输出结论
- capability: reporting
- procedure: finding 分类 → 风险评级 → 给出修复建议
- required_tools: promptfoo
- prerequisites: evidence-collection

## Agent Memory Procedure（agent-memory）
- purpose: 沉淀任务经验供未来复用
- trigger: 任务完成后需要记忆
- capability: agent-memory
- procedure: 记录工具统计 → 提炼成功/失败模式 → 归档工作流版本
- required_tools: mem0
- prerequisites: -

