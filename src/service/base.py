from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.group_nomenclature import GroupNomenclature


class StartService:
    __data = {}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = object.__new__(cls)
        return cls.instance

    def create(self) -> (Nomenclature, Range, GroupNomenclature):
        ...
