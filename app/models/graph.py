"""图数据结构 + 分层。实现 T2（issue #3）。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Graph:
    """不可变有向图。构造请走 app.models.parse()。"""

    nodes: frozenset[str]
    edges: frozenset[tuple[str, str]]

    def layers(self) -> dict[str, int]:
        """最长路径分层：入度 0 的节点为第 0 层，其余 = max(pred.layer)+1。有环时抛 CycleError（契约见 parser）。"""
        raise NotImplementedError("T2: graph.layers")

    def has_cycle(self) -> bool:
        raise NotImplementedError("T2: graph.has_cycle")

    def cycle_nodes(self) -> frozenset[str]:
        raise NotImplementedError("T2: graph.cycle_nodes")

    def iter_topo_orders(self, max_count: int | None = None):
        """按字典序稳定产出全部拓扑序；max_count 截断；有环时产出空。"""
        raise NotImplementedError("T2: graph.iter_topo_orders")

    def count_orders(self) -> int:
        raise NotImplementedError("T2: graph.count_orders")
