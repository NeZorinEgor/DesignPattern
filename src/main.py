import os

from settings import SettingsManager

settings_manager = SettingsManager()
settings_manager.open(file_path=os.path.join(os.pardir, "settings.json"))
settings = settings_manager.settings
print(settings.org_name)
print(settings.inn)
