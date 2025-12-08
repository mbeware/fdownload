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

## Premiere tentative avec SQLAlchemy

# from sqlalchemy.ext.declarative import declarative_base as sqlalchemy_declarative_base
# from sqlalchemy import Column as sqlalchemy_Column
# from sqlalchemy import Integer as sqlalchemy_Integer
# from sqlalchemy import String  as sqlalchemy_String
# import sqlalchemy

# from sqlalchemy.orm import sessionmaker as sqlalchemy_sessionmaker
# class SQLAlchemyDatabase:
#     def __init__(self, db_path: str):
#         self.db_path = db_path
#         self.engine = sqlalchemy.create_engine(db_path)

#     def setup_schema_sqlalchemy(self):
#         # Create all tables from Base in the engine
#         self.Base.metadata.create_all(self.engine)
        
#     def get_engine(self):
#         return self.engine

#     def connect(self):
#         self.session = sqlalchemy_sessionmaker(bind=self.engine)()
#         return self.session
    
#     def get_Base(self):
#         self.Base = sqlalchemy_declarative_base()
#         return self.Base
    
