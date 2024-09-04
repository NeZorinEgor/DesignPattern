import json
import os

from models.settings import Settings


class SettingsManager:
    """ Класс для управления настройками. """
    file_name = "settings.json"
    __settings = Settings()

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(SettingsManager, cls).__new__(cls)
    #     return cls.instance

    @property
    def settings(self) -> Settings:
        return self.__settings

    def from_json(self, file_path: str = os.path.join(os.pardir, file_name)) -> None:
        """ По умолчанию берется файл ../settings.json, можно указать полный путь. """
        # Проверки на входные значения
        if not isinstance(file_path, str):
            raise TypeError("File path should be a string")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")

        # Чтений json файла и гибкое создание класса
        with open(file_path, "r", encoding="utf-8") as f:
            file = json.load(f)
            for key, value in file.items():
                if hasattr(self.__settings, key):
                    setattr(self.__settings, key, value)

    def from_dict(self, input_dict: dict) -> None:
        if not isinstance(input_dict, dict):
            raise TypeError("Var should be a dict")

        for key, value in input_dict.items():
            if hasattr(self.__settings, key):
                setattr(self.settings, key, value)
