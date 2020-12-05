from sqlalchemy import Table, Integer, Float, Text, Column

from dao.db import DB
from dao.DAOInterface import DAOInterface


class DAOProducts(DAOInterface):
    def __init__(self):
        self.db = DB()
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
        self.meta.create_all(self.db)
        self.conn = self.db.connection.connect()

    def selectAll(self):
        sel = self.Products.select()
        r = self.conn.execute(sel)
        return r.fetchall()


    def select(self, productId):
        pass

    def insert(self, product):
        ins = self.Products.insert().values(
            productsId=product._id,
            name=product._name,
            price=product._price,
            stock=product._stock,
            min=product._min,
            max=product._max
        )
        self.conn.execute(ins)

    def update(self, product):
        pass

    def delete(self, productId):
        pass
