# 候选对象证据卡

> 状态：`[cand]` ｜ 关联方向：AI 安全（G1）/ 供应链信任边界 ｜ 日期：2026-11-24

## 一句话定位
微软官方 Agent Framework 的 PyPI 元包 1.26.1 / 1.26.2 被非授权发布，靠 `.pth` 启动钩子在**每次 Python 解释器启动时**执行凭据窃取器——不是框架漏洞，而是**注册表作为执行面**：合法包名 + 合法依赖 + 不 import 也会执行。

## 1. 它解决什么问题
此类事件暴露的不是某个 CVE 的补丁问题，而是三条工程假设同时失效：
- **"官方包名 = 可信来源"**：包身份是注册表给的，不是代码给的；
- **"不 import 就安全"**：`.pth` 在 site 初始化阶段执行，`pip` 自身启动也会触发，依赖扫描/`import` 前检查全部失效；
- **"删包即清除"**：恶意 wheel 一旦被 CI / 容器 / venv 解析过，凭据已经外发，回滚包不等于回滚后果。
对本仓的直接含义：Harness/Runtime 周的"动作门控 / 判定依据外部 / 回执可核验"三判据，在**制品供应链**这一侧同样成立——需要"发布事件可核验（谁在什么时间用什么凭据发布了什么）"，而不只是"commit 可核验"。

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **时间线**（多源交叉一致，Wiz / StepSecurity / PyPI / GitHub Advisory）：1.26.0 于 2026-11-12 发布（最后干净版）→ **1.26.1 于 11-17 20:35 UTC** → **1.26.2 于 11-17 21:08 UTC（33 分钟后）** → 约 21:30 UTC 两版均被 PyPI 隔离/移除。窗口约 41–45 分钟。
- **恶意载荷**：wheel-only（历次正常发布均含 sdist）；新增 `.pth` 启动钩子（1.26.1 为 `agent_framework_meta.pth` / `_telemetry.py`，1.26.2 改名 `af_runtime_diag.pth` / `af_runtime_diag.py`——**按文件名检测会漏**）；读取形如 `OPENAI` / `HF_` / `FOUNDRY` 的环境变量、`/proc/*/environ`、`.npmrc` / `.git-credentials` / Azure CLI 会话 / HF token，并向 Azure managed identity、Azure DevOps OIDC、（1.26.2 新增）GitHub Actions OIDC 申请**新鲜令牌**，统一外发到单个 `webhook.site` 地址。
- **保活手法**：保留合法框架代码与依赖，应用功能不受影响 → 受害者没有任何功能异常信号。
- **根因（Wiz 研究，单源）**：攻击者疑似使用**被窃取的微软内部发布流水线客户端证书**，绕过源码仓库直接向注册表发布；PyPA 公告 PYSEC-2026-4388 称两版"未经授权上传"并已移除，GitHub Advisory **GHSA-764m-3ppc-5m73** 定性 malware（CWE-506 / CWE-829 / CWE-522，critical，**无 CVE**）。
- **影响面**：约 4.1 万次/周、约 19 万次/月下载；Wiz 在其可见请求中计到 **3 次成功外发**。11-20 时 `microsoft/agent-framework`、`microsoft/onnxruntime`、`microsoft/onnxruntime-genai` 三个 GitHub 仓库 API 仍 404（微软称"为调查将部分仓库设为私有"，与本次攻击的因果关系未确认）。
- 与既有对象的关系：与 `[cand]litellm-double-supply-chain-2026-10`（发布流水线被攻破 + wheel 植入 stealer）**同族第二轮**，但这次是**注册表侧凭据（publishing certificate）**而非 GitHub token；与 Anthropic Mythos 5 的"恶意 PyPI 包 → 真实安装 → 窃凭据"链构成攻防两侧对照。

## 3. 与我的连接
- **连接的项目**：
  - **silver-shield**：新增检测面「制品供应链」——发布事件异常（wheel-only / 缺少 sdist / 构建时间戳不一致 / 新增 `.pth`）/ 启动钩子扫描 / 环境变量与 `~/.git-credentials`、`~/.npmrc` 读取行为 / 出网到 webhook 类域名。
  - **Tafcm / campus_order**：依赖锁定策略须从"版本 pin"升级为"**制品 pin（hash）+ 允许发布者**"；CI 中禁止 `pip install -U` 与浮动 `>=`；发布凭据应短期化（Trusted Publishing / OIDC）而非长期 token 或客户端证书。
  - **TeamMind**：多 agent 协作平台的依赖基座若走托管 runner，"环境里有什么凭据"应先于"能装什么包"被治理。
- **连接的知识点**：Harness 周"供应链/执行面"；Runtime 周"零凭据执行 + 短时凭据"（此处正是反例：CI runner 长期持有 Azure/GitHub OIDC 权限）；agent-containment-breach 卡的 PyPI 链；LiteLLM 卡的发布流水线叙事。
- **潜在收益**：把"AI 框架 = 可信基座"这一隐含假设显式打掉，给 silver-shield 一条可执行的制品级检测清单，而不只是 CVE 订阅。

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | GHSA-764m-3ppc-5m73（GitHub Advisory，malware / CWE-506，1.26.0 为最后干净版）；PYSEC-2026-4388（PyPA，未经授权上传、已移除）；Wiz 博客《Malicious version of Microsoft's agent-framework published to PyPI》（11-17，含时间线与证书根因）；StepSecurity 分析（`.pth` 文件名两版差异）；PyPI 项目页版本历史（1.26.0 为最新可用）；Deepwatch CA-26-052（ATT&CK T1195.002 / T1552.001 映射） |
| 证据等级 | **FACT**（多源交叉一致的版本号/时间/载荷行为）；**根因（客户端证书被窃）为 Wiz 单源，标 DESIGN/待核**；无 CVE（advisory-only） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 静态：从 PyPI 归档/镜像取 1.26.1 wheel，比对 1.26.0 的文件清单与 `.pth` 内容（预期可复现"仅 wheel、新增 pth"）；② 行为：隔离 venv 中安装 1.26.1，仅启动 `python`（不 import），观察是否触发出网（**禁止在联网环境实跑，须断网 + 假 webhook**）；③ 制度：核对本机/CI 是否存在 `agent-framework>=1.26` 浮动依赖并留证据 |
| 预期完成时间 | 兜底任务不排期；若升为深耕对象，1 次会话内可完成静态①与制度③，行为②仅在隔离环境做 |

## 5. 验证结果
<!-- 待回填 -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（事件已闭环处置，价值在于**制品供应链检测清单**，非持续跟踪对象）
- [ ] 拒绝（原因）
