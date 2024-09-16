from src.models.nomenclature import Nomenclature


def test_unique_uuid_for_different_instances():
    n1 = Nomenclature()
    n2 = Nomenclature()
    assert n1.uuid != n2.uuid


def test_nomenclature_instances_equal_when_names_match():
    n1 = Nomenclature()
    n1.name = "this"
    n2 = Nomenclature()
    n2.name = "this"
    assert n1 == n2


def test_nomenclature_instances_not_equal_when_names_differ():
    n1 = Nomenclature()
    n1.name = "this"
    n2 = Nomenclature()
    n2.name = "not this"
    assert n1 != n2
