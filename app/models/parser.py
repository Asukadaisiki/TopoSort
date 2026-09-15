"""`<a,b>` 文本解析。实现 T2（issue #3）。"""


class ParseError(ValueError):
    """解析失败。lineno 从 1 开始；line 为原始行文本。"""

    def __init__(self, lineno: int, line: str, reason: str):
        super().__init__(f"第 {lineno} 行解析失败：{reason}（原文：{line!r}）")
        self.lineno = lineno
        self.line = line
        self.reason = reason


def parse(text: str) -> "Graph":
    """契约见包 __init__。实现 T2。"""
    raise NotImplementedError("T2: parser.parse")
