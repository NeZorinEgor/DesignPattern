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
    def set_format(report_format):
        Validator.validate(report_format, FormatEnum)

        report_class = ReportFactory.report_classes.get(report_format)
        if report_class is None:
            raise InvalidTypeError("Неподдерживаемый формат отчета")

        return report_class()

    def create(self, data):
        """Создает отчет в зависимости от текущих настроек."""
        try:
            report_format = self.settings.report_format
            report_class = self.set_format(report_format)
            return report_class.create(data)
        except Exception as e:
            self.error_proxy.error_message = str(e)
            return None


settings_manager = SettingsManager()
settings_manager.from_json(os.path.join(os.pardir, "settings.json"))
repository = DataRepository()
service = StartService(repository)
service.create()
recipe = repository.data[DataRepository.recipe_id()][0]

factory = ReportFactory(settings_manager.settings)
creator = factory.set_format(FormatEnum.JSON)

print(creator.create(recipe))
