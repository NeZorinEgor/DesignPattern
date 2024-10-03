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
            if key == "uuid":
                continue

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
