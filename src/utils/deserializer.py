from src.utils.validator import Validator
from src.models.range import Range


class Deserializer:
    @staticmethod
    def _is_primitive(value):
        return isinstance(value, (int, float, bool, str, bytes, type(None)))

    @staticmethod
    def deserialize(cls, json: dict):
        Validator.validate(cls, type_=type)  # Убедимся, что передан класс
        instance = cls()  # Создаем новый экземпляр класса

        for key, value in json.items():
            # Если это примитив и он есть у класса
            if hasattr(instance, key) and Deserializer._is_primitive(value):
                setattr(instance, key, value)
            # Если это кастомная модель и она есть в классе
            elif hasattr(instance, key) and isinstance(value, dict):
                dict_fields = value.keys()
                model_fields = filter(lambda x: not x.startswith("_") and not callable(getattr(cls, x)), dir(cls))
                if set(dict_fields) == set(model_fields):
                    # Рекурсивно десериализуем значение в новый экземпляр класса
                    sub_instance = Deserializer.deserialize(cls, value)
                    setattr(instance, key, sub_instance)

        return instance


# Пример использования
range = Range.create(name="кг.", conversion_factor=1000,
                     base_unit=Range.create(name="гр.", conversion_factor=1, base_unit=None))
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
print(range == deserialized_range)
