import os

from src.managers.settings import SettingsManager
from src.models.organization import Organization


def test_read_settings_class():
    settings_manager = SettingsManager()
    path = os.path.join(os.pardir, "settings.json")
    settings_manager.from_json(path=path)
    settings = settings_manager.settings
    organization = Organization(settings)
    assert organization.inn == settings.inn
    assert organization.bic == settings.bic
    assert organization.account == settings.account
    assert organization.type_of_ownership == settings.type_of_ownership
