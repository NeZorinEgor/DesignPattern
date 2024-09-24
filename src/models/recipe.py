from src.core.model import BaseModel


class Recipe(BaseModel):
    def __init__(self, name, ingredients, instructions, lesson_topic=None):
        super().__init__()
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.lesson_topic = lesson_topic

    def local_eq(self, other):
        return self.name == other.name and self.ingredients == other.ingredients

    def __str__(self):
        lesson_info = f" (Тема занятия: {self.lesson_topic})" if self.lesson_topic else ""
        return f"Рецепт: {self.name}{lesson_info}\nИнгредиенты: {', '.join(self.ingredients)}\nИнструкции: {self.instructions}"
