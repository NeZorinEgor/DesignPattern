import os

from managers.settings import SettingsManager


def main():
    settings_manager = SettingsManager()
    settings_manager.from_json(path=os.path.join(os.pardir, "settings.json"))
    settings = settings_manager.settings

    print(settings)


if __name__ == "__main__":
    main()
