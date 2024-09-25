import json
import os.path
from xml.etree.ElementTree import tostring, Element

from src.core.report import ABCReport, FormatEnum
from src.data_repository import DataRepository
from src.errors.proxy import ErrorProxy
from src.errors.validator import Validator
from src.models.settings import Settings

from src.settings_manager import SettingsManager
from src.start_service import StartService


class CSVReport(ABCReport):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create(data):
        # Поля класса
        fields = list(filter(lambda x: not x.startswith("_"), vars(data).keys()))
        header = ";".join(fields)

        # Формирование значений
        values = []
        for field in fields:
            value = getattr(data, field)
            if isinstance(value, list):
                if field == 'ingredients':
                    # Обработка списка ингредиентов
                    value = "[" + "; ".join(
                        f"{ingredient.nomenclature.name}: {ingredient.quantity} {ingredient.range}"
                        for ingredient in value
                    ) + "]"
                else:
                    value = "[" + ", ".join(str(item) for item in value) + "]"
            else:
                value = str(value)
            values.append(value)

        values_str = ";".join(values)
        return f"{header}\n{values_str}"


class MarkdownReport(ABCReport):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create(data):
        fields = list(filter(lambda x: not x.startswith("_"), vars(data).keys()))
        header = " | ".join(fields)
        separator = " | ".join(["---"] * len(fields))
        # Формирование значений
        values = []
        for field in fields:
            value = getattr(data, field)
            if isinstance(value, list):
                value = "[" + ", ".join(str(item) for item in value) + "]"
            else:
                value = str(value)
            values.append(value)
        values_str = " | ".join(values)  # Значения для таблицы Markdown

        # Формируем Markdown-строку
        markdown_str = f"# {data.name}\n\n"
        markdown_str += header + "\n" + separator + "\n" + values_str + "\n"
        return markdown_str


class JSONReport(ABCReport):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create(data):
        fields = {field: getattr(data, field) for field in vars(data).keys() if not field.startswith("_")}
        return [i for i in vars(data).keys()]
        # fields = {
        #     field: getattr(data, field) if field != 'ingredients' else [ingredient.to_dict() for ingredient in
        #                                                                 data.ingredients]
        #     for field in vars(data).keys() if not field.startswith("_")
        # }
        # return json.dumps(fields, indent=3, ensure_ascii=False, default=str)


class XMLReport(ABCReport):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create(data):
        # Создание корневого элемента
        root = Element("data")
        fields = {field: getattr(data, field) for field in vars(data).keys() if not field.startswith("_")}

        # Формирование XML
        for key, value in fields.items():
            child = Element(key)
            if isinstance(value, list):
                if key == 'ingredients':
                    # Обработка списка ингредиентов
                    for ingredient in value:
                        ingredient_element = Element("ingredient")
                        ingredient_element.set("name", ingredient.nomenclature.name)
                        ingredient_element.set("quantity", str(ingredient.quantity))
                        ingredient_element.set("unit", ingredient.range.name)
                        child.append(ingredient_element)
                else:
                    child.text = ", ".join(str(item) for item in value)
            else:
                child.text = str(value)
            root.append(child)

        # Преобразование в строку XML с заголовком
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        return xml_declaration + tostring(root, encoding="unicode")


class RTFReport(ABCReport):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create(data):
        fields = list(filter(lambda x: not x.startswith("_"), vars(data).keys()))
        # Заголовок в RTF
        rtf_header = "{\\rtf1\\ansi\n"
        # Формирование таблицы
        rtf_content = "{\\b " + "\\cell ".join(fields) + " \\row\n"

        # Формирование значений
        for field in fields:
            value = getattr(data, field)
            if isinstance(value, list):
                value = ", ".join(str(item) for item in value)
            else:
                value = str(value)
            rtf_content += value + " \\cell "
        rtf_content += "\\row\n}"

        # Формирование полного RTF-документа
        return rtf_header + rtf_content + "\n}"


class ReportFactory:
    report_classes = {
        FormatEnum.CSV: CSVReport,
        FormatEnum.MARKDOWN: MarkdownReport,
        FormatEnum.JSON: JSONReport,
        FormatEnum.XML: XMLReport,
        FormatEnum.RTF: RTFReport,
    }

    def __init__(self, settings: Settings):
        self.settings = settings
        self.error_proxy = ErrorProxy()

    @staticmethod
    def set_format(report_format):
        Validator.validate(report_format, FormatEnum)

        report_class = ReportFactory.report_classes.get(report_format)
        if report_class is None:
            raise ValueError("Неподдерживаемый формат отчета")

        return report_class()

    def create(self, data):
        """Создает отчет в зависимости от текущих настроек."""
        try:
            report_format = self.settings.report_format
            report_class = self.set_format(report_format)
            return report_class.create(data)
        except Exception as e:
            self.error_proxy.error_message = str(e)
            return None


settings_manager = SettingsManager()
settings_manager.from_json(os.path.join(os.pardir, "settings.json"))
repository = DataRepository()
service = StartService(repository)
service.create()
recipe = repository.data[DataRepository.recipe_id()][0]


factory = ReportFactory(settings_manager.settings)
factory.set_format(FormatEnum.JSON)
r = JSONReport()
print(r.create(recipe))
print(recipe)