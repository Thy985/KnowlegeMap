# Agent Task Expansion：对一个合法授权的网站执行安全测试，产出漏洞清单与证据链
task_type=security-assessment risk=high approval_required=True

## 1. Required Capabilities（任务→能力分解）
reconnaissance, endpoint-discovery, http-interaction, vulnerability-detection, request-replay, result-aggregation, evidence-collection, reporting
_未知能力发现（目标解析）_：vulnerability-detection

## 2. Capability Gap（已有 vs 需求）
missing: reconnaissance, endpoint-discovery, vulnerability-detection, request-replay, http-interaction, evidence-collection, reporting

## 2.1 Capability Tree（任务动态实例化 · JIT 展开）
```
Web Security Assessment（root.security-assessment）
├── Reconnaissance ❌ conf=0.00
│   ├── Asset Discovery ❌ → garak
│   ├── Subdomain Discovery ❌ → garak
│   ├── Service Discovery ❌ → garak
│   └── Technology Fingerprinting ❌ → garak
├── Web Mapping ❌ conf=0.00
│   ├── URL Discovery ❌ → playwright
│   ├── Endpoint Discovery ❌ → playwright
│   ├── API Discovery ❌ → playwright
│   └── JavaScript Analysis ❌ → playwright
├── Vulnerability Assessment ❌ conf=0.00
│   ├── Injection ❌ → garak
│   ├── Authentication ❌ → garak
│   ├── Authorization ❌ → garak
│   ├── XSS ❌ → garak
│   └── SSRF ❌ → garak
├── Validation ❌ conf=0.00
│   ├── Request Construction ❌ → mcp
│   ├── Payload Generation ❌ → garak
│   ├── Reproduction ❌ → playwright
│   └── Impact Verification ❌ → playwright
├── Evidence ❌ conf=0.00
│   ├── Request/Response Capture ❌ → promptfoo
│   ├── Reproduction Artifact ❌ → promptfoo
│   └── Evidence Linking ❌ → promptfoo
├── Reporting ❌ conf=0.00
│   ├── Finding Classification ❌ → promptfoo
│   ├── Risk Assessment ❌ → promptfoo
│   └── Remediation ❌ → promptfoo
```

## 3. Tool Discovery（能力驱动，非关键词驱动）
- reconnaissance: garak, pyrit, browser-use, webwright
- endpoint-discovery: browser-use, webwright, playwright
- http-interaction: mcp, browser-use, playwright
- vulnerability-detection: garak, pyrit, owasp-agentic-security
- request-replay: playwright, browser-use, webwright
- result-aggregation: promptfoo, langfuse, agentevals
- evidence-collection: otel-genai, langfuse, promptfoo
- reporting: promptfoo, langfuse

## 4. Tool Composition（组合理由）
工具链：garak -> playwright -> mcp -> promptfoo
- **garak**  fit=0.780  task_fit=1.0 coverage=0.25 auto=0.9 structured=0.9 reliability=0.75 eco=0.8
  - 理由：适配 1.00，覆盖 0.25，CLI 原生/结构化输出，agent 可直接调用；安全影响：仅授权目标使用；；权限=target-auth（授权）；风险=仅授权目标使用
- **playwright**  fit=0.725  task_fit=0.7 coverage=0.25 auto=0.9 structured=0.9 reliability=0.85 eco=0.9
  - 理由：适配 0.70，覆盖 0.25，CLI 原生/结构化输出，agent 可直接调用；安全影响：需沙箱防滥用；；权限=local-process；风险=需沙箱防滥用
- **browser-use**  fit=0.723  task_fit=0.7 coverage=0.38 auto=0.95 structured=0.85 reliability=0.7 eco=0.75
  - 理由：适配 0.70，覆盖 0.38，CLI 原生/结构化输出，agent 可直接调用；安全影响：需授权范围约束；；权限=local-process；风险=需授权范围约束
- **promptfoo**  fit=0.738  task_fit=0.6 coverage=0.38 auto=0.95 structured=0.95 reliability=0.85 eco=0.9
  - 理由：适配 0.60，覆盖 0.38，CLI 原生/结构化输出，agent 可直接调用；；权限=local-run；风险=none
