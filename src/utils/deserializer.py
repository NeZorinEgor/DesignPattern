from src.utils.validator import Validator
from src.models.range import Range


class Deserializer:
    @staticmethod
    def deserialize(cls, json: dict):
        Validator.validate(cls, type_=type)
        instance = cls()

        for key, value in json.items():
            key = key.lower()
            if hasattr(instance, key):
                attr = getattr(instance, key)
                if isinstance(attr, list):
                    deserialized_values = [Deserializer.deserialize(attr[0].__class__, item) for item in value]
                    setattr(instance, key, deserialized_values)
                elif isinstance(attr, Range):  # Проверка, если атрибут - объект класса Range
                    deserialized_value = Deserializer.deserialize(attr.__class__, value)
                    setattr(instance, key, deserialized_value)
                else:
                    setattr(instance, key, value)

                # Если это base_unit, создаем экземпляр Range
                if key == 'base_unit' and isinstance(value, dict):
                    base_unit_instance = Range.create(
                        name=value['name'],
                        conversion_factor=value['conversion_factor'],
                        base_unit=None  # Здесь можно передать deserialized для base_unit, если он есть
                    )
                    setattr(instance, key, base_unit_instance)
        return instance


range = Range.create(name="кг.", conversion_factor=1000, base_unit=Range.create(name="гр.", conversion_factor=1, base_unit=None))
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

deserialized_range = Deserializer.deserialize(Range, range_dict)

print(deserialized_range)
print(range)
print(deserialized_range == range)  # Теперь должно вернуть True

