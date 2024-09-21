import pytest
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.recipe import Recipe
from src.start_service import StartService
from src.settings_manager import SettingsManager


@pytest.fixture
def setup_data_repository():
    # Настройка репозитория и сервиса
    repository = DataRepository()
    settings_manager = SettingsManager()
    # Вы можете добавить здесь настройку конфигурации
    service = StartService(repository=repository, settings_manager=settings_manager)
    service.create()  # Создаем номенклатуры и группы
    service.create_receipts()  # Создаем рецепты
    return repository


def test_nomenclature_exists(setup_data_repository):
    repository = setup_data_repository
    assert "nomenclature" in repository.data
    assert isinstance(repository.data["nomenclature"], Nomenclature)


def test_range_exists(setup_data_repository):
    repository = setup_data_repository
    assert "range" in repository.data
    assert isinstance(repository.data["range"], Range)


def test_group_exists(setup_data_repository):
    repository = setup_data_repository
    assert "group" in repository.data
    assert isinstance(repository.data["group"], GroupNomenclature)


def test_recipes_exist(setup_data_repository):
    repository = setup_data_repository
    assert "recipes" in repository.data
    assert isinstance(repository.data["recipes"], list)
    assert len(repository.data["recipes"]) == 2
    assert isinstance(repository.data["recipes"][0], Recipe)
    assert isinstance(repository.data["recipes"][1], Recipe)
