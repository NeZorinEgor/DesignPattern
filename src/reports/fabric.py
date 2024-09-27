import os.path

from src.core.report import FormatEnum
from src.data_repository import DataRepository
from src.errors.custom import InvalidTypeError
from src.errors.proxy import ErrorProxy
from src.errors.validator import Validator
from src.models.settings import Settings
from src.reports.csv_report import CSVReport
from src.reports.json_report import JSONReport
from src.reports.markdown_report import MarkdownReport
from src.reports.rtf_report import RTFReport
from src.reports.xml_report import XMLReport

from src.settings_manager import SettingsManager
from src.start_service import StartService


class ReportFactory:
    report_classes = {
        FormatEnum.CSV: CSVReport,
        FormatEnum.MARKDOWN: MarkdownReport,
        FormatEnum.JSON: JSONReport,
        FormatEnum.XML: XMLReport,
        FormatEnum.RTF: RTFReport,
    }

    def __init__(self, settings: Settings):
        self.settings = settings
        self.error_proxy = ErrorProxy()

    @staticmethod
    def create(report_format: FormatEnum):
        """
        Возвращает класс, в завивисомти от входного аргумента
        """
        Validator.validate(report_format, FormatEnum)

        report_class = ReportFactory.report_classes.get(report_format)
        if report_class is None:
            raise InvalidTypeError("Неподдерживаемый формат отчета")

        return report_class()

    def create_default(self):
        """
        Возвращает класс в зависимости от значения по умолчанию из настроек
        """
        base_format = self.settings.report_format
        report_class = ReportFactory.report_classes.get(base_format)
        if report_class is None:
            raise InvalidTypeError("Неподдерживаемый формат отчета")
        return report_class()


# TODO: add fixture to test
# Настройки для фабрики
settings_manager = SettingsManager()
settings_manager.from_json(os.path.join(os.pardir, "settings.json"))
# Создание инстанса рецепта
repository = DataRepository()
service = StartService(repository)
service.create()
recipe = repository.data[DataRepository.recipe_id()][0]
# Фабрика отчетности
factory = ReportFactory(settings_manager.settings)
creator = factory.create_default()
# creator = factory.create(FormatEnum.JSON)
print(creator.create(recipe))
