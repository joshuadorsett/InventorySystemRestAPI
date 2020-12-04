from sqlalchemy import Table, Integer, Float, Text, Column

from dao.Connection import Connection
from dao.DAOInterface import DAOInterface


class DAOProducts(DAOInterface):
    def __init__(self):
        self.conn = Connection()
        self.meta = self.conn.meta
        self.Products = Table(
            'Products',
            self.meta,
            Column('productsId', Integer, primary_key=True),
            Column('name', Text),
            Column('price', Float),
            Column('stock', Integer),
            Column('min', Integer),
            Column('max', Integer)
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
