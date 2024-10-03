from src.models.range import Range
from src.utils.deserializer import Deserializer


def test_deserialize_range():
    # Создаем объект Range для сравнения
    expected_range = Range.create(name="кг.", conversion_factor=1000,
                                  base_unit=Range.create(name="гр.", conversion_factor=1, base_unit=None))

    # JSON-данные для десериализации
    range_dict = {
        "uuid": "65256fbf-ca34-4636-95f2-87615dc98648",
        "name": "кг.",
        "conversion_factor": 1000,
        "base_unit": {
            "uuid": "65256fbf-ca34-4636-95f2-87615dc98648",
            "name": "гр.",
            "conversion_factor": 1,
            "base_unit": None
        }
    }

    # Десериализация
    deserialized_range = Deserializer.deserialize(Range, range_dict)

    # Проверяем, что объект корректно десериализован
    assert deserialized_range.name == expected_range.name
    assert deserialized_range.conversion_factor == expected_range.conversion_factor

    # Проверяем наличие base_unit
    assert deserialized_range.base_unit is not None
    assert deserialized_range.base_unit.name == expected_range.base_unit.name
    assert deserialized_range.base_unit.conversion_factor == expected_range.base_unit.conversion_factor

    # Проверяем корректность сравнения объектов
    assert deserialized_range == expected_range
