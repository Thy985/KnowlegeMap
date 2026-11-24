# 2026-11-25 Personal Tech Radar 兜底扫描

- 范围：轻量全领域（MCP / A2A / Agent 框架安全 / Memory / Runtime / AI Infra），4 组 general_search + 1 次 web_fetch。
- 去重基准：`grep -a -r -l -i` 于 `06_expansion_index` / `03_expansion_queue` / `08_agent_centric`，命中 Cairn 于 agentic-attack 卡（09-25 / 10-01 两处，均为"成本 ~$2 调度套件"级别）。
- 当前深耕：Computer Use / Browser（11-23~11-29 第一周）；本轮不含该领域内容。

## 判定

| 对象 | 档位 | 处置 |
|---|---|---|
| **Cairn × MONAI Label 零日（CVE-2026-133968）** | **S（New 事件，领域外）** | 并入 `[cand]agentic-attack-2026.md` 事件日 25（Changed），不新建卡 |
| MemT-1.0-Pro（554B memory-native，11-23） | B | 记日志；Memory 已收束，不建卡 |
| Microsoft agent-framework 1.26.1/1.26.2 | 已入账（11-24） | 去重，不重复 |
| MCP 2026-07-28 revision / A2A v1.0 breaking changes | 已入账 | 去重，不重复 |
| AgentCore next-gen runtime 默认（11-12） | B | 记日志，不建卡 |
| OpenAI「雅典娜」数据工具（11-25） | 证据不足 | 不写 |

## 一手事实（AWS Blog，11-20 发布）

- 2026-09-10 AWS Threat Intelligence 发现**未认证公网暴露的 Cairn 实例**，运营历史（配置 / prompt / 输出）全部可读 → 才得以还原事件。
- 行动窗口：2026-09-08 起约 48 小时；目标为中国大陆以外东亚高校；操作者 prompt 为简体中文、脚本时间戳 CST（AWS 归因表述，本仓仅记录）。
- 授权形状：目标 IP 清单 + 一句目标（"取得 shell 权限"，措辞微调），步骤由 agent 自行规划/执行/换招。
- Redis 面：约 16 小时、**148 次**连续动作，复制加载 / 沙箱逃逸 / 写配置 / 破坏内存 / Log4Shell，全失败 → Qdrant SSRF 取 Docker 拓扑 → PostgreSQL/SSH 凭据喷洒，仍失败。
- GPU 面：OSINT（名录/主页/存档/论文）→ ~80 个真实用户名；SSH/管理后台/NAS/VPN/门户 **30,000+** 组合。
- 成功面（医用影像 AI 应用）：枚举 API → upload 端点 filename 参数 → 路径穿越；**API 映射到任意文件写约 11 分钟**；`sitecustomize.py` 写反弹 shell → 调 training API 拉新进程 → **root 反弹 shell**。
- 后续：操作者提供通往第二所高校网络的代理（同软件在跑），指示打更多机器——"机器找路、人给跳板"。
- 零日认定：发现时无公告/无补丁/无漏洞库记录，AWS 高置信判定为零日。
- 修复：项目 11-22 发 0.8.6（同时修会话归档第二处穿越）。

## 漏洞记录

- CVE-2026-133968 / EUVD-2026-131722 / GHSA-2f43-rwqm-6h67；CVSS 9.8；`monailabel ≤0.8.5`；`PUT /datastore/image` 的 `image` 参数目录穿越 → RCE；**已在野利用（2026-09 起）**；EPSS 3.13%。
- CISA KEV：中文媒体 11-25 称已列入；EUVD 页面（11-20 抓取）显示 "Not listed" → **时间差待核**。

## 含义（写入卡内）

1. 质变是"发现"能力，不是成本：前 24 个事件日都是已知手法/已知面，本次是自主发现未知漏洞 + 完整利用链。
2. `sitecustomize.py`（本次）与 `.pth`（11-17 MAF）同族——**解释器启动即执行**成为标准后利用原语。
3. 攻击方控制面裸奔（Cairn 无认证公网实例）是事件可被看见的唯一原因，与事件日 22~24 同族。
4. 16 小时 148 次动作 → 人类审计跟不上，防守必须"高置信检测 + 自动响应"。
5. silver-shield 两条确定性检查：服务端收文件名的写接口清单；启动期钩子文件（`sitecustomize.py` / `usercustomize.py` / `*.pth`）基线比对。

## 未做

- 未独立复现路径穿越（无隔离环境）；未核 NVD 原文；未核 KEV 当前状态（时间差）；Cairn star/fork 各快照不一致未统一。
