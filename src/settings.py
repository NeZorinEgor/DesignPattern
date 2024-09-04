import json
import os
from utils import singleton


@singleton
class Settings:
    _inn = ""
    _org_name = ""

    @property
    def inn(self):
        return self._inn

    @inn.setter
    def inn(self, new_inn):
        if not isinstance(new_inn, str):
            raise TypeError("INN must be a string")
        self._inn = new_inn

    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError("Organization name must be a string")
        self._org_name = new_name


@singleton
class SettingsManager:
    file_name = "settings.json"

    def __init__(self):
        self.__settings = Settings()

    def open(self, file_path: str):
        if not isinstance(file_path, str):
            raise TypeError("File path should be a string")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")

        with open(file_path, "r") as f:
            file = json.load(f)

            for k, v in file.items():
                if hasattr(self.__settings, k):
                    setattr(self.__settings, k, v)

    @property
    def settings(self):
        return self.__settings
