import json
import os.path
from xml.etree.ElementTree import tostring, Element

from src.core.report import ABCReport, FormatEnum
from src.errors.validator import Validator

from src.models.settings import Settings
from src.settings_manager import SettingsManager


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
        # Формирование JSON
        fields = {field: getattr(data, field) for field in vars(data).keys() if not field.startswith("_")}
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
    report_classes = {
        FormatEnum.CSV: CSVReport,
        FormatEnum.MARKDOWN: MarkdownReport,
        FormatEnum.JSON: JSONReport,
        FormatEnum.XML: XMLReport,
        FormatEnum.RTF: RTFReport,
    }

    def __init__(self, settings: Settings):
        self.settings = settings  # Инкапсуляция настроек

    @staticmethod
    def set_format(report_format):
        Validator.validate(report_format, FormatEnum)

        report_class = ReportFactory.report_classes.get(report_format)
        if report_class is None:
            raise ValueError("Неподдерживаемый формат отчета")

        return report_class()

    def create(self, data):
        """Создает отчет в зависимости от текущих настроек."""
        report_format = self.settings.report_format
        report_class = self.set_format(report_format)
        return report_class.create(data)


from src.models.ingredient import Ingredient
from src.models.nomenclature import Nomenclature
from src.models.range import gram, milliliter, piece, teaspoon
from src.models.recipe import Recipe

ingredients = [
    Ingredient(range=gram, nomenclature=Nomenclature.create("Пшеничная мука", group="бакалея"), quantity=200),
    Ingredient(range=milliliter, nomenclature=Nomenclature.create("Молоко", group="Молочные продукты"), quantity=300),
    Ingredient(range=piece, nomenclature=Nomenclature.create("Яйца", group="Яйца"), quantity=2),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Сахар", group="Бакалея"), quantity=50),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Разрыхлитель теста", group="Бакалея"), quantity=10),
    Ingredient(range=teaspoon, nomenclature=Nomenclature.create("Соль", group="Приправы"), quantity=0.5),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Черника", group="Ягода"), quantity=150),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Сливочное масло", group="Молочные продукты"), quantity=30),
]
steps = [
    "Подготовьте все ингредиенты. В глубокой миске смешайте муку, сахар, разрыхлитель и соль.",
    "В отдельной миске взбейте яйца и добавьте молоко. Хорошо перемешайте.",
    "Влейте яичную смесь в сухие ингредиенты и перемешайте до однородности. Постарайтесь не перебить тесто, небольшие комочки допустимы.",
    "В растопленное сливочное масло добавьте тесто и аккуратно перемешайте.",
    "Добавьте чернику в тесто и осторожно перемешайте, чтобы не повредить ягоды.",
    "Разогрейте сковороду на среднем огне и слегка смажьте ее маслом.",
    "Вылейте половник теста на сковороду. Готовьте до появления пузырьков на поверхности, затем переверните и жарьте до золотистого цвета.",
    "Повторяйте процесс, пока не израсходуете все тесто.",
    "Подавайте панкейки горячими, можно с медом или кленовым сиропом.",
]

pancake_recipe = Recipe(
    name="ПАНКЕЙКИ С ЧЕРНИКОЙ",
    ingredients=ingredients,
    steps=steps,
    cooking_time_by_min=25
)

manager = SettingsManager()
manager.from_json(os.path.join(os.pardir, "settings.json"))
manager.settings.report_format = FormatEnum.JSON
factory = ReportFactory(manager.settings)
print(factory.create(pancake_recipe))

