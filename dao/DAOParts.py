from sqlalchemy import Table

from dao.Connection import Connection
from dao.DAOInterface import DAOInterface


class DAOParts(DAOInterface):
    def __init__(self):
        self.conn = Connection()
        self.meta = self.conn.meta
        self.Parts = Table(

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
