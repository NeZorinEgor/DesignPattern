from src.contracts.nomenclature import ABCNomenclature


class Nomenclature(ABCNomenclature):
    __name: str = ""

    def local_eq(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
