from src.contracts.implements.nomenclature import Nomenclature


n1 = Nomenclature()
n2 = Nomenclature()


def test_other_uuid_for_instances():
    assert n1.uuid != n2.uuid


def test_base_equals():
    n1.name = "this"
    n2.name = "this"
    assert n1 == n2


def test_base_no_equals():
    n1.name = "this"
    n2.name = "not this"
    assert n1 == n2
