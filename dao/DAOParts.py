from sqlalchemy import Table, Integer, Column, Text, Float

from dao.db import DB
from dao.DAOInterface import DAOInterface
from models.Part import Part


class DAOParts(DAOInterface):
    def __init__(self):
        self.db = DB()
        self.meta = self.db.meta
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
        query = r.fetchall()
        parts = []
        for p in query:
            part = Part(p[0], p[1], p[2], p[3], p[4], p[5])
            parts.append(part)
        return parts

    def select(self, partsId):
        sel = self.Parts.select().where( self.Parts.partsId.like(partsId) )
        r = self.conn.execute(sel)
        p = r.fetchone()
        part = Part(p[0], p[1], p[2], p[3], p[4], p[5])
        return part

    def insert(self, part):
        ins = self.Parts.insert().values(
            name=part._name,
            price=part._price,
            stock=part._stock,
            min=part._min,
            max=part._max
        )
        self.conn.execute(ins)

    def update(self, part):
        upd = self.Parts.update().values(
            name=part._name,
            price=part._price,
            stock=part._stock,
            min=part._min,
            max=part._max
        )
        self.conn.execute(upd)

    def delete(self, partsId):
        dele = self.Parts.delete().where(self.Parts.partsId.like(partsId))
        self.conn.execute(dele)
