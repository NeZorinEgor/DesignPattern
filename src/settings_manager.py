import json
import os

from src.errors import ErrorProxy, InvalidTypeError
from src.models.settings import Settings


class SettingsManager:
    """Класс для управления настройками с интеграцией ErrorProxy."""

    file_name = "settings.json"
    __settings = Settings()
    __error_proxy = ErrorProxy()

    def __new__(cls):
        # Singleton pattern
        if not hasattr(cls, 'instance'):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def error_proxy(self) -> ErrorProxy:
        return self.__error_proxy

    def set_exception(self, ex: Exception) -> None:
        """Устанавливает сообщение об ошибке в ErrorProxy."""
        self.__error_proxy.error_message = str(ex)
        raise ex

    def from_json(self, path: str = os.path.join(os.pardir, file_name)) -> None:
        try:
            if not isinstance(path, str):
                raise InvalidTypeError("File path should be a string")
            if not os.path.exists(path):
                raise FileNotFoundError(f"File {path} does not exist")

            with open(path, "r", encoding="utf-8") as f:
                file = json.load(f)
                for key, value in file.items():
                    if hasattr(self.__settings, key):
                        setattr(self.__settings, key, value)
        except Exception as ex:
            self.set_exception(ex)
            if not self.__error_proxy.is_empty:
                return

    def from_dict(self, input_dict: dict) -> None:
        """Установка полей класса Settings из dict'а."""
        try:
            if not isinstance(input_dict, dict):
                raise InvalidTypeError("Var should be a dict")

            for key, value in input_dict.items():
                if hasattr(self.__settings, key):
                    setattr(self.__settings, key, value)
        except Exception as ex:
            self.set_exception(ex)
