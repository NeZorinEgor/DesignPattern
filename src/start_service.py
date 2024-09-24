from src.errors.validator import Validator
from src.models.ingredient import Ingredient
from src.settings_manager import SettingsManager
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.recipe import Recipe


class StartService:
    def __init__(self, repository: DataRepository, settings_manager: SettingsManager):
        Validator.validate(repository, DataRepository)
        Validator.validate(settings_manager, SettingsManager)
        self.__repository = repository
        self.__settings_manager = settings_manager

    @property
    def settings(self):
        return self.__settings_manager.settings

    def create_nomenclature(self):
        """
        Фабричный метод для создания номенклатуры.
        """
        nomenclature = Nomenclature()
        nomenclature.name = "Товар A"
        self.__repository.data["nomenclature"] = nomenclature
        print("Номенклатура успешно создана и сохранена в репозиторий.")

    def create_group(self):
        """
        Фабричный метод для создания группы.
        """
        group = GroupNomenclature.create_base_group()
        self.__repository.data["group"] = group
        print("Группа успешно создана и сохранена в репозиторий.")

    def create_units(self):
        """
        Фабричный метод для создания единиц измерения.
        """
        gram = Range(name="Грамм", conversion_factor=1.0)  # Грамм как базовая единица
        kilogram = Range(name="Килограмм", conversion_factor=1000.0, base_unit=gram)  # Килограмм как производная
        self.__repository.data["ranges"] = {"gram": gram, "kilogram": kilogram}
        print("Единицы измерения успешно созданы и сохранены в репозиторий.")

    def create_recipes(self):
        """
        Фабричный метод для создания рецептов.
        """
        # Создаем базовые единицы измерения
        gram = Range(name="gram", conversion_factor=1.0)
        milliliter = Range(name="milliliter", conversion_factor=1.0)
        piece = Range(name="piece", conversion_factor=1.0)
        teaspoon = Range(name="teaspoon", conversion_factor=1.0)  # Чайная ложка
        tablespoon = Range(name="tablespoon", conversion_factor=1.0)  # Столовая ложка

        # Рецепт панкейков
        pancake_recipe = Recipe(
            name="Панкейки с черникой",
            ingredients=[
                Ingredient(name="Пшеничная мука", unit=Range(name="kg", base_unit=gram, conversion_factor=200)),
                Ingredient(name="Молоко", unit=Range(name="milliliter", base_unit=milliliter, conversion_factor=300)),
                Ingredient(name="Яйца", unit=Range(name="piece", base_unit=piece, conversion_factor=2)),
                Ingredient(name="Сахар", unit=Range(name="gram", base_unit=gram, conversion_factor=50)),
                Ingredient(name="Разрыхлитель теста", unit=Range(name="gram", base_unit=gram, conversion_factor=10)),
                Ingredient(name="Соль", unit=Range(name="teaspoon", base_unit=teaspoon, conversion_factor=0.5)),
                Ingredient(name="Черника", unit=Range(name="gram", base_unit=gram, conversion_factor=150)),
                Ingredient(name="Сливочное масло", unit=Range(name="gram", base_unit=gram, conversion_factor=30)),
            ],
        )

        # Рецепт греческого салата
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
                Ingredient(name="Перец", unit=Range(name="taste", conversion_factor=1.0)),  # "по вкусу"
            ],
        )

        self.__repository.data["recipes"] = [pancake_recipe, salad_recipe]
        print("Рецепты успешно созданы и сохранены в репозиторий.")

    def create(self):
        """
        Основной метод для создания данных: номенклатур, групп, единиц измерения и рецептов.
        """
        self.create_nomenclature()
        self.create_group()
        self.create_units()
        self.create_recipes()
