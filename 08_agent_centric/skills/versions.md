# Skill Versions（tool_stats 数据驱动演进）

> 每次演进基于真实 usage_count / success_rate / failure_modes；样本不足或表现稳定不产生新版本。

## endpoint-discovery
### v1
- 演进理由：v1 基于工具实测（样本≥3）；工具按成功率重排
- 工具成功率：playwright=1.00
- 工具（重排后）：playwright, browser-use
- procedure: crawl 与被动收集 URL → normalize 归一化路径 → deduplicate 去重 → validate 探测有效性

## http-interaction
### v1
- 演进理由：v1 基于工具实测（样本≥3）；剔除 mcp(sr=0.00)；补 1 个失败检查步骤
- 工具成功率：playwright=1.00, mcp=0.00
- 剔除：mcp
- 工具（重排后）：playwright
- procedure: 构造请求 → 建立会话 → 执行并捕获响应 → 为该步骤设置超时与重试上限（mcp: timeout）

## evidence-collection
### v1
- 演进理由：v1 基于工具实测（样本≥3）；工具按成功率重排
- 工具成功率：promptfoo=1.00
- 工具（重排后）：promptfoo, otel-genai
- procedure: 捕获请求/响应 → 保存复现产物 → 链接到 finding

