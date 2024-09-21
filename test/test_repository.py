import pytest
from src.data_repository import DataRepository
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.group_nomenclature import GroupNomenclature
from src.models.recipe import Recipe


@pytest.fixture
def repository():
    return DataRepository()


def test_nomenclature(repository):
    nomenclature = Nomenclature()
    nomenclature.name = "Товар A"
    repository.data["nomenclature"] = nomenclature

    assert "nomenclature" in repository.data
    assert repository.data["nomenclature"].name == "Товар A"


def test_ranges(repository):
    gram = Range(name="Грамм", conversion_factor=1.0)
    kilogram = Range(name="Килограмм", conversion_factor=1000.0, base_unit=gram)
    repository.data["ranges"] = {"gram": gram, "kilogram": kilogram}

    assert "ranges" in repository.data
    assert "gram" in repository.data["ranges"]
    assert "kilogram" in repository.data["ranges"]
    assert repository.data["ranges"]["kilogram"].conversion_factor == 1000.0


def test_group_nomenclature(repository):
    group = GroupNomenclature.create_base_group()
    repository.data["group"] = group

    assert "group" in repository.data
    assert isinstance(repository.data["group"], GroupNomenclature)


def test_recipes(repository):
    recipe = Recipe(
        name="Панкейки с черникой",
        ingredients={
            "Пшеничная мука": "200 гр",
            "Молоко": "300 мл",
            "Яйца": "2 шт"
        },
        instructions="Смешайте все ингредиенты и готовьте."
    )
    repository.data["recipes"] = [recipe]

    assert "recipes" in repository.data
    assert len(repository.data["recipes"]) == 1
    assert repository.data["recipes"][0].name == "Панкейки с черникой"
