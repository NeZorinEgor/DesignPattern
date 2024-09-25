from src.core.report import ABCReport


class MarkdownReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        pass
