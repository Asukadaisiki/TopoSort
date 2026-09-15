"""候选池芯片。实现 T4（issue #5）。"""


class CandidatePool:
    def set_ready(self, nodes) -> None:
        raise NotImplementedError("T4: CandidatePool.set_ready")

    def on_consume(self, node: str) -> None:
        raise NotImplementedError("T4: CandidatePool.on_consume")
