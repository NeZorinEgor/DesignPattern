from src.errors.custom import InvalidTypeError, InvalidLengthError


class Validator:
    @staticmethod
    def validate(value, type_=None, len_=None):
        # Проверка типа данных, если тип указан
        if type_ is not None and not isinstance(value, type_):
            raise InvalidTypeError(f"argument must be of type {type_.__name__}")

        # Проверка длины, если длина указана и значение поддерживает len()
        if len_ is not None and hasattr(value, '__len__') and len(value) != len_:
            raise InvalidLengthError(f"argument must have a length of {len_}, but got {len(value)}")
