import sqlite3
import os

from game_backupper.data.settings import DB_FILE_PATH
from game_backupper.common.constants import DB_ACTIVATE_FOREIGN_KEY, DB_CREATE_DATABASE_SQL


def sanity_test(path: str):
    # TODO: Increment the sanity, check if the tables exists and are correct
    return os.path.exists(path)


def create_database():
    if not DB_FILE_PATH.parent.exists():
        os.makedirs(DB_FILE_PATH.parent)
    with sqlite3.connect(DB_FILE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(DB_ACTIVATE_FOREIGN_KEY)
        cursor.executescript(DB_CREATE_DATABASE_SQL)
        conn.commit()


def load_database():
    if not sanity_test(DB_FILE_PATH):
        create_database()


class DatabaseConn(object):
    def __init__(self):
        self.db_conn = sqlite3.connect(DB_FILE_PATH)

    def __enter__(self):
        self.db_conn.execute(DB_ACTIVATE_FOREIGN_KEY)
        return self.db_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_conn.close()


load_database()
