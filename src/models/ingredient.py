from src.core.model import BaseModel
from src.models.range import Range


class Ingredient(BaseModel):
    def __init__(self, name: str, unit: Range):
        super().__init__()
        self.name = name
        self.unit = unit  # Свойство для хранения единицы измерения

    def local_eq(self, other: object) -> bool:
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False

    def __str__(self) -> str:
        return f"Ingredient(name={self.name}, unit={self.unit})"

    def __repr__(self) -> str:
        return f"Ingredient(name={self.name}, unit={repr(self.unit)})"
