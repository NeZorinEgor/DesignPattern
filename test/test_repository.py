import pytest
from src.data_repository import DataRepository
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.group_nomenclature import GroupNomenclature
from src.models.recipe import PersonalRecipe


@pytest.fixture
def repository():
    """Фикстура для создания репозитория данных перед каждым тестом."""
    repo = DataRepository()
    return repo


def test_nomenclature(repository):
    """Тест для проверки наличия номенклатуры."""
    nomenclature = Nomenclature()
    nomenclature.name = "Товар A"
    repository.data["nomenclature"] = nomenclature

    assert "nomenclature" in repository.data
    assert repository.data["nomenclature"].name == "Товар A"


def test_units_of_measurement(repository):
    """Тест для проверки наличия единиц измерения."""
    kilogram = Range(name="Килограмм", conversion_factor=1.0)
    gram = Range(name="Грамм", conversion_factor=0.001, base_unit=kilogram)

    repository.data["ranges"] = {"kilogram": kilogram, "gram": gram}

    assert "ranges" in repository.data
    assert "kilogram" in repository.data["ranges"]
    assert repository.data["ranges"]["kilogram"].name == "Килограмм"


def test_groups(repository):
    """Тест для проверки наличия групп."""
    group = GroupNomenclature.create_base_group()
    repository.data["group"] = group

    assert "group" in repository.data
    assert isinstance(repository.data["group"], GroupNomenclature)


def test_recipes(repository):
    """Тест для проверки наличия рецептов."""
    recipe = PersonalRecipe(name="Мой личный борщ", ingredients=["Свекла", "Капуста"], instructions="Варить 1 час.")
    repository.add_recipe(recipe)

    assert len(repository.get_recipes()) > 0
    assert repository.get_recipes()[0].name == "Мой личный борщ"

