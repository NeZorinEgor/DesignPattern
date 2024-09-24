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

    @property
    def format(self):
        return self.__format



