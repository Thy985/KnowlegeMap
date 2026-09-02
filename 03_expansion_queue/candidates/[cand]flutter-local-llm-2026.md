# 候选证据卡 · [cand] Flutter 本地/端侧 LLM 推理工具链（ai_edge / flutter_gemma / Llamafu 等）
> 状态：`[cand]` ｜ 分类：本地/边缘/移动 AI（G3） ｜ 发现：2026-09-02（雷达） ｜ 等级：**A**
## 一句话定位
2026 年 Flutter/Dart 生态已出现成形的"端侧 LLM"工具带：Google `ai_edge`（v0.1.0，基于 MediaPipe GenAI）、`flutter_gemma`（跨 6 平台跑 Gemma/Qwen/DeepSeek/Phi/SmolLM）、`Llamafu`（Flutter FFI + llama.cpp）、`llama_flutter_android`（Android GGUF）等——让 Tafcm 这类 Dart 移动应用可以直接把 LLM 推理搬到本机。
## 1. 它是什么 / 解决什么问题
- 解决"移动/桌面端离线跑 LLM"：Tafcm 的"手机优先+离线可用"、silver-shield 的端侧感知都依赖这类能力["https://pub.dev/packages/flutter_gemma"]["https://github.com/cognisoc/llamafu"]
- 技术路线分两派：**系统原生派**（ai_edge/ML Kit GenAI → Gemini Nano；flutter_local_ai 用系统 API，零模型下载）vs **开源模型派**（flutter_gemma/Llamafu/llama_flutter 打包 GGUF 自跑）["https://pub.dev/documentation/flutter_local_ai/latest/"]
- 平台现状：iOS=Apple Core AI（WWDC26）、Android=LiteRT-LM（替代 MediaPipe LLM Inference）、Flutter=ai_edge v0.1.0["https://aicoding.csdn.net/6a68693f10ee7a33f29343f1.html"]
## 2. 为什么现在值得关注（活跃度证据）
- flutter_gemma 1.5.1（2026-08-31）跨 iOS/Android/Web/macOS/Windows/Linux 六平台，含视觉模型与 Function Calling["https://pub.dev/packages/flutter_gemma"]
- Google ai_edge 发布 v0.1.0（基于 MediaPipe GenAI），Google 官方背书["https://aicoding.csdn.net/6a68693f10ee7a33f29343f1.html"]
- Llamafu / llama_flutter_android 均在 2026-09 前后活跃更新（GGUF 本地推理 + token 流式 + 工具调用）["https://github.com/cognisoc/llamafu"]["https://github.com/dragneel2074/Llama-Flutter"]
## 3. 与我的连接
- **连接的项目**：**Tafcm（Dart，最活跃项目）**——直接可用的本地 AI 能力，公式/Markdown 工具可加"本地小模型助手"；**silver-shield**——端侧风险识别模型部署；**weather-recognition**——on-device 推理
- **连接的知识点**：本地/边缘 AI 缺口（G3）、Tafcm 离线优先定位、ML 实验方法论（模型部署面）
- **潜在收益**：给 Tafcm 加离线 LLM 能力的选型实证；补全"本地/边缘 AI"知识空白的最短路径（直接在活跃 Dart 项目上验证）
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://pub.dev/packages/flutter_gemma ｜ https://pub.dev/packages/flutter_local_ai ｜ https://github.com/cognisoc/llamafu ｜ Google ai_edge 文档 |
| 证据等级 | FACT（pub.dev 官方包信息） |
| 验证方式 | 在 Tafcm 侧建最小 demo：flutter_gemma 跑一个离线生成任务，对比 ai_edge 系统原生路线，测启动/首 token/体积 |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
> **雷达增量（2026-09-03，Changed）**：
> - **新发现：`flutter_litert_lm`**（Flutter 插件，跑 Google **LiteRT-LM**——Android 端已**替代 MediaPipe LLM Inference** 的官方新路线，支持 Gemma/Qwen/Phi/DeepSeek 及 litert-community 全系模型，GPU(OpenCL)/NPU 硬件加速，无 API key 无网络）["https://github.com/songhieu/flutter_litert_lm"]——这是 Tafcm 本地 LLM 选型的重要新增候选
> - 新增 `llx_flutter`（Flutter FFI 插件跑 GGUF via llama.cpp，Dart 拥有 app-facing API + 生命周期，原生层管 model loading/context/token，示例含 bundle GGUF）["https://github.com/gmarzjr/llx_flutter"]、`flutter_native_ai`（统一 API 封装 Apple Foundation Models + Gemini Nano）["https://github.com/bowvie/flutter_native_ai"]、`Flutter Local AI`（三端统一 API：Android ML Kit GenAI / iOS FoundationModels / Windows AI APIs，零模型下载）["https://pub.dev/documentation/flutter_local_ai/latest/"]
> - 平台格局已收敛为**三派**：系统原生（Apple Core AI / LiteRT-LM / Windows AI）｜ Flutter 官方（ai_edge v0.1.0 on MediaPipe GenAI）｜ 开源 GGUF（llama.cpp 系：llx_flutter/Llamafu/llama_flutter_android）["https://aicoding.csdn.net/6a68693f10ee7a33f29343f1.html"]
> - **含义**：Tafcm 选型可从 3 派各取一实测（推荐 flutter_litert_lm 或 flutter_local_ai 作为零下载系统原生派代表 + llx_flutter 作为可控 GGUF 派代表）
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
