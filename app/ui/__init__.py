"""ui：界面壳（组装与信号槽）。实现 T5（issue #6）。

公共 API：

    MainWindow()  # 三栏：输入面板 | 图画板 | 泳道+结果流；顶栏控制条
        .set_input(text: str)
        .input_text() -> str
        .click_start()                 # 触发 parse→player→timeline→scene 全链路
        .results() -> list[list[str]]  # 当前结果流内容
        .error_text() -> str | None    # 解析错误/环 的展示文案（对话框或状态栏）

    run()  # 程序入口
"""

from .main_window import MainWindow

__all__ = ["MainWindow", "run"]


def run() -> None:
    raise NotImplementedError("T5: ui.run")
