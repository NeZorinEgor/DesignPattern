from src.errors.validator import Validator
from src.models.ingredient import Ingredient
from src.settings_manager import SettingsManager
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range, gram, milliliter, piece, teaspoon, tablespoon
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
        ingredients = [
            Ingredient(range=gram, nomenclature=Nomenclature.create("Пшеничная мука", group="бакалея"), quantity=200),
            Ingredient(range=milliliter, nomenclature=Nomenclature.create("Молоко", group="Молочные продукты"),
                       quantity=300),
            Ingredient(range=piece, nomenclature=Nomenclature.create("Яйца", group="Дairy"), quantity=2),
            Ingredient(range=gram, nomenclature=Nomenclature.create("Сахар", group="Бакалея"), quantity=50),
            Ingredient(range=gram, nomenclature=Nomenclature.create("Разрыхлитель теста", group="Бакалея"),
                       quantity=10),
            Ingredient(range=teaspoon, nomenclature=Nomenclature.create("Соль", group="Приправы"), quantity=0.5),
            # 1/2 чайной ложки
            Ingredient(range=gram, nomenclature=Nomenclature.create("Черника", group="Фрукты"), quantity=150),
            Ingredient(range=gram, nomenclature=Nomenclature.create("Сливочное масло", group="Молочные продукты"),
                       quantity=30),
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
