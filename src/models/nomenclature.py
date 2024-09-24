from src.core.model import BaseModel


class Nomenclature(BaseModel):
    __name: str = ""
    __group = None
    __range = None

    def __init__(self):
        super().__init__()

    def local_eq(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        group_str = f"Группа: {self.__group}" if self.__group else "Группа: не указана"
        range_str = f"Единица измерения: {self.__range}" if self.__range else "Единица измерения: не указана"
        return f"Номенклатура: {self.name}, {group_str}, {range_str}"
