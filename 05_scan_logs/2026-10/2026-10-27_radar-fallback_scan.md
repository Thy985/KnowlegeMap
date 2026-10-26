# 兜底扫描日志 · 2026-10-27（Personal Tech Radar · 轻量全领域兜底）

> 定位：当前深耕领域（Runtime）之外的重大突发事件安全网；刻意做得很轻，绝大多数天 No Action。

## 扫描范围
全领域轻量两路（安全重大事件 / 协议框架重大变更）+ 一次定向精读（本周 AI 安全周报）。

## 发现与判定

### 建卡 1 张（A 级，领域外）：`[cand]litellm-double-supply-chain-2026-10.md`
**LiteLLM 双重供应链投毒（2026-10-21/22）**——全新对象，领域外 A 级重大事件：
- v1.107.0 的 7 个编译 wheel 植入 credential stealer + RCE 后门（Python startup hooks，任意进程启动即激活）；GitHub 源码与 sdist 干净；被盗 GitHub CLI token → 恶意 workflow → PyPI + Docker 镜像发布，约 2 小时暴露
- 48 小时内**第二起独立攻击**（gateway 日志泄露 GitHub token → 第二个恶意包）——两家独立攻击者一周内先后得手
- 微软 Defender（10-23）与 Datadog（10-21）独立取证
- 意义：LLM 网关=企业 AI 栈负载组件，供应链投毒从"工具链"升级到"推理中枢"；对 silver-shield/TeamMind 供应链加固有直接教育价值

### 记日志不建卡（A 级信号并入已有对象 + B 级背景）
- **ARTEX AI agents 国家级战役（10-22，A 级领域外）**：中国关联 APT 将自定义 offensive AI agent 部署进 **ConnectWise MSP 供应链** + 日本制造业，自主侦察/凭据收集/数据外渗（初始访问后无人引导）——**两周内第二个确认的 AI agent 主要进攻工具国家级战役**（上一为 OpenAI 1200 agents 10-20）。属已有对象「Agentic Attack 范式事件」的重大新增战役，**并入该认知不新建卡**；去重基准对应条目已追加。
- **OpenCode sign-in MCP RCE（10-22，B 级增量）**：恶意 MCP 服务器在开发者登录 Windows/WSL 时执行任意代码（无需后续交互）——OpenCode 已覆盖（10-17 泄露），追加认知。
- **Proofpoint 行为检测失效趋势（10-23，B 级背景）**：生成式 AI 系统性消除攻击流量行为特征——十年行为检测体系加速失效。
- **Capcom 1170 万账号泄露（10-22）**：普通企业数据泄露，B 级背景。
- 已覆盖命中（不重复）：php2shell（10-21）、OpenAI GPT-6 监控对抗（10-20）、Anthropic 越权（10-09）、MCP 2026-07-28 spec/A2A 加入 AAIF（10-01，治理普通增量）。

## 文件变更
- **新建** `03_expansion_queue/candidates/[cand]litellm-double-supply-chain-2026-10.md`（A 级）
- **修改** `06_expansion_index/README.md`（新增 2026-10-27 兜底段 + 去重基准追加 LiteLLM + Agentic Attack 条目追加 ARTEX）
- **修改** `_INDEX.md`（追加本日志行）
- **新建** `05_scan_logs/2026-10/2026-10-27_radar-fallback_scan.md`（本日志）

## 结论
**New**（LiteLLM 双重供应链投毒 A 级新卡——领域外重大突发事件，一手证据充分）
