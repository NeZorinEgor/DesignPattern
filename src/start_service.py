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
