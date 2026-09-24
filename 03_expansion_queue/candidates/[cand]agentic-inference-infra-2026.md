# 候选对象证据卡

> 状态：`[cand]` ｜ 关联方向：AI Infra × Agent（G3 项目需要 / G5 战略级，知识库空白区） ｜ 日期：2026-09-20（雷达 #18）

## 一句话定位
2026-09 推理基础设施正式进入"**agentic-aware**"时代：NVIDIA Dynamo 为 coding agent / multi-agent 工作负载做 KV 缓存感知调度（此前 round-robin 对两种模式"盲目"），AWS prefix-aware routing 让同前缀请求共享 KV 缓存（P50 TTFT -77%）、HyperPod Inference Gateway GPU-aware 路由（TTFT -82%）、vLLM KV offload 到 CPU 内存、边缘 Unified AI Gateway 联合模型路由+KV 管理——"agent 的推理成本与延迟"成为可工程化的系统问题。

## 1. 它解决什么问题
- **agentic 工作负载与 chat 负载特征不同**：coding agent 是"长 prefill→tool call→扩展 prefix→重复"的序列模式；multi-agent 是"并行 fan-out 短独立上下文"——round-robin 路由对两者都盲目，无法利用 cache locality / 请求优先级 / 会话结构["https://docs.nvidia.com/dynamo/v1.1.1/digest/agentic-inference.md"]
- 长 agent 会话的 KV cache 不断增长、占满 GPU 内存，被迫重算；重复前缀（工具 schema/系统提示）反复 prefill 浪费算力
- 边缘/端侧（Tafcm 场景）需要在"设备-边缘-云"间联合决策"跑哪个模型、在哪跑、KV 缓存怎么放"

## 2. 为什么现在值得关注（活跃度证据）
- **NVIDIA Dynamo（v1.1.1，官方文档 08-17 更新）**：LLM-aware Router（KV 缓存感知路由 + 优先级调度 + 可扩展路由策略三机制）、**KV Caching to Storage**（GPU→CPU RAM/SSD/网络存储即时卸载）、Grove（拓扑优化 K8s 编排）["https://www.nvidia.com/en-us/ai/dynamo/"]["https://docs.nvidia.com/dynamo/v1.1.1/digest/agentic-inference.md"]
- **AWS SageMaker HyperPod Inference Gateway（09-18 发布）**：K8s 原生 GPU-aware 路由，单一 managed add-on，**首 token 延迟降 82%**["https://www.unite.ai/aws-launches-sagemaker-hyperpod-inference-gateway-for-gpu-aware-routing/"]
- **AWS prefix-aware routing（09-10）**：同前缀→同实例 KV 复用，Llama 3.1 70B 上 **P50 TTFT -77%、吞吐 +16%**["https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/"]
- **vLLM KV offloading connector（09-18 博客）+ PegaFlow 外部 KV cache 服务**：KV 卸载 CPU 内存降重算、可插拔卸载后端["https://vllm.ai/blog"]
- **Unified AI Gateway（arXiv 2609.06940，09-07）**：边缘部署 AI 流量枢纽——联合模型路由 + KV 缓存管理 + 计算放置（端/边/云三域）["https://arxiv.org/abs/2609.06940"]
- **阿里云 TokenWorks（08-25）**：agentic 时代企业级推理平台（智能路由/cache-aware 调度/KV 存储/模型预热）["https://help.aliyun.com/en/pai/tokenworks-overview"]

## 3. 与我的连接
- **连接的项目**：**Tafcm**（本地/边缘推理——Unified AI Gateway 的"端-边-云联合路由"直接映射 Tafcm 的本地优先 + 云端后备架构）；**TeamMind**（multi-agent fan-out 的推理模式——Dynamo 文档把"多 agent 并行短上下文"列为独立工作负载类别）；**dsh**（coding agent 序列模式"长 prefill+tool call 循环"是 Dynamo 优化对象）；E2E-CLI（agent 化测试的长链路推理）
- **连接的知识点**：Agent Harness 六职责（control 职责的"推理调度"侧面）、Context Engineering（前缀复用=工具 schema/系统提示缓存）、五维模型 Tool/Context 维度
- **潜在收益**：**补 G3/G5"AI Infra×Agent"知识空白**；Tafcm 的"本地优先"设计可获得"边缘网关联合调度"的参考实现；理解 agent 推理成本结构（prefix 复用率）反哺 Context Engineering 的预算决策
> **雷达增量（2026-09-25，agentic KV cache 管理研究爆发）**：
> - **ThunderAgent（arXiv 2602.13692）**：**程序感知 agentic 推理调度**——把调度建模为约束优化（最小化重算/缓存开销、最大化 prefill/decode 吞吐）；**state-aware pausing**（内存压力下选择性暂停"acting"工作流，保留"reasoning"程序）["https://arxiv.org/html/2602.13692"]
> - **Sutradhara（arXiv 2601.12967）**：**编排器-引擎协同设计**——KV 块语义标记（区分低价值 transient 块与高价值首轮复用块）+ 优先级驱逐["https://arxiv.org/html/2601.12967v1/"]
> - **IntentKV（arXiv 2606.09916）**：**跨轮意图感知 KV 剪枝**——会话级 QueryMemory 打分活历史 token，slot-map 重定向保前缀缓存可组合性（匹配全缓存基线性能）["https://arxiv.org/html/2606.09916"]
> - **KernelFlume（arXiv 2606.29207）**：**解码为中心架构**——stable projection/FFN 与 core-attention 分离，weightless attention 节点存 token-range KV 分区按请求状态弹性扩展（路由表 + UCX 信号）["https://arxiv.org/html/2606.29207"]
> - **DualPath（arXiv 2602.21548）**：**双路径 KV 缓存加载**——常规 storage→prefill 路径之外，KV 可经 RDMA 从 decode 引擎直传 prefill 引擎，打破 prefill 侧存储带宽瓶颈["https://arxiv.org/html/2602.21548"]
> - **Astera Labs Leo X 系列（09-15）**：**硬件层 KV cache offload**——智能内存控制器在 GPU/CPU 间加速 KV 迁移（agentic 流量"sub-agent bursts"尖峰特征驱动）["https://www.asteralabs.com/resources/blog/supercharging-agentic-ai-how-leo-x-series-smart-memory-controllers-accelerate-inference-with-kv-cache-offload/"]
> - **含义**：① **Agentic KV Cache 管理从"路由机制"扩展为"调度/驱逐/剪枝/架构/硬件"全栈研究对象**——Dynamo 之后两个月内 5 篇论文 + 1 硬件方案，该领域进入研究密集期；② "agentic 流量特征"（sub-agent bursts/长会话复用/tool-call 中断）成为推理系统设计一等输入——Tafcm 本地+云混合的 KV 策略可对照 IntentKV（剪枝）与 DualPath（跨引擎迁移）；③ **硬件入场（Astera）**说明 KV offload 从软件优化走向基础设施——dsh 长会话成本测算需纳入 KV 存储/迁移成本模型

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | https://docs.nvidia.com/dynamo/v1.1.1/digest/agentic-inference.md ｜ https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/ ｜ https://arxiv.org/abs/2609.06940 ｜ https://vllm.ai/blog |
| 证据等级 | **FACT（NVIDIA/AWS 官方 + arXiv 论文 + vLLM 官方博客）** |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | 精读 Dynamo agentic-inference 文档 → 测算 Tafcm 本地+云混合的 KV 复用收益 → 对照 prefix-aware routing 思路评估 dsh 长会话成本 |
| 预期完成时间 | 2026-10 |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
