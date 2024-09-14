import json
import os
from src.models.settings import Settings
from src.errors.proxy import ErrorProxy


class SettingsManager:
    """ Класс для управления настройками. """

    file_name = "settings.json"
    __settings = Settings()
    _error = ErrorProxy()

    def __new__(cls):
        # Singleton pattern
        if not hasattr(cls, 'instance'):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def error(self) -> ErrorProxy:
        return self._error

    def from_json(self, path: str = os.path.join(os.pardir, file_name)) -> None:
        """ Установка полей класса Settings из Json файла. По умолчанию берется файл ../settings.json, можно указать полный путь. """
        # Проверки на входные значения
        try:
            if not isinstance(path, str):
                raise TypeError("File path should be a string")
            if not os.path.exists(path):
                raise FileNotFoundError(f"File {path} does not exist")

            # Чтение json файла и заполнение полей класса
            with open(path, "r", encoding="utf-8") as f:
                file = json.load(f)
                for key, value in file.items():
                    if hasattr(self.__settings, key):
                        setattr(self.__settings, key, value)

        except Exception as e:
            self._error.set_error(e)

    def from_dict(self, input_dict: dict) -> None:
        """ Установка полей класса Settings из dict'а. """
        try:
            if not isinstance(input_dict, dict):
                raise TypeError("Var should be a dict")

            # Чтение словаря и заполнение полей класса
            for key, value in input_dict.items():
                if hasattr(self.__settings, key):
                    setattr(self.__settings, key, value)

        except Exception as e:
            self._error.set_error(e)
