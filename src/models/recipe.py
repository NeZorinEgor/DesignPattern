from src.core.model import BaseModel


class Recipe(BaseModel):
    def __init__(self, name, ingredients, instructions):
        super().__init__()
        self.__name = name
        self.__ingredients = ingredients  # Список ингредиентов с единицами измерения
        self.__instructions = instructions  # Инструкции приготовления

    @property
    def name(self):
        return self.__name

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def instructions(self):
        return self.__instructions

    def local_eq(self, other):
        return self.name == other.name

    def __str__(self):
        ingredients_str = ', '.join(self.ingredients)
        return f"Рецепт: {self.name}, Ингредиенты: {ingredients_str}, Инструкции: {self.instructions}"
