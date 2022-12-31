from tempfile import TemporaryFile
from tempfile import TemporaryDirectory
from game_backupper.tests.test_constants import TEST_SETTINGS_LOAD_SETTINGS_EXCESSIVE_PARAMS, TEST_SETTINGS_LOAD_SETTINGS_INSUFFICIENT_PARAMS
from game_backupper.common.constants import EXCEPTION_SETTINGS_EXCESSIVE_NUMBER_CONFIG_KEYS, EXCEPTION_SETTINGS_INSUFFICIENT_NECESSARY_CONFIG_KEYS
from game_backupper.data.settings.settings import _check_settings
import unittest
import os
import json

from game_backupper.common.exceptions import SettingParseException


def _test_prepare_load_setting(json_str):
    # td_save_dir = TemporaryDirectory()
    # td_backup_dir = TemporaryDirectory()

    settings_ini = TemporaryFile(delete=False)
    settings_ini.write(json_str.encode("utf-8"))

    settings_name = settings_ini.name
    settings_ini.close()

    with open(settings_name, "r") as file:
        lines = file.readlines()
    lines = "".join(lines)
    return json.loads(lines), settings_name


class TestSettings(unittest.TestCase):

    def test_load_settings_excessive_params(self):
        config, settings_name = _test_prepare_load_setting(TEST_SETTINGS_LOAD_SETTINGS_EXCESSIVE_PARAMS)

        try:
            _check_settings(config)
            self.fail("Did not capture expected exception.")
        except SettingParseException as e:
            self.assertEqual(SettingParseException().__class__, e.__class__)
            self.assertEqual(repr(SettingParseException(EXCEPTION_SETTINGS_EXCESSIVE_NUMBER_CONFIG_KEYS)), repr(e))
        finally:
            os.unlink(settings_name)

    def test_load_settings_insufficient_params(self):
        config, settings_name = _test_prepare_load_setting(TEST_SETTINGS_LOAD_SETTINGS_INSUFFICIENT_PARAMS)

        try:
            _check_settings(config)
            self.fail("Did not capture expected exception.")
        except SettingParseException as e:
            self.assertEqual(SettingParseException().__class__, e.__class__)
            self.assertEqual(repr(SettingParseException(EXCEPTION_SETTINGS_INSUFFICIENT_NECESSARY_CONFIG_KEYS)), repr(e))
        finally:
            os.unlink(settings_name)


if __name__ == "__main__":
    unittest.main()
