from sqlalchemy import Table, Column, Integer

from dao.db import DB
from dao.DAOInterface import DAOInterface


class DAOAssociation(DAOInterface):
    def __init__(self):
        self.db = DB()
        self.meta = self.conn.meta
        self.Associations = Table(
            'Associations',
            self.meta,
            Column('partsId', Integer, primary_key=True),
            Column('productsId', Integer, primary_key=True)
        )
        self.meta.create_all(self.db)
        self.conn = self.db.connection.connect()

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
