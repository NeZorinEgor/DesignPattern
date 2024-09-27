import pytest
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.recipe import Recipe
from src.start_service import StartService


@pytest.fixture
def setup_repository():
    """Фикстура для настройки репозитория и данных"""
    repository = DataRepository()
    service = StartService(repository)
    service.create()  # Инициализация данных
    return repository


def test_nomenclatures(setup_repository):
    """Проверка наличия номенклатур"""
    repository = setup_repository
    nomenclatures = repository.data[DataRepository.nomenclature_id()]
    assert len(nomenclatures) > 0  # Проверка, что есть хотя бы одна номенклатура
    assert all(isinstance(nomenclature, Nomenclature) for nomenclature in nomenclatures)  # Все элементы должны быть номенклатурами


def test_ranges(setup_repository):
    """Проверка наличия единиц измерения"""
    repository = setup_repository
    ranges = repository.data[DataRepository.range_id()]
    assert len(ranges) > 0  # Проверка, что есть хотя бы одна единица измерения
    assert all(isinstance(range_item, Range) for range_item in ranges)  # Все элементы должны быть единицами измерения


def test_groups(setup_repository):
    """Проверка наличия групп"""
    repository = setup_repository
    groups = repository.data[DataRepository.group_id()]
    assert len(groups) > 0  # Проверка, что есть хотя бы одна группа
    assert all(isinstance(group, GroupNomenclature) for group in groups)  # Все элементы должны быть группами


def test_recipes(setup_repository):
    """Проверка наличия рецептов"""
    repository = setup_repository
    recipes = repository.data[DataRepository.recipe_id()]
    assert len(recipes) > 0  # Проверка, что есть хотя бы один рецепт
    assert all(isinstance(recipe, Recipe) for recipe in recipes)  # Все элементы должны быть рецептами
