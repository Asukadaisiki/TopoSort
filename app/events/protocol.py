"""StepEvent 协议定义（唯一权威出处）。实现 T3（issue #4）。"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Enqueue:
    node: str
    branch_id: int


@dataclass(frozen=True)
class Consume:
    node: str
    branch_id: int


@dataclass(frozen=True)
class Fork:
    branch_id: int      # 原分支
    new_branch_id: int  # 新分出的分支
    node: str           # 分叉时被选走的节点


@dataclass(frozen=True)
class Complete:
    branch_id: int
    order: tuple[str, ...]


@dataclass(frozen=True)
class DeadEnd:
    branch_id: int
    stuck_nodes: frozenset[str]


@dataclass(frozen=True)
class CycleFound:
    stuck_nodes: frozenset[str]


StepEvent = Enqueue | Consume | Fork | Complete | DeadEnd | CycleFound
