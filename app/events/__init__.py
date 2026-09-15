"""events：算法→动画的解耦层（纯逻辑，零 Qt 依赖——CI 强制）。

公共 API：

    StepEvent         # dataclass 联合类型，见 protocol.py
    TopoPlayer(graph) -> player
        .iter_events() -> Iterator[StepEvent]   # 确定性：同输入两次序列逐项相等
        事件类型：Enqueue(node, branch_id) / Consume(node, branch_id) /
                  Fork(branch_id, new_branch_id, node) / Complete(branch_id, order) /
                  DeadEnd(branch_id, stuck_nodes) / CycleFound(stuck_nodes)

    Timeline(player, lane_limit: int = 8, tick_ms: int = 400)
        .tick() -> list[StepEvent]   # 每拍交错推进所有活跃分支一步（伪并发）
        .pause() / .resume() / .step_once() -> list[StepEvent]
        .set_speed(ms: int)          # 调整拍间隔
        .state -> "running" | "paused" | "finished"
        契约：超出 lane_limit 的分支不展示但仍计数；全部分支终止后 state=finished
"""

from app.events.protocol import (
    Complete,
    Consume,
    CycleFound,
    DeadEnd,
    Enqueue,
    Fork,
    StepEvent,
)
from app.events.player import TopoPlayer
from app.events.timeline import Timeline

__all__ = [
    "StepEvent", "Enqueue", "Consume", "Fork", "Complete", "DeadEnd", "CycleFound",
    "TopoPlayer", "Timeline",
]
