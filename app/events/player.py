"""算法 → 确定性事件流。实现 T3（issue #4）。"""

from ..models import Graph
from .protocol import StepEvent


class TopoPlayer:
    def __init__(self, graph: Graph):
        self.graph = graph

    def iter_events(self):
        """契约：确定性；对无环图最终对每条完整序发一次 Complete。"""
        raise NotImplementedError("T3: TopoPlayer.iter_events")
