from src.contracts.base_model import BaseModel
from src.models.group_nomenclature import GroupNomenclature
from src.models.range import Range


class Nomenclature(BaseModel):
    __name: str = ""
    __group = None
    __range = None

    def __init__(
            self,
            name: str = "",
            group: GroupNomenclature = None,
            range_unit: Range = None
    ):
        super().__init__()
        self.__name = name
        self.__group = group
        self.__range = range_unit

    def local_eq(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
