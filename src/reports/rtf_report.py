from src.core.report import ABCReport


class RTFReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        fields = list(
            filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data))
        )

        # Начало RTF документа
        rtf_content = r"{\rtf1\ansi\ansicpg1251\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Arial;}}"
        rtf_content += r"{\*\generator Riched20 10.0.18362;}"

        # Заголовок
        rtf_content += r"\viewkind4\uc1\pard\fs20\b Recipe Report\b0\par"

        # Записываем данные
        for field in fields:
            value = self._to_serializable(getattr(data, field))
            rtf_content += r"\b " + field + r":\b0 "
            rtf_content += self._format_rtf_value(value) + r"\par"

        # Завершение документа
        rtf_content += r"}"

        return rtf_content

    def _format_rtf_value(self, value, indent=0):
        """
        Форматирование значений для RTF-документа с рекурсивной обработкой списков и словарей
        """
        if isinstance(value, list):
            result = ""
            for idx, item in enumerate(value):
                result += r"\pard" + r"\tx" + str(indent * 200) + r"\fi" + str(indent * 200)
                result += r"\b item" + str(idx) + r":\b0 " + self._format_rtf_value(item, indent + 1) + r"\par"
            return result
        elif isinstance(value, dict):
            result = ""
            for k, v in value.items():
                result += r"\pard" + r"\tx" + str(indent * 200) + r"\fi" + str(indent * 200)
                result += r"\b " + k + r":\b0 " + self._format_rtf_value(v, indent + 1) + r"\par"
            return result
        else:
            return str(value)
