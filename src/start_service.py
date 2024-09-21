from src.errors.validator import Validator
from src.models.recipe import Recipe
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

    def create(self):
        meter_range = Range(name="Грамм", conversion_factor=1.0)

        length_group = GroupNomenclature()

        nomenclature = Nomenclature()
        nomenclature.name = "Линейка"
        nomenclature._Nomenclature__range = meter_range
        nomenclature._Nomenclature__group = length_group

        self.__repository.data["nomenclature"] = nomenclature
        self.__repository.data["range"] = meter_range
        self.__repository.data["group"] = length_group

        print("Данные успешно созданы и сохранены в репозитории.")

    def create_receipts(self):
        recipe1 = Recipe(
            name="Паста",
            ingredients=["200 г пасты", "1 л воды", "1 ч.л. соли", "1 ст.л. масла"],
            instructions="Сварите пасту в подсоленной воде."
        )

        recipe2 = Recipe(
            name="Салат",
            ingredients=["2 огурца", "3 помидора", "2 ст.л. масла", "по вкусу соль"],
            instructions="Нарежьте овощи и заправьте маслом."
        )

        self.__repository.data["recipes"] = [recipe1, recipe2]

        print("Рецепты успешно созданы и сохранены в репозитории.")

