from typing import List

from src.core.model import BaseModel
from src.errors.validator import Validator
from src.models.ingredient import Ingredient
from src.models.nomenclature import Nomenclature
from src.models.range import gram, milliliter, piece, teaspoon


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

    def local_eq(self, other):
        return self.name == other.name and self.ingredients == other.ingredients

    def __str__(self):
        ingredients_str = ", ".join(str(ingredient) for ingredient in self.ingredients)
        steps_str = "\n".join(f"{i + 1}. {step}" for i, step in enumerate(self.steps))

        return f"Рецепт: {self.name}\n" \
               f"Ингредиенты: {ingredients_str}\n" \
               f"Шаги приготовления:\n{steps_str}"


name = "ПАНКЕЙКИ С ЧЕРНИКОЙ"
ingredients = [
    Ingredient(range=gram, nomenclature=Nomenclature.create("Пшеничная мука", group="бакалея"),  quantity=200),
    Ingredient(range=milliliter, nomenclature=Nomenclature.create("Молоко", group="Молочные продукты"), quantity=300),
    Ingredient(range=piece, nomenclature=Nomenclature.create("Яйца", group="Дairy"), quantity=2),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Сахар", group="Бакалея"), quantity=50),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Разрыхлитель теста", group="Бакалея"), quantity=10),
    Ingredient(range=teaspoon, nomenclature=Nomenclature.create("Соль", group="Приправы"), quantity=0.5),  # 1/2 чайной ложки
    Ingredient(range=gram, nomenclature=Nomenclature.create("Черника", group="Фрукты"), quantity=150),
    Ingredient(range=gram, nomenclature=Nomenclature.create("Сливочное масло", group="Молочные продукты"), quantity=30),
]
steps = [
    "Подготовьте все ингредиенты. В глубокой миске смешайте муку, сахар, разрыхлитель и соль.",
    "В отдельной миске взбейте яйца и добавьте молоко. Хорошо перемешайте.",
    "Влейте яичную смесь в сухие ингредиенты и перемешайте до однородности. Постарайтесь не перебить тесто, небольшие комочки допустимы.",
    "В растопленное сливочное масло добавьте тесто и аккуратно перемешайте.",
    "Добавьте чернику в тесто и осторожно перемешайте, чтобы не повредить ягоды.",
    "Разогрейте сковороду на среднем огне и слегка смажьте ее маслом.",
    "Вылейте половник теста на сковороду. Готовьте до появления пузырьков на поверхности, затем переверните и жарьте до золотистого цвета.",
    "Повторяйте процесс, пока не израсходуете все тесто.",
    "Подавайте панкейки горячими, можно с медом или кленовым сиропом.",
]

r = Recipe(
    name="ПАНКЕЙКИ С ЧЕРНИКОЙ",
    ingredients=ingredients,
    steps=steps,
    cooking_time_by_min=25
)
print(r)
