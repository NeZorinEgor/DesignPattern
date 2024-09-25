from abc import ABC, abstractmethod
from enum import Enum


class FormatEnum(Enum):
    CSV = 1
    MARKDOWN = 2
    JSON = 3
    XML = 4
    RTF = 5


class ABCReport(ABC):
    """
    Абстрактный класс для отчётов
    """
    __format: FormatEnum = FormatEnum.CSV

    @staticmethod
    @abstractmethod
    def create(data):
        pass

    def _to_serializable(self, val):
        """
        Вспомогательная функция для рекурсивного преобразования объектов в строковые представления
        """
        if isinstance(val, dict):
            return {str(k): self._to_serializable(v) for k, v in val.items()}
        elif isinstance(val, list):
            return [self._to_serializable(v) for v in val]
        elif hasattr(val, '__dict__'):
            return {key: self._to_serializable(value) for key, value in val.__dict__.items()}
        elif hasattr(val, '__str__'):
            return str(val)
        else:
            return val

    @property
    def format(self):
        return self.__format



