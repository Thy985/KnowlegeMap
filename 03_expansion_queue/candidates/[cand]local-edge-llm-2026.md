# 候选证据卡 · [cand] 本地/边缘 LLM 推理与边缘微调（LlamaWeb / MLC-LLM / BitNet 边缘微调 / TinyLLM）

> 状态：`[cand]` ｜ 分类：本地/边缘 AI（B13）/ G3 项目需要 ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
2026 本地/边缘 LLM 进入"跨端 + 浏览器 + 移动 GPU 微调"阶段：LlamaWeb 把 llama.cpp 跑进浏览器 WebGPU、MLC-LLM 全平台、BitNet 可在手机 GPU 微调、TinyLLM 实证边缘 agent SLM——直接服务 Tafcm（离线优先）与 silver-shield（边缘感知）。

## 1. 关键事实
- **LlamaWeb**（arXiv 2026）：llama.cpp 的 WebGPU 后端，浏览器内 GPU 加速跑多模型，多精度、内存高效["https://arxiv.org/html/2605.20706v1"]
- **MLC-LLM**：跨平台，Vulkan/Metal/OpenCL/WebGPU/Android 均 production["https://localaimaster.com/blog/mlc-llm-setup-guide"]
- **BitNet b1.58 边缘微调**（QVAC Fabric）：首次在移动 GPU（Adreno/Mali/Apple Bionic）微调 BitNet，125M 约 10 分钟（Samsung S25），1B 级亦可["https://github.com/tetherto/qvac-rnd-fabric-llm-bitnet"]
- **TinyLLM**（arXiv）：小语言模型在边缘做 agentic 任务的评测与优化，DPO 对齐 SLM agent["https://arxiv.org/html/2511.22138v1/"]
- 运行时谱系：llama.cpp（GGUF 事实标准，CPU/ARM/Apple）、ONNX Runtime（CPU/CUDA/TensorRT/DirectML）、OpenVINO（Intel）、TensorRT-LLM（NVIDIA）["https://martinuke0.github.io/posts/2026-03-22-the-shift-to-edge-native-llms-optimizing-local-inference-for-privacy-first-developer-workflows/"]
> **雷达增量（2026-09-11，Changed）**：
> - **MiniCPM5-2B（2026-09-07，OpenBMB，Apache-2.0）**：25 亿参数小模型（1.98B 激活），目标"手机/笔记本/边缘盒"级硬件——Tafcm 移动端 SLM 直接候选["https://ai-tldr.dev/models/minicpm5-2b/"]
> - **Qwen3.8 系列（2026-08 起）**：Qwen3.8-27B（08-14，原生 VLM，本地 Mac 第一，LLMCheck Score 71）超 Qwen3.6 27B；Empero **Qwen3.8-9B-GGUF**（从 Qwen3.8 2.4T A95B 全参蒸馏至 Qwen3.5-9B 架构）；Qwen3-4B-Instruct/Thinking-2507["https://llmcheck.net/blog/state-of-open-source-local-llms-september-2026/"]["https://ai.atomgit.com/hf_mirrors/empero-ai/Qwen3.8-9B-GGUF"]
> - **Edge LLM（WASM-first + WebGPU，纯 Rust）**：浏览器内零服务器跑 LLM，同代码库编译 native+WASM（同一 WGSL shader/量化核/推理管线）；M5 Pro 基准 vs llama.cpp 对比公开——与 flutter-local-llm 的浏览器路线互补["https://github.com/CloseAI-ai/edge-llm"]
> - **GLM-5.3-Flash（MIT，320B/18B active MoE）**：quant 可跑 Mac Studio——前沿 MoE 进入本地["https://llmcheck.net/blog/state-of-open-source-local-llms-september-2026/"]
> - **含义**：本地 SLM 竞争从"能跑"转向"手机/浏览器原生"（MiniCPM5-2B/Edge LLM）；Qwen3.8-27B 证明 27B 级 VLM 已可在 24GB RAM 本地部署——Tafcm 本地选型池显著扩大

## 2. 与我的知识/项目关系
- **Tafcm**（Dart 移动端、离线优先）：llama.cpp FFI / ONNX Runtime 跨平台打包，或 WebGPU（若走 Web）；移动端嵌入是明确路径
- **silver-shield**（摄像头端感知）：边缘分类/事件检测（YAMNet 类）可用 ONNX Runtime/OpenVINO
- **G3 缺口"本地/边缘/移动 AI"** 是 KB 空白，本卡建立第一层

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（arXiv + 官方文档） |
| 来源 | https://arxiv.org/html/2605.20706v1 ｜ https://github.com/tetherto/qvac-rnd-fabric-llm-bitnet ｜ https://arxiv.org/html/2511.22138v1/ |
| 验证方式 | 评估在 Flutter/Dart 侧用 llama.cpp FFI 跑一个小模型的概念验证；对比 WebGPU 方案 |
| 预期 | 2026-10 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
