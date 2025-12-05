import sqlite3
from sqlite3 import Connection

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn: Connection = None # type: ignore

    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row  # return dict-like rows

    def get_conn(self) -> Connection:
        if not self.conn:
            self.connect()
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None # type: ignore
