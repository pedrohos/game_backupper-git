from enum import Enum
from pathlib import Path

from game_backupper.common.constants import EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_PATH, \
    EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_STRING, EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_FLOAT, \
    EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_INT
from game_backupper.common.exceptions import SettingTypeFuncInvalidPath, SettingTypeFuncInvalidString, \
    SettingTypeFuncInvalidFloat, SettingTypeFuncInvalidInt


def _get_path(path):
    if isinstance(path, str):
        return Path(path)
    elif isinstance(path, Path):
        return path
    else:
        raise SettingTypeFuncInvalidPath(EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_PATH)


def _get_str(config_str):
    if isinstance(config_str, str):
        return config_str
    else:
        raise SettingTypeFuncInvalidString(EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_STRING)


def _get_float(config_str):
    if isinstance(config_str, float):
        return config_str
    else:
        raise SettingTypeFuncInvalidFloat(EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_FLOAT)


def _get_int(config_str):
    if isinstance(config_str, int):
        return config_str
    else:
        raise SettingTypeFuncInvalidInt(EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_INT)


class SettingType(Enum):
    PATH = _get_path
    STRING = _get_str
    FLOAT = _get_float
    INT = _get_int
