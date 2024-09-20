from src.contracts.model import BaseModel


class GroupNomenclature(BaseModel):
    __nomenclature_type = ""

    def __init__(self):
        super().__init__()

    def local_eq(self, other):
        pass

    @staticmethod
    def create_base_group():
        return GroupNomenclature()

