from game_backupper.core.game_controller import GameController
from game_backupper.data import database
import unittest


class TestGameController(unittest.TestCase):
    def test_add_game(self):
        game_controller = GameController()
        print(game_controller.get_info())
        game_controller.add_game("Callisto Protocol", "/Users/pedrohos/GameBackupper/Saves/Callisto Protocol")
        print(game_controller.get_info())

    def test_delete_game(self):
        game_controller = GameController()
        print(game_controller.get_info())
        game_controller.add_game("Callisto Protocol", "/Users/pedrohos/GameBackupper/Saves/Callisto Protocol")
        print(game_controller.get_info())
        game_controller.delete_game(1)
        print(game_controller.get_info())
