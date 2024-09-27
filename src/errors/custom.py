class InvalidType(Exception):
    """
    Исключение, вызываемое при неверном типе данных.
    """
    pass


class InvalidLength(Exception):
    """
    Исключение, вызываемое при неверной длине данных.
    """
    pass


class UnsupportableReportFormat(Exception):
    """
    Ошибка, вызываемая при неверно указанном формате в json файле
    """
    pass
