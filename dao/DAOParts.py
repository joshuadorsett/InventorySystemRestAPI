from sqlalchemy import Table, Integer, Column, Text, Float

from dao.db import DB
from dao.DAOInterface import DAOInterface


class DAOParts(DAOInterface):
    def __init__(self):
        self.db = DB()
        self.meta = self.conn.meta
        self.Parts = Table(
            'Parts',
            self.meta,
            Column('partsId', Integer, primary_key=True),
            Column('name', Text),
            Column('price', Float),
            Column('stock', Integer),
            Column('min', Integer),
            Column('max', Integer)
        )
        self.meta.create_all(self.db)
        self.conn = self.db.connection.connect()

    def selectAll(self):
        pass

    def select(self, partsId):
        pass

    def insert(self, part):
        pass

    def update(self, part):
        pass

    def delete(self, partsId):
        pass
