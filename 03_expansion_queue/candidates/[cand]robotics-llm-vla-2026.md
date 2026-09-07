# 候选证据卡 · [cand] Robotics×LLM / 具身智能 VLA（Qwen-VLA / Qwen-RobotSuite / LingBot-VLA 2.0）
> 状态：`[cand]` ｜ 分类：Robotics × LLM / 具身智能（G4 兴趣未接入） ｜ 发现：2026-09-08（雷达 #7） ｜ 等级：**B**
## 一句话定位
2026 年 VLA（Vision-Language-Action）进入"统一基础模型"阶段：**Qwen-VLA**（DiT 动作解码器统一跨任务/环境/本体决策）、**Qwen-RobotSuite**（操控/世界模型/导航三件套）、蚂蚁 **LingBot-VLA 2.0**（6 万小时真实数据、跨形态泛化）、宇树 **UnifoLM-VLA**（LIBERO 98.7）——具身智能从"单任务模型"走向"统一基座 + 开源生态"。与我的 multi_arm_line_ws 项目（孤悬无知识支撑）形成潜在连接。
## 1. 它是什么 / 解决什么问题
- 痛点：具身决策被拆成操控/导航等专用模型，跨任务/环境/机器人本体泛化差["https://arxiv.org/pdf/2605.30280"]
- **Qwen-VLA**（2026-05）：统一具身基础模型，Qwen VLM 栈从感知/理解/推理扩展到连续动作与轨迹生成（DiT 动作解码器）；大规模联合预训练（机器人操控轨迹 + 人类第一视角演示 + 仿真 + V&L 数据）["https://arxiv.org/pdf/2605.30280"]["https://hub.baai.ac.cn/paper/0ae9c7ce-168e-4379-84ad-108e12eb2a93"]
- **Qwen-RobotSuite**（2026-06）：Qwen-RobotManip / Qwen-RobotWorld（视频世界模型）/ Qwen-RobotNav 三模型["https://www.marktechpost.com/2026/06/16/meet-qwen-robotsuite-three-embodied-ai-models-for-vla-manipulation-video-world-modeling-and-navigation"]
- **LingBot-VLA 2.0**（蚂蚁 Robbyant，2026-07 开源）：跨形态学习 + 全身控制 + 6 万小时真实训练数据["https://www.roboticsbusinessnews.com/news/10/3229/robbyant-open-sources-lingbot-vla-2-0-to-advance-universal-embodied-ai-for-robotics.html"]
- 同线：Visics VLOA（3D 物体轨迹作跨本体通用接口）、TurboVLA（RTX 4090 32Hz <1GB VRAM 实时 VLA）["https://embodiedglobal.com/en/article/roboscience-visics-vloa-embodied-world-model-universal-robot-2026"]["https://share.transistor.fm/s/57443c98"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-08）**：Qwen-VLA arXiv 2605.30280 ✅、Qwen-RobotSuite 官方发布 ✅、LingBot-VLA 2.0 行业报道 ✅、awesome-foundation-models-for-robotics 持续更新 ✅
- 中国厂商密集动作：Qwen（阿里）、LingBot（蚂蚁）、UnifoLM（宇树，09-07 发布世界模型实时驱动全自主格斗）——具身智能开源竞赛进入白热化["http://m.toutiao.com/group/7682791919331574298/"]
- 开源清单 60+ 模型（Pi0→HoloBrain-0 15 大开源力作）["https://blog.csdn.net/Yangy_Jiaojiao/article/details/163745508"]
## 3. 与我的连接
- **连接的项目**：**multi_arm_line_ws**（多机械臂工作区项目，G4 标记"孤悬无知识支撑"）——VLA 与机械臂操控直接相关
- **连接的知识点**：Robotics × LLM（G4 兴趣未接入）、多模态模型、世界模型
- **潜在收益**：给 multi_arm_line_ws 补上理论/生态支撑的最小入口；VLA 的"统一基座"思路与 Agent 框架的"统一 harness"范式同构（可作类比学习）
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/pdf/2605.30280 ｜ https://www.marktechpost.com/2026/06/16/meet-qwen-robotsuite-three-embodied-ai-models-for-vla-manipulation-video-world-modeling-and-navigation ｜ https://github.com/cagbal/awesome-foundation-models-for-robotics |
| 证据等级 | **FACT（arXiv + 官方发布 + 开源清单核验通过）** |
| 验证方式 | 通读 Qwen-VLA 论文 → 对照 multi_arm_line_ws 的操控需求 → 评估是否引入 VLA 基座或仅作知识补全 |
| 预期完成时间 | 观察期（G4 兴趣层，视 multi_arm_line_ws 进展） |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
