from src.errors.validator import Validator
from src.models.recipe import LessonRecipe, PersonalRecipe
from src.settings_manager import SettingsManager
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range


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

    def create_receipts(self, personal_recipe_data, lesson_recipe_data=None):
        """
        Формирует и сохраняет рецепты в зависимости от переданных данных.

        :param personal_recipe_data: словарь с данными для личного рецепта
        :param lesson_recipe_data: словарь с данными для рецепта на занятии (опционально)
        """

        # Создание личного рецепта
        personal_recipe = PersonalRecipe(
            name=personal_recipe_data["name"],
            ingredients=personal_recipe_data["ingredients"],
            instructions=personal_recipe_data["instructions"]
        )

        # Сохранение личного рецепта в репозиторий
        self.__repository.add_recipe(personal_recipe)

        # Если переданы данные для рецепта занятия, создаем и сохраняем его
        if lesson_recipe_data:
            lesson_recipe = LessonRecipe(
                name=lesson_recipe_data["name"],
                ingredients=lesson_recipe_data["ingredients"],
                instructions=lesson_recipe_data["instructions"],
                lesson_topic=lesson_recipe_data["lesson_topic"]
            )
            self.__repository.add_recipe(lesson_recipe)

        print("Рецепты успешно созданы и сохранены в репозиторий.")

    def create(self, personal_recipe_data, lesson_recipe_data=None):
        """
        Основной метод для создания данных. Вызывает создание рецептов, номенклатур, единиц измерения и групп.
        :param personal_recipe_data: данные для создания личного рецепта
        :param lesson_recipe_data: данные для создания рецепта занятия (опционально)
        """

        # Генерация данных для рецептов
        self.create_receipts(personal_recipe_data, lesson_recipe_data)

        # Генерация данных для номенклатур
        nomenclature = Nomenclature()
        nomenclature.name = "Товар A"
        self.__repository.data["nomenclature"] = nomenclature

        # Генерация данных для групп
        group = GroupNomenclature.create_base_group()
        self.__repository.data["group"] = group

        # Генерация данных для единиц измерения
        kilogram = Range(name="Килограмм", conversion_factor=1.0)
        gram = Range(name="Грамм", conversion_factor=0.001, base_unit=kilogram)
        self.__repository.data["ranges"] = {"kilogram": kilogram, "gram": gram}

        print("Номенклатура, группы и единицы измерения успешно созданы и сохранены в репозиторий.")
