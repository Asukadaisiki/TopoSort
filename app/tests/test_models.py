"""T2 算法内核契约测试（验收标准本身）。骨架阶段应红，T2 完成后全绿。

规则：只走公共 API（app.models 导出），断言行为而非实现。
"""
import pytest

from app.models import Graph, ParseError, parse
from app.tests.conftest import CANON_ORDERS, CANON_TEXT


def is_valid_order(order, graph: Graph) -> bool:
    """性质断言：序是节点的完整排列，且尊重所有边方向。"""
    if sorted(order) != sorted(graph.nodes):
        return False
    pos = {n: i for i, n in enumerate(order)}
    return all(pos[a] < pos[b] for a, b in graph.edges)


class TestParse:
    def test_canon_graph(self):
        g = parse(CANON_TEXT)
        assert g.nodes == frozenset("ABCDE")
        assert g.edges == frozenset({("A", "C"), ("A", "E"), ("B", "C"), ("C", "D")})

    def test_tolerates_blank_lines_and_fullwidth_and_bare(self):
        g = parse("\n<A,C>\n\n（A，E）\nB,C\n")
        assert ("A", "E") in g.edges and ("B", "C") in g.edges

    def test_duplicate_edges_dedup(self):
        g = parse("<A,B>\n<A,B>\n")
        assert len(g.edges) == 1

    def test_bad_line_reports_lineno(self):
        with pytest.raises(ParseError) as ei:
            parse("<A,B>\n<A>\n")
        assert ei.value.lineno == 2

    def test_self_loop_rejected(self):
        with pytest.raises(ParseError):
            parse("<A,A>\n")


class TestCycle:
    def test_two_node_cycle(self):
        g = parse("<A,B>\n<B,A>\n")
        assert g.has_cycle() is True
        assert g.cycle_nodes() == frozenset({"A", "B"})
        assert list(g.iter_topo_orders()) == []

    def test_cycle_nodes_excludes_free_nodes(self):
        g = parse("<A,B>\n<B,A>\n<C,D>\n")
        assert g.cycle_nodes() == frozenset({"A", "B"})


class TestEnumerate:
    def test_canon_six_orders_all_valid(self):
        g = parse(CANON_TEXT)
        orders = list(g.iter_topo_orders())
        assert len(orders) == 6
        assert all(is_valid_order(o, g) for o in orders)
        assert sorted(map(tuple, orders)) == sorted(map(tuple, CANON_ORDERS))

    def test_max_count_truncates(self):
        g = parse(CANON_TEXT)
        assert len(list(g.iter_topo_orders(max_count=2))) == 2

    def test_stability_same_input_same_sequence(self):
        g = parse(CANON_TEXT)
        assert list(g.iter_topo_orders()) == list(g.iter_topo_orders())

    def test_count_matches_enumeration(self):
        g = parse(CANON_TEXT)
        assert g.count_orders() == len(list(g.iter_topo_orders()))


class TestLayers:
    def test_canon_layers(self):
        g = parse(CANON_TEXT)
        layers = g.layers()
        assert layers["A"] == 0 and layers["B"] == 0
        assert layers["C"] == 1
        assert layers["D"] == 2 and layers["E"] == 1
