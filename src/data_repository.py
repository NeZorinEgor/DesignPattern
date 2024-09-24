from src.errors.custom import InvalidTypeError, InvalidLengthError
from src.errors.validator import Validator


class DataRepository:
    __data = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DataRepository, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def group_key():
        return "groups"

    @staticmethod
    def nomenclature_key():
        return "nomenclature"

    @staticmethod
    def unit_key():
        return "units"

    @staticmethod
    def receipt_key():
        return "receipts"

    @property
    def data(self):
        return self.__data

    def add_item(self, key, item):
        """
        Добавляет элемент в репозиторий по заданному ключу.
        Если ключ не существует, он создается как пустой список.
        """
        if key not in self.__data:
            self.__data[key] = []
        self.__data[key].append(item)

    def get_items(self, key):
        """Возвращает элементы по заданному ключу, если такие существуют."""
        return self.__data.get(key, [])

    def add_recipe(self, recipe):
        """Специальный метод для добавления рецептов."""
        Validator.validate(recipe, type_=dict)  # Пример валидации
        self.add_item(self.receipt_key(), recipe)

    def get_recipes(self):
        """Получает все рецепты."""
        return self.get_items(self.receipt_key())

    def add_group(self, group):
        """Метод для добавления групп."""
        Validator.validate(group, type_=dict)  # Пример валидации
        self.add_item(self.group_key(), group)

    def get_groups(self):
        """Получает все группы."""
        return self.get_items(self.group_key())

    def add_nomenclature(self, nomenclature):
        """Метод для добавления номенклатуры."""
        Validator.validate(nomenclature, type_=dict)  # Пример валидации
        self.add_item(self.nomenclature_key(), nomenclature)

    def get_nomenclature(self):
        """Получает всю номенклатуру."""
        return self.get_items(self.nomenclature_key())

    def add_unit(self, unit):
        """Метод для добавления единиц измерения."""
        Validator.validate(unit, type_=dict)  # Пример валидации
        self.add_item(self.unit_key(), unit)

    def get_units(self):
        """Получает все единицы измерения."""
        return self.get_items(self.unit_key())
