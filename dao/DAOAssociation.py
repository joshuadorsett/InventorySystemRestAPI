from sqlalchemy import Table, Column, Integer

from dao.Connection import Connection
from dao.DAOInterface import DAOInterface


class DAOAssociation(DAOInterface):
    def __init__(self):
        self.conn = Connection()
        self.meta = self.conn.meta
        self.Associations = Table(
            'Associations',
            self.meta,
            Column('partsId', Integer, primary_key=True),
            Column('productsId', Integer, primary_key=True)
        )

    def selectAll(self):
        pass

    def select(self, association):
        pass

    def insert(self, association):
        pass

    def update(self, association):
        pass

    def delete(self, association):
        pass
