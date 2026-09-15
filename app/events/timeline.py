"""伪并发时间线：暂停/单步/调速/泳道上限。实现 T3（issue #4）。"""

from .player import TopoPlayer


class Timeline:
    def __init__(self, player: TopoPlayer, lane_limit: int = 8, tick_ms: int = 400):
        self.player = player
        self.lane_limit = lane_limit
        self.tick_ms = tick_ms
        self.state = "running"

    def tick(self) -> list:
        """推进一拍：每个活跃分支各走一步（交错）。实现 T3。"""
        raise NotImplementedError("T3: Timeline.tick")

    def pause(self) -> None:
        raise NotImplementedError("T3: Timeline.pause")

    def resume(self) -> None:
        raise NotImplementedError("T3: Timeline.resume")

    def step_once(self) -> list:
        raise NotImplementedError("T3: Timeline.step_once")

    def set_speed(self, ms: int) -> None:
        raise NotImplementedError("T3: Timeline.set_speed")
