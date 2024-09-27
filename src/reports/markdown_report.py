from src.core.report import ABCReport


class MarkdownReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data)))
        markdown = f"# {data.__class__.__name__} Report\n\n"
        for field in fields:
            value = self._to_serializable(getattr(data, field))
            markdown += f"## {field.capitalize()}\n"
            markdown += self._format_value(value) + "\n\n"
        return markdown

    def _format_value(self, value):
        """
        Вспомогательная функция для форматирования данных в Markdown
        """
        if isinstance(value, list):
            return '\n'.join(f"- {self._format_value(v)}" for v in value)
        elif isinstance(value, dict):
            return '\n'.join(f"**{k}**: {self._format_value(v)}" for k, v in value.items())
        else:
            return str(value)
