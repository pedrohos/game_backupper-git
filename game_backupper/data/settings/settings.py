import logging
import json
from functools import lru_cache
from pathlib import Path

from game_backupper.common.exceptions import SettingParseException, SettingTypeFuncInvalidAttribute
from game_backupper.common.constants import EXCEPTION_SETTINGS_EXCESSIVE_NUMBER_CONFIG_KEYS, \
    EXCEPTION_SETTINGS_INSUFFICIENT_NECESSARY_CONFIG_KEYS, LOGGER_ERROR_SETTINGS_FAILED_TO_LOAD_SETTINGS, \
    LOGGER_ERROR_SETTINGS_FAILED_TO_PARSE_JSON, EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_ATTRIBUTE, LOGGER_WARNING_LOADING_DEFAULT_SETTINGS

from game_backupper.data.settings.name_enum import SettingName
from . import SETTINGS_FILE_PATH, DEFAULT_SETTINGS

SETTINGS_SECTION_NAMES = [key.name for key in SettingName]


def _check_settings(config: dict):
    intersection = set(SETTINGS_SECTION_NAMES).intersection(set(config.keys()))

    if len(intersection) < len(SETTINGS_SECTION_NAMES):
        raise SettingParseException(EXCEPTION_SETTINGS_INSUFFICIENT_NECESSARY_CONFIG_KEYS)
    elif set(config.keys()) != set(SETTINGS_SECTION_NAMES):
        raise SettingParseException(EXCEPTION_SETTINGS_EXCESSIVE_NUMBER_CONFIG_KEYS)


def _load_settings(config: dict):
    res_config = {}
    for enum_name, enum_value in SettingName:
        enum_func = enum_value[1]
        try:
            res_config[config[enum_name]] = enum_func(config[enum_name])
        except SettingTypeFuncInvalidAttribute as e:
            logger = logging.getLogger(__name__)
            logger.error(repr(e))
            logger.error(EXCEPTION_SETTINGS_TYPE_FUNCTION_INVALID_ATTRIBUTE)
    return res_config


def _load_default_settings():
    return DEFAULT_SETTINGS


@lru_cache(maxsize=None)
def load_settings(settings_file: Path = SETTINGS_FILE_PATH):
    try:
        # Parses file
        with open(settings_file, "r") as file:
            lines = file.readlines()
        lines = "".join(lines)
        config = json.loads(lines)

        # Check if the number of parameters are matching
        _check_settings(config)
        config = _load_settings(config)
    except SettingParseException as e:
        logger = logging.getLogger(__name__)
        logger.error(repr(e))
        logger.error(LOGGER_ERROR_SETTINGS_FAILED_TO_LOAD_SETTINGS)
        logger.warning(LOGGER_WARNING_LOADING_DEFAULT_SETTINGS)
        config = _load_default_settings()
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(repr(e))
        logger.error(LOGGER_ERROR_SETTINGS_FAILED_TO_PARSE_JSON)
        logger.error(LOGGER_ERROR_SETTINGS_FAILED_TO_LOAD_SETTINGS)
        logger.warning(LOGGER_WARNING_LOADING_DEFAULT_SETTINGS)
        config = _load_default_settings()

    return config
