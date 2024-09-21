class DataRepository:
    __data = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DataRepository, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def group_key():
        return "group"

    @property
    def data(self):
        return self.__data

    def add_recipe(self, recipe):
        if "recipes" not in self.__data:
            self.__data["recipes"] = []
        self.__data["recipes"].append(recipe)

    def get_recipes(self):
        return self.__data.get("recipes", [])
