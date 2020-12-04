from sqlalchemy import Table

from dao.Connection import Connection
from dao.DAOInterface import DAOInterface


class DAOProducts(DAOInterface):
    def __init__(self):
        self.conn = Connection()
        self.meta = self.conn.meta
        self.Products = Table(

        )

    def selectAll(self):
        pass

    def select(self, productId):
        pass

    def insert(self, product):
        pass

    def update(self, product):
        pass

    def delete(self, productId):
        pass
