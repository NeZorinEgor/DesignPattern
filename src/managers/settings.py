import json
import os

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

    @property
    def settings(self) -> Settings:
        return self.__settings

    def from_json(self, path: str = os.path.join(os.pardir, file_name)) -> None:
        """ Установка полей класса Settings из Json файла. По умолчанию берется файл ../settings.json, можно указать полный путь. """
        # Проверки на входные значения
        if not isinstance(path, str):
            raise TypeError("File path should be a string")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")

        # Чтений json файла и заполнение полей класса
        with open(path, "r", encoding="utf-8") as f:
            file = json.load(f)
            for key, value in file.items():
                if hasattr(self.__settings, key):
                    setattr(self.__settings, key, value)

    def from_dict(self, input_dict: dict) -> None:
        """ Установка полей класса Settings из dict'а. """
        if not isinstance(input_dict, dict):
            raise TypeError("Var should be a dict")

        # Чтений словаря и заполнение полей класса
        for key, value in input_dict.items():
            if hasattr(self.__settings, key):
                setattr(self.settings, key, value)
