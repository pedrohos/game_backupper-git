from game_backupper.core.game_controller import GameController
from game_backupper.data import database
import unittest


class TestGameController(unittest.TestCase):
    def test_add_game(self):
        game_controller = GameController()
        print(game_controller.get_games())
        game_controller.add_game("Callisto Protocol", "C:/GameBackupper/Saves/Callisto Protocol")

