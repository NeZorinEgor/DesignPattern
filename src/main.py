import os
from src.settings_manager import SettingsManager
from models.organization import Organization
from src.data_repository import DataRepository
from src.start_service import StartService


def main():
    settings_manager = SettingsManager()
    path = os.path.join(os.pardir, "settings.json")
    settings_manager.from_json(path=path)
    settings = settings_manager.settings
    organization = Organization(settings)
    print(organization)

    repository = DataRepository()
    start_service = StartService(repository, settings_manager)
    personal_recipe_data = {
        "name": "Мой личный борщ",
        "ingredients": ["Свекла", "Капуста", "Морковь", "Картофель", "Мясо", "Соль"],
        "instructions": "Нарезать овощи и варить на медленном огне 1 час."
    }
    lesson_recipe_data = {
        "name": "Борщ на занятии",
        "ingredients": ["Свекла", "Капуста", "Морковь", "Картофель", "Мясо", "Соль"],
        "instructions": "Объяснить последовательность приготовления и варить в течение часа.",
        "lesson_topic": "Классические супы"
    }
    start_service.create(personal_recipe_data, lesson_recipe_data)
    print("\nСохраненные рецепты:")
    for recipe in repository.get_recipes():
        print(f"Рецепт: {recipe.name}, Ингредиенты: {recipe.ingredients}, UUID: {recipe.uuid}")
    print("\nСохраненная номенклатура:")
    print(repository.data["nomenclature"])
    print("\nСохраненные группы:")
    print(repository.data["group"])
    print("\nСохраненные единицы измерения:")
    for name, unit in repository.data["ranges"].items():
        print(f"{name}: {unit}")


if __name__ == "__main__":
    main()
