from enum import Enum
from .type_enum import SettingType
# from ...common.constants import ENUM_SETTINGS_FILE_ROOT_DESC, ENUM_SETTINGS_SAVE_LIMIT_DESC, \
#     ENUM_SETTINGS_SAVE_FOLDER_DESC


class SettingName(Enum):
    BACKUP_SAVE_FOLDER = (0, SettingType.PATH),
    N_SAVE_LIMIT = (1, SettingType.INT),
    SETTINGS_ROOT = (2, SettingType.PATH)
