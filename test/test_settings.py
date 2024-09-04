import os.path

import pytest

from managers.settings import SettingsManager


def test_no_load_settings():
    """ Тест если ничего не загружать """
    settings_manager = SettingsManager()

    settings = settings_manager.settings
    assert settings.INN == ""
    assert settings.ACCOUNT == ""
    assert settings.CORRESPONDENT_ACCOUNT == ""
    assert settings.BIC == ""
    assert settings.NAME == ""
    assert settings.TYPE_OF_OWNERSHIP == ""


# Тестовые данные
settings_dict = {
    "INN": "111111111111",
    "ACCOUNT": "22222222222",
    "CORRESPONDENT_ACCOUNT": "33333333333",
    "BIC": "444444444",
    "NAME": "555555555",
    "TYPE_OF_OWNERSHIP": "66666"
}


def test_load_settings_from_dict():
    """ Тест загрузки данных из словаря """
    settings_manager = SettingsManager()
    settings_manager.from_dict(settings_dict)

    settings = settings_manager.settings
    assert settings.INN == "111111111111"
    assert settings.ACCOUNT == "22222222222"
    assert settings.CORRESPONDENT_ACCOUNT == "33333333333"
    assert settings.BIC == "444444444"
    assert settings.NAME == "555555555"
    assert settings.TYPE_OF_OWNERSHIP == "66666"


def test_load_settings_from_json():
    """ Тест загрузки данных из json файла """
    settings_manager = SettingsManager()
    settings_manager.from_json(os.path.join(os.pardir, "settings.json"))

    settings = settings_manager.settings
    assert settings.INN == "123456789012"
    assert settings.ACCOUNT == "40702810123"
    assert settings.CORRESPONDENT_ACCOUNT == "38104000000"
    assert settings.BIC == "044525225"
    assert settings.NAME == "CLEAR ARCHETYPE? NO NO NO"
    assert settings.TYPE_OF_OWNERSHIP == "SOLID"


def test_load_settings_from_json_from_another_dir_and_name():
    """ Тест загрузки данных из json файла """
    settings_manager = SettingsManager()
    settings_manager.from_json(os.path.join("zxy_file_for_test.json"))

    settings = settings_manager.settings
    assert settings.INN == "############"
    assert settings.ACCOUNT == "@@@@@@@@@@@"
    assert settings.CORRESPONDENT_ACCOUNT == "!!!!!!!!!!!"
    assert settings.BIC == "$$$$$$$$$"
    assert settings.NAME == "%%%%%%%%%%%%%%%%%%%%"
    assert settings.TYPE_OF_OWNERSHIP == "^^^^^"


def test_invalid_fields_len():
    """ Тест на загрузку полей не корректной длинны """
    settings_manager = SettingsManager()

    with pytest.raises(ValueError, match="INN must be exactly 12 characters long, not 1"):
        settings_manager.from_dict({"INN": "1"})
    with pytest.raises(ValueError, match="ACCOUNT must be exactly 11 characters long, not 1"):
        settings_manager.from_dict({"ACCOUNT": "2"})
    with pytest.raises(ValueError, match="CORRESPONDENT_ACCOUNT must be exactly 11 characters long, not 1"):
        settings_manager.from_dict({"CORRESPONDENT_ACCOUNT": "3"})
    with pytest.raises(ValueError, match="BIC must be exactly 9 characters long, not 1"):
        settings_manager.from_dict({"BIC": "4"})
    with pytest.raises(ValueError, match="TYPE_OF_OWNERSHIP must be exactly 5 characters long, not 1"):
        settings_manager.from_dict({"TYPE_OF_OWNERSHIP": "5"})


def test_is_singleton():
    """ Проверку на 1 экземпляр класса """
    settings_manager1 = SettingsManager()
    settings_manager1.from_dict(settings_dict)
    settings1 = settings_manager1.settings

    settings_manager2 = SettingsManager()
    settings_manager2.from_dict(settings_dict)
    settings2 = settings_manager2.settings
    assert settings1 is settings2
    assert settings_manager1 is settings_manager2
