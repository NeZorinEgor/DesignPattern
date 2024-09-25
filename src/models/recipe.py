from typing import List
from src.core.model import BaseModel
from src.errors.validator import Validator
from src.models.ingredient import Ingredient


class Recipe(BaseModel):
    __name: str
    __ingredients: List[Ingredient]   # Список объектов Ingredient
    __steps: List[str]
    __cooking_time_by_min: float | int

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validator.validate(value, type_=str)
        self.__name = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: List[Ingredient]):
        Validator.validate(value, type_=List[Ingredient])
        self.__ingredients = value

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value: List[str]):
        Validator.validate(value, type_=List[str])
        self.__steps = value

    @property
    def cooking_time_by_min(self):
        return self.__cooking_time_by_min

    @cooking_time_by_min.setter
    def cooking_time_by_min(self, value: float | int):
        Validator.validate(value, type_=int | float)
        self.__cooking_time_by_min = value

    @staticmethod
    def create(name: str, ingredients: List[Ingredient], steps: List[str], cooking_time_by_min: float | int):
        recipe = Recipe()
        recipe.name = name
        recipe.ingredients = ingredients
        recipe.steps = steps
        recipe.cooking_time_by_min = cooking_time_by_min
        return recipe

    def local_eq(self, other):
        return self.name == other.name and self.ingredients == other.ingredients

    def __eq__(self, other):
        return self.name == other.name and self.ingredients == other.ingredients

    def __str__(self):
        ingredients_str = "\n".join(str(ingredient) for ingredient in self.ingredients)
        steps_str = "\n".join(f"{i + 1}. {step}" for i, step in enumerate(self.steps))

        return f"Рецепт: {self.name}\n" \
               f"Ингредиенты: \n{ingredients_str}\n" \
               f"Время приготовления: {self.cooking_time_by_min} минут\n" \
               f"Шаги приготовления:\n{steps_str}"
