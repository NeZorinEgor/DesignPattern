from src.core.model import BaseModel
from src.errors.validator import Validator
from src.models.nomenclature import Nomenclature
from src.models.range import Range, gram


class Ingredient(BaseModel):
    def local_eq(self, other):
        return self.nomenclature == other.nomenclature

    def __init__(self, range: Range = None, nomenclature: Nomenclature = None, quantity: int | float = 0):
        super().__init__()
        Validator.validate(range, type_=Range)
        Validator.validate(nomenclature, type_=Nomenclature)
        Validator.validate(quantity, type_=int | float)   # как Optional
        self.__range = range
        self.__nomenclature = nomenclature
        self.__quantity = quantity

    def to_dict(self):
        return {
            "ingredient": self.nomenclature.name,
            "quantity": self.quantity,
            "range": str(self.range)
        }

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: Range):
        if not isinstance(value, Range):
            raise ValueError("Expected a Range instance.")
        self.__range = value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        if not isinstance(value, Nomenclature):
            raise ValueError("Expected a Nomenclature instance.")
        self.__nomenclature = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self.__quantity = value

    def __str__(self):
        return f"Ingredient: {self.nomenclature.name}, Quantity: {self.quantity}, Range: {self.range.base_unit}"
