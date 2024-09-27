import json
from src.core.report import ABCReport


class JSONReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data)))
        result = {field: self._to_serializable(getattr(data, field)) for field in fields}
        # Возвращаем результат в формате JSON
        return json.dumps(result, indent=3, ensure_ascii=False)