- **mcp**  fit=0.646  task_fit=0.5 coverage=0.12 auto=0.95 structured=0.95 reliability=0.85 eco=0.9
  - 理由：适配 0.50，覆盖 0.12，CLI 原生/结构化输出，agent 可直接调用；安全影响：MCP03 Tool Poisoning / Supply Chain（AST↔MCP）；；权限=tool-scope；风险=MCP03 Tool Poisoning / Supply Chain（AST↔MCP）
**排除候选**：
- browser-use：与 playwright 语义重叠（互斥组 ['browser-use', 'playwright', 'webwright']），fit 0.723 < 0.725
**数据流缺口**（需转换环节）：
- garak->playwright: 数据流不兼容：garak(structured) → playwright(script)，需要转换环节（记录为设计缺口）
- playwright->mcp: 数据流不兼容：playwright(structured) → mcp(tool-schema)，需要转换环节（记录为设计缺口）
- mcp->promptfoo: 数据流不兼容：mcp(structured) → promptfoo(config)，需要转换环节（记录为设计缺口）

## 5. Workflow
v4（v1→v4）
- stage-1 [目标测绘与暴露面识别] tools=['garak'] dep=-
  - checkpoint: 检查点：目标测绘与暴露面识别 产出物完整
  - recovery: 记录失败模式并继续
- stage-2 [端点/路径发现] tools=['playwright'] dep=['stage-1']
  - checkpoint: 检查点：端点/路径发现 产出物完整
  - recovery: 记录失败模式并继续
- stage-3 [HTTP 会话构造与请求执行] tools=['mcp'] dep=['stage-2']
  - checkpoint: 检查点：HTTP 会话构造与请求执行 产出物完整
  - recovery: 连接失败 → 指数退避重试 ≤3 次；会话过期 → 重建会话
- stage-4 [漏洞检测（注入/越权/配置）] tools=['garak'] dep=['stage-3']
  - checkpoint: 检查点：漏洞检测（注入/越权/配置） 产出物完整
  - recovery: 失败 → 缩小范围重试；标记 false-positive 候选待人工确认
- stage-5 [请求重放与回归验证] tools=['playwright'] dep=['stage-4']
  - checkpoint: 检查点：请求重放与回归验证 产出物完整
  - recovery: 记录失败模式并继续
- stage-6 [多工具结果归一化聚合] tools=['promptfoo'] dep=['stage-5']
  - checkpoint: 检查点：多工具结果归一化聚合 产出物完整
  - recovery: 记录失败模式并继续
- stage-7 [证据链收集（请求/响应/轨迹）] tools=['promptfoo'] dep=['stage-6']
  - checkpoint: 检查点：证据链收集（请求/响应/轨迹） 产出物完整
  - recovery: 证据缺失 → 标记判定为低置信并请求重放
- stage-8 [生成可追溯报告] tools=['promptfoo'] dep=['stage-7']
  - checkpoint: 检查点：生成可追溯报告 产出物完整
  - recovery: 生成失败 → 保留结构化中间结果
_复用历史工作流（similar task history（对一个合法授权的网站执行安全测试，产出漏洞清单与证据链 v1））_

## 6. Evaluation
score=0.887 failure=[false-positive-rate:2 个 false-positive 候选] reproducibility=0.7
- garak 检出 17/18 已知漏洞 (EXPERIMENT): garak 检出 17/18 已知漏洞 | criterion=detection-accuracy score=0.92 failure=none
- playwright 重放验证 3 个候选 (EXPERIMENT): playwright 重放验证 3 个候选 | criterion=false-positive-rate score=0.85 failure=2 个 false-positive 候选
- promptfoo 证据链完整 16/18 (EXPERIMENT): promptfoo 证据链完整 16/18 | criterion=evidence-completeness score=0.88 failure=none
- 两次运行结果一致 (EXPERIMENT): 两次运行结果一致 | criterion=reproducibility score=0.9 failure=none
- task-run (EXPERIMENT): [false-positive-rate:2 个 false-positive 候选] 

## 7. Memory Update
run_id=task-demo-security-4；工具统计/工作流版本/失败模式已回写 Agent Operational Memory

---
证据纪律：所有工具/能力锚点见 03_expansion_queue/candidates + 00_bootstrap/00_starred_reference.md（FACT 优先）。