from sqlalchemy import Table

from dao.Connection import Connection
from dao.DAOInterface import DAOInterface


class DAOAssociation(DAOInterface):
    def __init__(self):
        self.conn = Connection()
        self.meta = self.conn.meta
        self.Associations = Table(

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
