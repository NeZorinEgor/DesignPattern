from src.contracts.base_model import BaseModel


class GroupNomenclature(BaseModel):
    def __init__(self, nomenclature_type):
        super().__init__()
        self.__nomenclature_type = nomenclature_type

    def local_eq(self, other):
        pass

    def create_base_group(self):
        return GroupNomenclature(self.__nomenclature_type)

