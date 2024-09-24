from src.core.model import BaseModel


class Nomenclature(BaseModel):
    __name: str = ""
    __group = None

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

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, new_group) -> None:
        self.__group = new_group

    @staticmethod
    def create(name: str, group=None):
        item = Nomenclature()
        item.name = name
        item.group = group
        return item

    def __str__(self):
        group_str = str(self.__group) if self.__group else "No group"
        return f"Nomenclature: {self.__name}, Group: {group_str}"
