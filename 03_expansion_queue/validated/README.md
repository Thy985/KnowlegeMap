# 03 · validated（已验证高价值对象）

> 晋升条件：≥2 条独立证据 + 一次真机/源码级验证。晋升后在此记录**验证了什么、证据在哪、与哪个项目/知识连接**。
> 生命周期：candidates（[cand]）→ 本目录（[val]）→ 晋升飞书内库 / 应用到项目。

## 已验证对象清单

| 对象 | 发现日期 | 验证日期 | 验证方式 | 验证结果 | 等级 | 连接 |
|---|---|---|---|---|---|---|
| [DeepSeek Harness v0.1]([val]deepseek-harness-2026.md) | 2026-09-02 | 2026-09-02 | 源码级验证（git clone + 精读 docs/architecture + capability-seams + README） | ✅ 通过：确证 Cordis 插件树、能力 seam 三角色、profile/组合包/patch 配置树、配套论文 arXiv 2608.25512；与 TeamMind/五维模型完成架构对照 | **S** | TeamMind（插件化/seam 化/事件溯源会话日志/把关流水线 三点可借鉴） |
| promptfoo（首轮） | 2026-09-01 | 2026-09-01 | 本机实测（echo provider 2/2 PASS） | ✅ 通过 | **S** | Tafcm ADI / silver-shield Benchmark |

## 验证方法备忘
- **DeepSeek Harness**：`git clone --depth 1 https://github.com/deepseek-ai/deepseek-harness.git` → 读 README（确认 MIT/TS/dev-preview/Cordis/论文）→ 读 docs/architecture.zh.md（确认插件树/profile/组合包/核心包）→ 读 docs/capability-seams.zh.md（确认 seam 三角色与全套 ctx.* 服务）→ 对照 TeamMind 五维模型逐项映射。
- 后续对象晋升时在此追加，并附验证命令/证据 URL。
