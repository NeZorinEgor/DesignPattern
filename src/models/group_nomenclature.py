from src.core.model import BaseModel
from src.errors.validator import Validator


class GroupNomenclature(BaseModel):
    __nomenclature_type = ""

    def __init__(self, nomenclature_type="No group"):
        super().__init__()
        Validator.validate(nomenclature_type, type_=str)
        self.__nomenclature_type = nomenclature_type

    def local_eq(self, other):
        return self.__nomenclature_type == other.__nomenclature_type

    @staticmethod
    def create_base_group():
        return GroupNomenclature()

    def __str__(self):
        return f"Группа номенклатуры: {self.__nomenclature_type}, UUID: {self.uuid}"
