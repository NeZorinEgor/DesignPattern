import os

import pytest

from src.data_repository import DataRepository
from src.models.recipe import Recipe
from src.settings_manager import SettingsManager
from src.start_service import StartService


@pytest.fixture
def recipe_model() -> Recipe:
    """
    Создание зависимости для тестов
    """
    # Настройки для фабрики
    settings_manager = SettingsManager()
    settings_manager.from_json(os.path.join(os.pardir, "settings.json"))
    # Создание инстанса рецепта
    repository = DataRepository()
    service = StartService(repository)
    service.create()
    return repository.data[DataRepository.recipe_id()][0]


def test_recipe_creation(recipe_model):
    """
    Проверка, что экземпляр корректно создан
    """
    assert recipe_model is not None


def test_recipe_properties(recipe_model):
    """
    Проверка на свойства модели по умолчанию TODO
    """
    assert recipe_model.name == "Панкейки с черникой"
    assert recipe_model.cooking_time_by_min == 25
    assert type(recipe_model.ingredients) == list
