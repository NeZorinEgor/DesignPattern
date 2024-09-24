class Range:
    def __init__(self, name, conversion_factor, base_unit=None):
        self.name = name
        self.conversion_factor = conversion_factor
        self.base_unit = base_unit if base_unit else self

    def convert_to_base(self, value):
        return value * self.conversion_factor

    def convert_from_base(self, value):
        return value / self.conversion_factor

    def __str__(self):
        if self.base_unit == self:
            base_unit_str = " (базовая единица)"
        else:
            base_unit_str = f", базовая единица: {self.base_unit.name}"

        return f"{self.name}: коэффициент пересчета {self.conversion_factor}{base_unit_str}"


# Создаем базовые единицы измерения
gram = Range(name="грамм", conversion_factor=1.0)
milliliter = Range(name="миллилитр", conversion_factor=1.0)
piece = Range(name="шт.", conversion_factor=1.0)
teaspoon = Range(name="чайная ложка", conversion_factor=1.0)
tablespoon = Range(name="столовая ложка", conversion_factor=1.0)
