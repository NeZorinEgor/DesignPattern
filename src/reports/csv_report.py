import csv
from io import StringIO
from src.core.report import ABCReport


class CSVReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        fields = list(
            filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data))
        )

        # Создаем буфер для записи CSV
        output = StringIO()
        writer = csv.writer(output)

        # Записываем заголовки
        writer.writerow(fields)

        # Записываем данные
        writer.writerow(self._to_serializable(getattr(data, field)) for field in fields)

        # Возвращаем результат в формате CSV
        return output.getvalue()
