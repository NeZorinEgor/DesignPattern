import xml.etree.ElementTree as ET
from src.core.report import ABCReport


class XMLReport(ABCReport):
    def __init__(self):
        super().__init__()

    def create(self, data):
        fields = list(
            filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data))
        )

        # Создаем корневой элемент
        root = ET.Element('Recipe')

        # Заполняем элемент данными
        for field in fields:
            value = self._to_serializable(getattr(data, field))
            field_element = ET.SubElement(root, field)
            field_element.text = str(value)

        # Создаем дерево и преобразуем его в строку
        xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')

        # Добавляем заголовок XML
        return f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_str}'
