import os
import shutil
from pathlib import Path
import hashlib
from game_backupper.data.settings.name_enum import SettingName
from game_backupper.data.settings.settings import load_settings
from game_backupper.common.constants import BACKUP_FILEPATH_GLOB_PATTERN


class Game:
    def __init__(self, game_id: int, name: str, game_save_root: Path, game_backup: Path = None):
        self._id = game_id
        self._name = name
        self._game_save_root = game_save_root

        settings = load_settings()
        if game_backup is None:
            self.game_backup = Path(settings[SettingName.BACKUP_SAVE_FOLDER], str(hashlib.sha256(name.encode("utf-8"))))
        else:
            self.game_backup = game_backup
        if not Path(self.game_backup).exists():
            os.mkdir(self.game_backup)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val

    @property
    def game_save_root(self):
        return self._game_save_root

    @game_save_root.setter
    def game_save_root(self, val: Path):
        self._game_save_root = val

    @property
    def game_backup(self):
        return self._game_backup

    @game_save_root.setter
    def game_backup(self, val: Path):
        if not val.exists():
            os.mkdir(val)
        for filepath in Path.glob(Path(self.game_backup), BACKUP_FILEPATH_GLOB_PATTERN):
            shutil.move(filepath, val)
        self._game_backup = val

