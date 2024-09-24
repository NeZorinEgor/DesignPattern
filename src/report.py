import json
from xml.etree.ElementTree import tostring, Element

from src.core.report import ABCReport, FormatEnum
from src.errors.validator import Validator
from src.models.ingredient import Ingredient
from src.models.range import Range, piece, gram, tablespoon
from src.models.recipe import Recipe


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
                value = "[" + ", ".join(str(item) for item in value) + "]"
            else:
                value = str(value)
            values.append(value)
        values_str = ";".join(values)
        print(header)
        print(values_str)


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
        # Формирование JSON
        fields = {field: getattr(data, field) for field in vars(data).keys() if not field.startswith("_")}
        # Преобразование в строку JSON
        return json.dumps(fields, indent=4, ensure_ascii=False, default=str)


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
                child.text = ", ".join(str(item) for item in value)
            else:
                child.text = str(value)
            root.append(child)

        # Преобразование в строку XML
        return tostring(root, encoding="unicode")


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
    @staticmethod
    def create(report_format):
        Validator.validate(report_format, FormatEnum)
        match report_format:
            case FormatEnum.CSV:
                return CSVReport()
            case FormatEnum.MARKDOWN:
                return MarkdownReport()
            case FormatEnum.JSON:
                return JSONReport()
            case FormatEnum.XML:
                return XMLReport()
            case FormatEnum.RTF:
                return RTFReport()
            case _:
                raise ValueError("Неподдерживаемый формат отчета")


salad_recipe = Recipe(
            name="Греческий салат",
            ingredients=[
                Ingredient(name="Огурцы", unit=Range(name="piece", base_unit=piece, conversion_factor=2)),
                Ingredient(name="Помидоры", unit=Range(name="piece", base_unit=piece, conversion_factor=3)),
                Ingredient(name="Оливки", unit=Range(name="gram", base_unit=gram, conversion_factor=50)),
                Ingredient(name="Фета", unit=Range(name="gram", base_unit=gram, conversion_factor=100)),
                Ingredient(name="Оливковое масло",
                           unit=Range(name="tablespoon", base_unit=tablespoon, conversion_factor=2)),
                Ingredient(name="Соль", unit=Range(name="taste", conversion_factor=1.0)),
                # "по вкусу" — условная единица
                Ingredient(name="Перец", unit=Range(name="taste", conversion_factor=1.0)),
            ],
        )

report_fabric = ReportFactory()

print(report_fabric.create(FormatEnum.CSV).create(salad_recipe))
print(report_fabric.create(FormatEnum.MARKDOWN).create(salad_recipe))
print(report_fabric.create(FormatEnum.JSON).create(salad_recipe))
print(report_fabric.create(FormatEnum.XML).create(salad_recipe))
print(report_fabric.create(FormatEnum.RTF).create(salad_recipe))


