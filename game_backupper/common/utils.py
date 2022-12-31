import os.path
from pathlib import Path
import re

from game_backupper.common.exceptions import NonexistentPathException
from game_backupper.data.settings.settings import load_settings
from game_backupper.data.settings.name_enum import SettingName
from game_backupper.common.constants import EXCEPTION_UTILS_NONEXISTENT_PATH, BACKUP_FILEPATH_GLOB_PATTERN, \
    BACKUP_VALID_FILENAME_REGEX_PATTERN


def _is_file_valid(filepath: Path):
    if not filepath.exists():
        return False
    return re.match(BACKUP_VALID_FILENAME_REGEX_PATTERN, filepath.stem) is not None


# def get_backups(backup: Path):
#     if not os.path.exists(backup):
#         raise NonexistentPathException(EXCEPTION_UTILS_NONEXISTENT_PATH)
#
#     settings = load_settings()
#     files = [file for file in backup.glob(BACKUP_FILEPATH_GLOB_PATTERN) if _is_file_valid(Path(backup, file))]
#     save_limit = settings[SettingName.N_SAVE_LIMIT]
#     return files[:save_limit]
