from pathlib import Path
from game_backupper.data.settings.name_enum import SettingName
from game_backupper.common.constants import SETTINGS_DEFAULT_BACKUP_PATH

SETTINGS_FILE_PREFIX = "."
SETTINGS_FILE_NAME = "settings.json"

DB_FILE_PREFIX = "./resources"
DB_FILE_NAME = "games.db"

SETTINGS_FILE_PATH = Path(SETTINGS_FILE_PREFIX, SETTINGS_FILE_NAME)
DB_FILE_PATH = Path(DB_FILE_PREFIX, DB_FILE_NAME)

DEFAULT_SETTINGS = {
    SettingName.BACKUP_SAVE_FOLDER: Path(SETTINGS_DEFAULT_BACKUP_PATH),
    SettingName.N_SAVE_LIMIT: 10,
    SettingName.SETTINGS_ROOT: Path(SETTINGS_FILE_PREFIX)
}
# # Creates cache for loaded settings
# class SettingsCache(object):
#     def __init__(self):
#         self._cache = {}
#
#     def __call__(self, val) -> dict:
#         if val not in self._cache:
#             self._cache[val] = load_settings(SETTINGS_FILE_PATH)
#
#         return self._cache[val]
