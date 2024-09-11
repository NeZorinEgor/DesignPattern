class Range:
    """ Модель единица измерения """
    def __init__(self, name, conversion_factor, base_unit=None):
        self.name = name
        self.conversion_factor = conversion_factor
        self.base_unit = base_unit if base_unit else self

    def convert_to_base(self, value):
        return value * self.conversion_factor

    def convert_from_base(self, value):
        return value / self.conversion_factor

    def __str__(self):
        return f"{self.name} (коэффициент пересчета: {self.conversion_factor})"



