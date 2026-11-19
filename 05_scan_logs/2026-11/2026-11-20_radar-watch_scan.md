# Personal Tech Radar 深耕 · 2026-11-20（周五 · 验证日）

> 领域：Memory（第二周 Day5）。任务：三项实测（注入复现 / delete 回执 / 作用域串读），判据见 `agent-memory.md` §8.5。

## 一、环境
vm / Python 3.12.11 / `mem0ai==2.2.1` / qdrant 本地 `path=/tmp/verify_mem2/qd5` / 8 维 FakeEmbedder / FakeLLM 空 facts / `infer=False` 直写。

## 二、结果

| 实验 | 关键读数 | 判定 |
|---|---|---|
| E1 注入路径 | 命中 1 条 score **0.8000**；poison 全文进上下文；stub 输出 `send_data/confirm=false` | 命中且改写（结构级）；模型依从率未测 |
| E2 删除回执 | `{"message":"Memory deleted successfully!"}`；get_all/search/qdrant 均 0；**history.db 保留 ADD/DELETE 全文** | 回执不可核验 + 派生副本残留 |
| E3 作用域 | `filters=None` → ValueError；带 filter 全为本人（0.79 ms）；相同文本 C/D 各 1.0 零交叉；qdrant 单文件 8 点含 A/B/C/D 明文 | API 层无串读；存储层无隔离 |

## 三、判断
1. SDK 默认安全 ≠ 系统安全：边界取三条路径中最弱者（查询强制 filter / 删除留全文 / 存储单文件）。
2. 删除回执是声明层：`successfully` 回答"没报错"，不回答"不存在了"；可核验回执需 id+scope+哈希+时间+覆盖范围。
3. MemLeak 边界澄清：泄漏前提是"检索不经 scope"；Mem0 2.2.1 不成立，但共享库/备份/自建检索仍成立。

## 四、限制
- E1 用 `infer=False` 跳过抽取式写入门控；下游为规则 stub，非真实模型 → 不能外推模型依从率。
- E2 的 history 保留是 Mem0 审计设计，未做 `delete_all`/备份/远端副本检查。
- E3 未测 Graphiti / 自建向量检索 / 跨 agent 共享 bank 的池化路径。
- 全部为单机小样本，无统计功效；未复现外部攻击链。

## 结论
**Changed**（§8.5.1 + 缺口三行；无新卡）
