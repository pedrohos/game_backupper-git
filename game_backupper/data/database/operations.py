from . import DatabaseConn
from game_backupper.common.constants import DB_FETCH_GAMES_SQL, DB_FETCH_BACKUPS_SQL, DB_ADD_GAME_SQL, \
    DB_ADD_BACKUP_SQL, DB_UPDATE_GAME_SQL, DB_DELETE_GAME_SQL, DB_DELETE_BACKUP_SQL
from game_backupper.common.game import Game


def get_games() -> []:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_FETCH_GAMES_SQL)
        res = cursor.fetchall()
    return res


def add_game(game: Game) -> int:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_ADD_GAME_SQL, [game.name, game.game_save_root, game.game_backup])
        conn.commit()
        return cursor.lastrowid


def modify_game(game_id, name, game_save_root, game_backup) -> None:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_UPDATE_GAME_SQL, [name, game_save_root, game_backup, game_id])
        conn.commit()


def delete_game(game_id) -> None:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_DELETE_GAME_SQL, [game_id])
        conn.commit()


def get_backups(game_id: str) -> []:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_FETCH_BACKUPS_SQL, [str(game_id)])
        res = cursor.fetchall()
    return res


def add_backup(game_id) -> int:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_ADD_BACKUP_SQL, [game_id])
        conn.commit()
        return cursor.lastrowid


def delete_backup(backup_id) -> None:
    with DatabaseConn() as conn:
        cursor = conn.cursor()
        cursor.execute(DB_DELETE_BACKUP_SQL, [backup_id])
        conn.commit()
