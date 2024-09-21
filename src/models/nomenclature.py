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
