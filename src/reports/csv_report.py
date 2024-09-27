import csv
from io import StringIO
from src.core.report import ABCReport


class CSVReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data)))
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(fields)
        writer.writerow([self._format_value(getattr(data, field)) for field in fields])
        return output.getvalue()

    def _format_value(self, value):
        """
        Вспомогательная функция для обработки значений в строковый вид для CSV
        """
        if isinstance(value, list):
            return '; '.join(self._format_value(v) for v in value)
        elif isinstance(value, dict):
            return '; '.join(f'{k}: {self._format_value(v)}' for k, v in value.items())
        else:
            return str(value)
