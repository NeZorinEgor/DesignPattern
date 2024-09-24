from src.core.model import BaseModel


class GroupNomenclature(BaseModel):
    __nomenclature_type = ""

    def __init__(self, nomenclature_type=""):
        super().__init__()
        self.__nomenclature_type = nomenclature_type

    def local_eq(self, other):
        pass

    @staticmethod
    def create_base_group():
        return GroupNomenclature()

    def __str__(self):
        return f"Группа номенклатуры: {self.__nomenclature_type}, UUID: {self.uuid}"
