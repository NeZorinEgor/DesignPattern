import json
import os

from src.errors.base import InvalidTypeError, InvalidLengthError
from src.errors.proxy import ErrorProxy
from src.models.settings import Settings


class SettingsManager:
    """ Класс для управления настройками. """

    file_name = "settings.json"
    __settings = Settings()

    def __new__(cls):
        # Singleton pattern
        if not hasattr(cls, 'instance'):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.error_proxy = ErrorProxy()

    def set_exception(self, ex: Exception):
        """ Установка исключения в ErrorProxy """
        self.error_proxy = ErrorProxy(ex)

    @property
    def settings(self) -> Settings:
        return self.__settings

    def from_json(self, path: str = os.path.join(os.pardir, file_name)) -> None:
        """ Установка полей класса Settings из Json файла. По умолчанию берется файл ../settings.json, можно указать полный путь. """
        try:
            # Проверки на входные значения
            if not isinstance(path, str):
                raise InvalidTypeError("File path should be a string")
            if not os.path.exists(path):
                raise FileNotFoundError(f"File {path} does not exist")

            # Чтений json файла и заполнение полей класса
            with open(path, "r", encoding="utf-8") as f:
                file = json.load(f)
                for key, value in file.items():
                    if hasattr(self.__settings, key):
                        setattr(self.__settings, key, value)
        except Exception as ex:
            self.set_exception(ex)
            raise

    def from_dict(self, input_dict: dict) -> None:
        """ Установка полей класса Settings из dict'а. """
        try:
            if not isinstance(input_dict, dict):
                raise InvalidTypeError("Input data should be a dict")

            # Чтений словаря и заполнение полей класса
            for key, value in input_dict.items():
                if hasattr(self.__settings, key):
                    setattr(self.__settings, key, value)

            # Пример дополнительной проверки длины (настраиваемое правило):
            if len(input_dict) > 100:
                raise InvalidLengthError("Input dictionary is too long")
        except Exception as ex:
            self.set_exception(ex)
            raise
