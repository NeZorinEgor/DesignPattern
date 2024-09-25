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
        rtf_content += r"\viewkind4\uc1\pard\fs20 Recipe Report\par"

        # Записываем данные
        for field in fields:
            value = self._to_serializable(getattr(data, field))
            rtf_content += r"\b " + field + r":\b0 " + str(value) + r"\par"

        # Завершение документа
        rtf_content += r"}"

        return rtf_content
