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
            self._add_value_to_element(field_element, value)

        # Создаем дерево и преобразуем его в строку
        xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')

        # Добавляем заголовок XML
        return f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_str}'

    def _add_value_to_element(self, parent, value):
        """
        Рекурсивное добавление значений в XML-элемент
        """
        if isinstance(value, list):
            for idx, item in enumerate(value):
                item_element = ET.SubElement(parent, f'item{idx}')
                self._add_value_to_element(item_element, item)
        elif isinstance(value, dict):
            for k, v in value.items():
                sub_element = ET.SubElement(parent, k)
                self._add_value_to_element(sub_element, v)
        else:
            parent.text = str(value)
