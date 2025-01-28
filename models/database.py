from sqlmodel import create_engine, SQLModel
from .model import *

sqlite_file_name = 'datebase.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'
engine = create_engine(sqlite_url, echo=True)


if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)