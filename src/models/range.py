from src.core.model import BaseModel


class Range(BaseModel):
    __name = None
    __conversion_factor = None
    __base_unit = None

    def local_eq(self, other):
        return self.__base_unit == other.__base_unit and self.__name == other.__name

    @property
    def name(self):
        return self.__name

    @property
    def base_unit(self):
        return self.__base_unit

    def conversion_factor(self):
        return self.__conversion_factor

    def convert_to_base(self, value):
        return value * self.__conversion_factor

    def convert_from_base(self, value):
        return value / self.__conversion_factor

    def __str__(self):
        return f"{self.__name}"

    @staticmethod
    def create(name, conversion_factor, base_unit=None):
        item = Range()
        item.__name = name
        item.__conversion_factor = conversion_factor
        if base_unit is None:
            base = Range()
            base.__name = None
            base.__conversion_factor = None
            base.__base_unit = None
            item.__base_unit = base
        else:
            item.__base_unit = base
        return item
