from src.errors.validator import Validator
from src.data_repository import DataRepository
from src.models.group_nomenclature import GroupNomenclature
from src.models.nomenclature import Nomenclature
from src.models.range import Range
from src.models.recipe import Recipe


class StartService:
    __repository: DataRepository
    __nomenclatures: dict = {}

    def __init__(self, repository):
        Validator.validate(repository, DataRepository)
        self.__repository = repository

    def __create_groups(self):
        """
        Стартовый набор групп
        """
        items = [
            GroupNomenclature.create(name="Бакалея"),
            GroupNomenclature.create(name="Молочные продукты"),
            GroupNomenclature.create(name="Яйца"),
            GroupNomenclature.create(name="Яйца"),
            GroupNomenclature.create(name="Приправы"),
            GroupNomenclature.create(name="Ягода"),
        ]
        self.__repository.data[DataRepository.group_id()] = items

    def __create_range(self):
        """
        Стартовый набор единиц измерения
        """
        gram = Range.create(name="грамм", conversion_factor=1.0)
        milliliter = Range.create(name="миллилитр", conversion_factor=1.0)
        piece = Range.create(name="шт.", conversion_factor=1.0)
        teaspoon = Range.create(name="чайная ложка", conversion_factor=1.0)
        tablespoon = Range.create(name="столовая ложка", conversion_factor=1.0)
        self.__repository.data[DataRepository.range_id()] = [gram, milliliter, piece, teaspoon, tablespoon]

    def __create_nomenclature(self):
        # Получаем необходимые единицы измерения и группы
        gram = self.__repository.data[DataRepository.range_id()][0]
        milliliter = self.__repository.data[DataRepository.range_id()][1]
        piece = self.__repository.data[DataRepository.range_id()][2]
        teaspoon = self.__repository.data[DataRepository.range_id()][3]

        group_grocery = [i for i in self.__repository.data[DataRepository.group_id()] if i.name == "Бакалея"][0]
        group_dairy = [i for i in self.__repository.data[DataRepository.group_id()] if i.name == "Молочные продукты"][0]
        group_eggs = [i for i in self.__repository.data[DataRepository.group_id()] if i.name == "Яйца"][0]
        group_berries = [i for i in self.__repository.data[DataRepository.group_id()] if i.name == "Ягода"][0]

        # Создаем номенклатуры на основе рецепта
        self.__nomenclatures["Пшеничная мука"] = Nomenclature.create(name="Пшеничная мука", group=group_grocery, range=gram)
        self.__nomenclatures["Молоко"] = Nomenclature.create(name="Молоко", group=group_dairy, range=milliliter)
        self.__nomenclatures["Яйцо"] = Nomenclature.create(name="Яйцо", group=group_eggs, range=piece)
        self.__nomenclatures["Сахар"] = Nomenclature.create(name="Сахар", group=group_grocery, range=gram)
        self.__nomenclatures["Разрыхлитель теста"] = Nomenclature.create(name="Разрыхлитель теста", group=group_grocery, range=gram)
        self.__nomenclatures["Соль"] = Nomenclature.create(name="Соль", group=group_grocery, range=teaspoon)
        self.__nomenclatures["Черника"] = Nomenclature.create(name="Черника", group=group_berries, range=gram)
        self.__nomenclatures["Сливочное масло"] = Nomenclature.create(name="Сливочное масло", group=group_dairy, range=gram)

        # Сохраняем номенклатуры в репозиторий
        self.__repository.data[DataRepository.nomenclature_id()] = list(self.__nomenclatures.values())

    def __create_recipe(self):
        # Определяем ингредиенты для рецепта
        ingredients = {
            self.__nomenclatures["Пшеничная мука"]: 200,  # 200 гр
            self.__nomenclatures["Молоко"]: 300,  # 300 мл
            self.__nomenclatures["Яйцо"]: 2,  # 2 шт
            self.__nomenclatures["Сахар"]: 50,  # 50 гр
            self.__nomenclatures["Разрыхлитель теста"]: 10,  # 10 гр
            self.__nomenclatures["Соль"]: 0.5,  # 1/2 ч.л. (0.5 ч.л.)
            self.__nomenclatures["Черника"]: 150,  # 150 гр
            self.__nomenclatures["Сливочное масло"]: 30  # 30 гр
        }

        steps = [
            "Подготовьте все ингредиенты. В глубокой миске смешайте муку, сахар, разрыхлитель и соль.",
            "В отдельной миске взбейте яйца и добавьте молоко. Хорошо перемешайте.",
            "Влейте яичную смесь в сухие ингредиенты и перемешайте до однородности. Постарайтесь не перебить тесто, небольшие комочки допустимы.",
            "В растопленное сливочное масло добавьте тесто и аккуратно перемешайте.",
            "Добавьте чернику в тесто и осторожно перемешайте, чтобы не повредить ягоды.",
            "Разогрейте сковороду на среднем огне и слегка смажьте ее маслом.",
            "Вылейте половник теста на сковороду. Готовьте до появления пузырьков на поверхности, затем переверните и жарьте до золотистого цвета.",
            "Повторяйте процесс, пока не израсходуете все тесто.",
            "Подавайте панкейки горячими, можно с медом или кленовым сиропом."
        ]

        cooking_time = 25  # Время приготовления в минутах

        # Создаем рецепт
        recipe = Recipe.create(
            name="Панкейки с черникой",
            ingredients=ingredients,
            steps=steps,
            cooking_time_by_min=cooking_time
        )

        # Сохраняем рецепт в репозиторий (при необходимости)
        self.__repository.data[DataRepository.recipe_id()] = [recipe]

    def create(self):
        self.__create_groups()
        self.__create_range()
        self.__create_nomenclature()
        self.__create_recipe()


# Пример использования
r = DataRepository()
s = StartService(r)
s.create()

print(r.data[DataRepository.recipe_id()][0])  # Печатаем созданный рецепт
