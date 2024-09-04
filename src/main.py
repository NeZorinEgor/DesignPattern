import os

from managers.settings import SettingsManager


settings_dict = {
    "INN": "123456789012",                   # 12 символов
    "ACCOUNT": "40702810123",                # 11 символов
    "CORRESPONDENT_ACCOUNT": "38104000000",  # 15 символов
    "BIC": "044525225",                      # 9 символов
    "NAME": "CLEAR ARCHETYPE? NO NO NO",     # n символов
    "TYPE_OF_OWNERSHIP": "SOLID"             # 5 символа
}


def main():
    settings_manager = SettingsManager()
    path_to_settings = os.path.join(os.pardir, "settings.json")
    # Загрузить настройки из json файла или словаря. Все равно класс - singleton.
    settings_manager.from_dict(input_dict=settings_dict)
    settings_manager.from_json(file_path=path_to_settings)
    settings = settings_manager.settings
    print(settings)


if __name__ == "__main__":
    main()
