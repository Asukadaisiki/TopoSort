"""图画布：分层布局消费 + 事件驱动视觉状态。实现 T4（issue #5）。"""


class GraphBoard:
    """依赖方向：只 import app.events 与 dict layers，绝不 import app.models 的算法函数。"""

    def __init__(self, graph_nodes, graph_edges, layers: dict[str, int]):
        raise NotImplementedError("T4: GraphBoard.__init__")

    def apply_event(self, event) -> None:
        raise NotImplementedError("T4: GraphBoard.apply_event")

    def node_state(self, node: str) -> str:
        raise NotImplementedError("T4: GraphBoard.node_state")

    def export_png(self, path) -> None:
        raise NotImplementedError("T4: GraphBoard.export_png")
