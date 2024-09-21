from src.core.model import BaseModel


class Recipe(BaseModel):
    def __init__(self, name, ingredients, instructions):
        super().__init__()
        self.name = name
        self.ingredients = ingredients  # список ингредиентов
        self.instructions = instructions  # текст инструкций

    def local_eq(self, other):
        return self.name == other.name and self.ingredients == other.ingredients


class PersonalRecipe(Recipe):
    def __init__(self, name, ingredients, instructions):
        super().__init__(name, ingredients, instructions)


class LessonRecipe(Recipe):
    def __init__(self, name, ingredients, instructions, lesson_topic):
        super().__init__(name, ingredients, instructions)
        self.lesson_topic = lesson_topic  # тема занятия
