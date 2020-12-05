from sqlalchemy import create_engine, MetaData, Table


class DB:
    def __init__(self):
        self.connection = create_engine('sqlite:///restAPI.db', echo=True)
        self.meta = MetaData()
