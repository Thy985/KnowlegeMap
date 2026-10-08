"""Skill Evolution（v3 · tool_stats 真实数据驱动）。

让 Skill 从静态 procedure 变成可演进资产：
- 任务后用 tool_stats（usage_count / success_rate / failure_modes）：
  1. 按成功率重排 required_tools（成功率高优先）；
  2. 样本足够但成功率持续低于阈值 → 降级/剔除；
  3. 针对高频 failure_mode 插入检查步骤。
- 版本化，演进理由基于真实数据（非 LLM 生成）。
- 无显著变化不产生新版本（避免版本膨胀）。
"""
from __future__ import annotations

from typing import Dict, List, Optional

from . import knowledge
from .domain import AgentMemory, SkillVersion

MIN_SAMPLES = 3       # 工具至少被用 N 次才纳入演进
DROP_RATE = 0.5       # 成功率低于此且样本足够 → 剔除

_FAILURE_STEPS = {
    "timeout": "为该步骤设置超时与重试上限",
    "false-positive": "对候选结果二次重放校验",
    "false_positive": "对候选结果二次重放校验",
    "env": "检查环境依赖/权限后再执行",
    "flaky": "重复执行 2 次取一致结果",
    "missed-detection": "扩充检测基线并复核漏检项",
    "missing-evidence": "补齐请求/响应证据后再结论",
}


def evolve_skill(skill_id: str, memory: AgentMemory,
                 min_samples: int = MIN_SAMPLES,
                 drop_rate: float = DROP_RATE) -> Optional[SkillVersion]:
    """单个 skill 基于 tool_stats 演进；无显著变化返回 None。"""
    tpl = knowledge.SKILLS.get(skill_id)
    if not tpl:
        return None
    base_tools = list(tpl["required_tools"])
    stats = {t: memory.tool_stats[t] for t in base_tools
             if t in memory.tool_stats}
    # 全部工具样本不足 → 不演进
    if not any(stats[t].usage_count >= min_samples for t in stats):
        return None

    tool_success = {t: stats[t].success_rate for t in stats}

    # 1. 重排：有统计按成功率降序，无统计保持原顺序在后
    scored = [t for t in base_tools if t in stats]
    scored.sort(key=lambda t: -stats[t].success_rate)
    unscored = [t for t in base_tools if t not in stats]
    ordered = scored + unscored

    # 2. 剔除持续失败工具
    removed = [t for t in scored
               if stats[t].usage_count >= min_samples
               and stats[t].success_rate < drop_rate]
    kept = [t for t in ordered if t not in removed]

    # 3. 针对高频 failure 插入检查步骤
    inserted: List[str] = []
    for t in scored:
        fm = stats[t].failure_modes
        if not fm:
            continue
        top = max(fm, key=lambda k: fm[k])
        step = _FAILURE_STEPS.get(top, f"针对 {top} 增加检查点")
        tag = f"{step}（{t}: {top}）"
        if tag not in inserted:
            inserted.append(tag)

    final_proc = list(tpl["procedure"])
    if inserted:
        vi = next((i for i, s in enumerate(final_proc)
                   if "validate" in s.lower() or "验证" in s), None)
        if vi is not None:
            final_proc = final_proc[:vi] + inserted + final_proc[vi:]
        else:
            final_proc = final_proc + inserted

    # 无显著变化 → 不产生新版本
    if not removed and not inserted and kept == base_tools:
        return None

    version = len(memory.skill_versions.get(skill_id, [])) + 1
    reason = [f"v{version} 基于工具实测（样本≥{min_samples}）"]
    if removed:
        reason.append("剔除 " + ", ".join(
            f"{t}(sr={tool_success[t]:.2f})" for t in removed))
    if inserted:
        reason.append(f"补 {len(inserted)} 个失败检查步骤")
    if kept != base_tools and not removed:
        reason.append("工具按成功率重排")

    sv = SkillVersion(
        skill_id=skill_id, version=version,
        capability=tpl.get("capability", ""), procedure=final_proc,
        required_tools=kept, tool_success=tool_success,
        removed_tools=removed, inserted_steps=inserted,
        evolution_reason="；".join(reason))
    memory.skill_versions.setdefault(skill_id, []).append(sv)
    return sv


def latest_skill(skill_id: str, memory: AgentMemory) -> Optional[SkillVersion]:
    """取 skill 最新演进版本（未来任务复用，不重新从零）。"""
    vs = memory.skill_versions.get(skill_id)
    return vs[-1] if vs else None


def evolve_skills_for_caps(memory: AgentMemory,
                           capabilities: List[str], **kw) -> List[SkillVersion]:
    """任务后：对涉及能力（skill capability）批量演进。"""
    cap_to_skill = {sk.get("capability"): sid
                    for sid, sk in knowledge.SKILLS.items()}
    out: List[SkillVersion] = []
    for cap in capabilities:
        sid = cap_to_skill.get(cap)
        if sid:
            sv = evolve_skill(sid, memory, **kw)
            if sv:
                out.append(sv)
    return out
