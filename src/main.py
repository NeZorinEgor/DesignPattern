import os

from src.data_repository import DataRepository
from src.settings_manager import SettingsManager
from models.organization import Organization
from src.start_service import StartService


def main():
    settings_manager = SettingsManager()
    path = os.path.join(os.pardir, "settings.json")
    settings_manager.from_json(path=path)
    settings = settings_manager.settings
    organization = Organization(settings)
    print(organization)

    data_repository = DataRepository()
    start_service = StartService(repository=data_repository, settings_manager=settings_manager)
    start_service.create()
    start_service.create_receipts()
    print("Данные из репозитория:")
    for key, value in data_repository.data.items():
        if isinstance(value, list):
            for item in value:
                print(f"{key}: {item.name if hasattr(item, 'name') else item}")
        else:
            print(f"{key}: {value.name if hasattr(value, 'name') else value}")


if __name__ == "__main__":
    main()
