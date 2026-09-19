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
