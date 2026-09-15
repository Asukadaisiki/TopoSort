"""T4 渲染场景契约测试（offscreen，验收标准本身）。骨架红，T4 后全绿。"""
import os

import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from app.scene import Effects, GraphBoard  # noqa: E402
from app.events import Complete, Consume, Enqueue  # noqa: E402

LAYERS = {"A": 0, "B": 0, "C": 1, "D": 2, "E": 1}
NODES = frozenset(LAYERS)
EDGES = frozenset({("A", "C"), ("A", "E"), ("B", "C"), ("C", "D")})


@pytest.fixture()
def board(qtbot):
    return GraphBoard(NODES, EDGES, LAYERS)


class TestVisualStates:
    def test_initial_idle(self, board):
        assert board.node_state("A") == "idle"

    def test_enqueue_then_consume(self, board):
        board.apply_event(Enqueue("A", 0))
        assert board.node_state("A") == "ready"
        board.apply_event(Consume("A", 0))
        assert board.node_state("A") == "ghost"

    def test_stuck_nodes_marked(self, board):
        from app.events import CycleFound

        board.apply_event(CycleFound(frozenset({"A", "B"})))
        assert board.node_state("A") == "stuck"
        assert board.node_state("B") == "stuck"


class TestExport:
    def test_png_nonempty(self, board, tmp_path):
        out = tmp_path / "graph.png"
        board.export_png(out)
        assert out.exists() and out.stat().st_size > 0


def test_effect_durations_bounded():
    assert 0 < Effects.GHOST_MS <= 1000
    assert 0 < Effects.PULSE_MS <= 1000
    assert 0 < Effects.EDGE_DIM_MS <= 1000
