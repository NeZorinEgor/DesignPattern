from src.core.model import BaseModel


class GroupNomenclature(BaseModel):
    __name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def local_eq(self, other):
        return self.__name == other.__name

    @staticmethod
    def create(name="Сырье"):
        item = GroupNomenclature()
        item.__name = name
        return item

    def __str__(self):
        return f"{self.__name}, uuid: {self.uuid}"
