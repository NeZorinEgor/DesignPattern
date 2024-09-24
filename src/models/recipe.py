from typing import List

from src.core.model import BaseModel
from src.errors.validator import Validator
from src.models.ingredient import Ingredient



class Recipe(BaseModel):
    def __init__(self, name, ingredients, steps, cooking_time_by_min):
        super().__init__()
        Validator.validate(name, type_=str)
        Validator.validate(ingredients, type_=List[Ingredient])
        Validator.validate(steps, type_=List[str])
        Validator.validate(cooking_time_by_min, type_=int | float)
        self.name = name
        self.ingredients: list[Ingredient] = ingredients
        self.steps = steps
        self.cooking_time_by_min = cooking_time_by_min

    def local_eq(self, other):
        return self.name == other.name and self.ingredients == other.ingredients

    def __str__(self):
        ingredients_str = ", ".join(str(ingredient) for ingredient in self.ingredients)
        steps_str = "\n".join(f"{i + 1}. {step}" for i, step in enumerate(self.steps))

        return f"Рецепт: {self.name}\n" \
               f"Ингредиенты: {ingredients_str}\n" \
               f"Время приготовления: {self.cooking_time_by_min}\n" \
               f"Шаги приготовления:\n{steps_str}"
