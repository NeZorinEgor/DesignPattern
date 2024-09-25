import os

from src.core.report import FormatEnum
from src.models.ingredient import Ingredient
from src.models.nomenclature import Nomenclature
from src.models.range import Range, piece, gram, tablespoon
from src.models.recipe import Recipe
from src.report import ReportFactory
from src.settings_manager import SettingsManager

ingredients2 = [
    Ingredient(range=piece, nomenclature=Nomenclature.create("Огурцы", group="Овощи"), quantity=2),
    Ingredient(range=piece, nomenclature=Nomenclature.create("Помидоры", group="Овощи"), quantity=3),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Оливки", group="Закуски"), quantity=50),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Фета", group="Молочные продукты"), quantity=100),
    Ingredient(range=tablespoon, nomenclature=Nomenclature.create("Оливковое масло", group="Приправы"), quantity=2),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Соль", group="Приправы"), quantity=0),  # По вкусу
    Ingredient(range=gram, nomenclature=Nomenclature.create("Перец", group="Приправы"), quantity=0),  # По вкусу
]

# Шаги приготовления
steps2 = [
    "Нарежьте огурцы и помидоры крупными кубиками.",
    "Добавьте оливки и фету.",
    "Полейте оливковым маслом, посолите и поперчите по вкусу.",
    "Перемешайте и подавайте.",
]

# Создание рецепта
salad_recipe = Recipe(
    name="ГРЕЧЕСКИЙ САЛАТ",
    ingredients=ingredients2,
    steps=steps2,
    cooking_time_by_min=15  # Время приготовления
)

settings_manager = SettingsManager()
report_fabric = ReportFactory(settings_manager.settings)


def test_create_report_files():
    dir_to_save = os.path.join(os.pardir, "docs", "reports")
    os.makedirs(dir_to_save, exist_ok=True)  # Создаем папку, если она не существует
    formats = {
        FormatEnum.CSV: "report.csv",
        FormatEnum.MARKDOWN: "report.md",
        FormatEnum.JSON: "report.json",
        FormatEnum.XML: "report.xml",
        FormatEnum.RTF: "report.rtf"
    }

    for report_format, file_name in formats.items():
        settings_manager.settings.report_format = report_format  # Устанавливаем формат
        report_content = report_fabric.create(salad_recipe)
        file_path = os.path.join(dir_to_save, file_name)

        with open(file_path, mode="w") as report_file:
            report_file.write(report_content)

        # Проверяем, что файл был создан
        assert os.path.exists(file_path)

