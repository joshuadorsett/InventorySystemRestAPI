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
        sel = self.Parts.select()
        r = self.conn.execute(sel)
        return r.fetchall()

    def select(self, partsId):
        sel = self.Parts.select().where( self.Parts.partsId.like(partsId) )
        r = self.conn.execute(sel)
        return r.fetchone()

    def insert(self, part):
        ins = self.Parts.insert().values(
            partsId=part._id,
            name=part._name,
            price=part._price,
            stock=part._stock,
            min=part._min,
            max=part._max
        )
        self.conn.execute(ins)

    def update(self, part):
        pass

    def delete(self, partsId):
        pass
