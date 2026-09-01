# 候选证据卡 · [cand] E2B 沙箱 + Agentic Provisioning Protocol（Firecracker microVM）

> 状态：`[cand]` ｜ 分类：代码沙箱 / Agent 执行域（B11） ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
E2B 是基于 Firecracker microVM 的开源 Agent 代码沙箱，提供真硬件虚拟化隔离；其"Agentic Provisioning Protocol"（与 Stripe Projects 合作）让 Agent 能自主发现/开通/鉴权安全执行环境——这是 Agent 执行域与权限的成熟解法。

## 1. 它是什么 / 解决什么问题
- **E2B**：开源沙箱运行时，每个沙箱 = Firecracker microVM（AWS Lambda 同款 hypervisor），"模型代码无法逃逸到宿主机"；支持长会话（Pro 24h）、自定义模板、SDK/API/MCP 集成；2025-07 完成 $21M A 轮（Insight Partners）["https://e2b.dev/?s=09"]["https://github.com/e2b-dev/E2B"][https://hokai.io/hub/tools/e2b]
- **隔离技术谱系**：gVisor（用户态假内核，~100ms 启动，50-80% syscall 性能）vs Firecracker（微 VM，~125ms，95%+）vs Kata Containers（~200ms）["https://juejin.cn/post/7655523967743557651"]
- **Agentic Provisioning Protocol**：Stripe Projects 作为信任层，Agent 通过标准协议发现/开通/鉴权 E2B 沙箱并拿到凭据，无需人碰控制台["https://e2b.dev/blog/e2b-sandboxes-are-now-available-through-stripe-projects"]
- 已接入 OpenAI Agents SDK；安全事件 CVE-2026-31431（Copy Fail）不受影响（自定义最小内核未编入相关模块）["https://e2b.dev/blog/not-affected-by-copy-fail-heres-why"]

## 2. 与我的知识/项目关系
- **EP-002「Permission Is Security Boundary」**：E2B 是"执行域隔离"的现成工程答案
- **TeamMind**：多 Agent 需要安全执行子进程 → 沙箱化执行域
- **dsh-pentest**：渗透 agent 必须沙箱，PentAGI 也走 Docker 沙箱路线
- **silver-shield**：规则引擎/事件流的可审计执行环境可参考

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（官方 + 生态多源） |
| 来源 | https://e2b.dev/ ｜ https://github.com/e2b-dev/E2B ｜ https://e2b.dev/blog/e2b-sandboxes-are-now-available-through-stripe-projects |
| 验证方式 | 本地跑一次 E2B SDK 沙箱执行（无 API key 用自托管或最小 demo）→ 评估与 gVisor/Daytona 对比 |
| 预期 | 2026-09/10 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
