class Range:
    __name = None
    __conversion_factor = None
    __base_unit = None

    @property
    def name(self):
        return self.__name

    def convert_to_base(self, value):
        return value * self.__conversion_factor

    def convert_from_base(self, value):
        return value / self.__conversion_factor

    def __str__(self):
        return f"{self.__name}"

    @staticmethod
    def create(name, conversion_factor, base_unit=None):
        item = Range()
        item.__name = name
        item.__conversion_factor = conversion_factor
        item.__base_unit = base_unit
        return item


