import tkinter
from tkinter import *
from tkinter import ttk
from game_backupper.core.game_controller import GameController

class Frontend:
    def _get_controller_games(self):
        return self.game_controller.get_games()

    def _get_controller_games(self):
        return self.game_controller.get_games()

    def __init__(self):
        self.game_controller = GameController()
        root = Tk()
        mainframe = ttk.Frame(root, padding="3 3 3 3")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        add_game_button = ttk.Button(root, text='Add Game', command=add_game)
        delete_game_button = ttk.Button(root, text='Delete Game', command=delete_game)
        refresh_games_button = ttk.Button(root, text='Delete Game', command=delete_game)
        open_folder_games_button = ttk.Button(root, text='Delete Game', command=open_game_folder)

        add_game_button = ttk.Button(root, text='Add Game', command=add_game)
        delete_game_button = ttk.Button(root, text='Delete Game', command=delete_game)
        refresh_games_button = ttk.Button(root, text='Delete Game', command=delete_game)
        open_folder_games_button = ttk.Button(root, text='Delete Game', command=open_game_folder)

        games_name = [game[1] for game in self._get_controller_games()]
        choicesvar = StringVar(value=games_name)
        games_list = Listbox(mainframe, listvariable=choicesvar).grid(column=1, row=1, sticky=(N, W))

        root.mainloop()
