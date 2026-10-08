# Workflow v3 · security-assessment
goal: 对一个合法授权的网站执行安全测试，产出漏洞清单与证据链
evolution_reason: v1→v3
tools: garak, playwright, promptfoo

## stages
### stage-1 [目标测绘与暴露面识别]
- tools: garak
- depends_on: -
- checkpoint: 检查点：目标测绘与暴露面识别 产出物完整
- failure_recovery: 记录失败模式并继续
### stage-2 [端点/路径发现]
- tools: playwright
- depends_on: stage-1
- checkpoint: 检查点：端点/路径发现 产出物完整
- failure_recovery: 记录失败模式并继续
### stage-3 [HTTP 会话构造与请求执行]
- tools: -
- depends_on: stage-2
- checkpoint: 检查点：HTTP 会话构造与请求执行 产出物完整
- failure_recovery: 连接失败 → 指数退避重试 ≤3 次；会话过期 → 重建会话
### stage-4 [漏洞检测（注入/越权/配置）]
- tools: garak
- depends_on: stage-3
- checkpoint: 检查点：漏洞检测（注入/越权/配置） 产出物完整
- failure_recovery: 失败 → 缩小范围重试；标记 false-positive 候选待人工确认
### stage-5 [请求重放与回归验证]
- tools: playwright
- depends_on: stage-4
- checkpoint: 检查点：请求重放与回归验证 产出物完整
- failure_recovery: 记录失败模式并继续
### stage-6 [多工具结果归一化聚合]
- tools: promptfoo
- depends_on: stage-5
- checkpoint: 检查点：多工具结果归一化聚合 产出物完整
- failure_recovery: 记录失败模式并继续
### stage-7 [证据链收集（请求/响应/轨迹）]
- tools: promptfoo
- depends_on: stage-6
- checkpoint: 检查点：证据链收集（请求/响应/轨迹） 产出物完整
- failure_recovery: 证据缺失 → 标记判定为低置信并请求重放
### stage-8 [生成可追溯报告]
- tools: promptfoo
- depends_on: stage-7
- checkpoint: 检查点：生成可追溯报告 产出物完整
- failure_recovery: 生成失败 → 保留结构化中间结果

checkpoints: 8 ｜ agents: recon-specialist, vuln-detector, evidence-collector, reporter
