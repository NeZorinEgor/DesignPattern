from src.errors.validator import Validator
from src.settings_manager import SettingsManager
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.recipe import Recipe


class StartService:
    __repository: DataRepository = None
    __settings_manager: SettingsManager = None

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
        pancake_recipe = Recipe(
            name="Панкейки с черникой",
            ingredients={
                "Пшеничная мука": "200 гр",
                "Молоко": "300 мл",
                "Яйца": "2 шт",
                "Сахар": "50 гр",
                "Разрыхлитель теста": "10 гр",
                "Соль": "1/2 ч.л.",
                "Черника": "150 гр",
                "Сливочное масло": "30 гр"
            },
            instructions="""
                1. Подготовьте все ингредиенты. В глубокой миске смешайте муку, сахар, разрыхлитель и соль.
                2. В отдельной миске взбейте яйца и добавьте молоко. Хорошо перемешайте.
                3. Влейте яичную смесь в сухие ингредиенты и перемешайте до однородности.
                4. В растопленное сливочное масло добавьте тесто и аккуратно перемешайте.
                5. Добавьте чернику в тесто и осторожно перемешайте.
                6. Разогрейте сковороду и готовьте панкейки до золотистого цвета.
            """
        )

        salad_recipe = Recipe(
            name="Греческий салат",
            ingredients={
                "Огурцы": "2 шт",
                "Помидоры": "3 шт",
                "Оливки": "50 гр",
                "Фета": "100 гр",
                "Оливковое масло": "2 ст.л.",
                "Соль": "по вкусу",
                "Перец": "по вкусу"
            },
            instructions="""
                1. Нарежьте огурцы и помидоры крупными кубиками.
                2. Добавьте оливки и фету.
                3. Полейте оливковым маслом, посолите и поперчите по вкусу.
                4. Перемешайте и подавайте.
            """
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
