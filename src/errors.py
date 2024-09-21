class InvalidTypeError(Exception):
    """ Исключение, вызываемое при неверном типе данных. """
    pass


class InvalidLengthError(Exception):
    """ Исключение, вызываемое при неверной длине данных. """
    pass


class ErrorProxy:
    __error_message: str = ""

    def __init__(self, exception: Exception = None):
        if exception is not None:
            self.__error_message = str(exception)

    @property
    def error_message(self) -> str:
        return self.__error_message

    @error_message.setter
    def error_message(self, new_message) -> None:
        if new_message == "":
            raise ValueError("Error message must be not empty!")
        self.__error_message = new_message

    @property
    def is_empty(self) -> bool:
        return len(self.__error_message) == 0
