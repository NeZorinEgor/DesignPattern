import os

from src.settings_manager import SettingsManager
from models.organization import Organization


def main():
    settings_manager = SettingsManager()
    path = os.path.join(os.pardir, "settings.json")
    settings_manager.from_json(path=path)
    settings = settings_manager.settings
    organization = Organization(settings)
    print(organization)


if __name__ == "__main__":
    main()
