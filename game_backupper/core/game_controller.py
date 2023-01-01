import os.path

from game_backupper.data.database import operations as db_operation
from game_backupper.common.game import Game
from game_backupper.data.settings.settings import load_settings, SettingName
from pathlib import Path


class GameController:
    def __init__(self):
        self._update_data()

    def _update_data(self):
        info = {}
        games = db_operation.get_games()
        for game in games:
            info[game[0]] = db_operation.get_backups(game[0])
        self.games = games
        self.info = info

    def get_games(self):
        return self.games

    def get_info(self):
        return self.info

    def add_game(self, name: str, game_save_root: str):
        _ = db_operation.add_game(Game(game_id=0, name=name, game_save_root=game_save_root))
        self._update_data()

    def delete_game(self, game_id: int):
        db_operation.delete_game(game_id)
        self._update_data()