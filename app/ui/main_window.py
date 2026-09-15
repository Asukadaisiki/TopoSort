"""主窗口。实现 T5（issue #6）。"""


class MainWindow:
    def set_input(self, text: str) -> None:
        raise NotImplementedError("T5: MainWindow.set_input")

    def input_text(self) -> str:
        raise NotImplementedError("T5: MainWindow.input_text")

    def click_start(self) -> None:
        raise NotImplementedError("T5: MainWindow.click_start")

    def results(self) -> list:
        raise NotImplementedError("T5: MainWindow.results")

    def error_text(self):
        raise NotImplementedError("T5: MainWindow.error_text")
