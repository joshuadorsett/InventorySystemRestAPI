from sqlalchemy import Table, Integer, Column, Text, Float

from dao.Connection import Connection
from dao.DAOInterface import DAOInterface


class DAOParts(DAOInterface):
    def __init__(self):
        self.conn = Connection()
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
