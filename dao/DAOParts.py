from dao.Connection import Connection
from dao.DAOInterface import DAOInterface
from models.Part import Part


class DAOParts(DAOInterface):
    conn = Connection()

    def selectAll(self):
        cursor = self.conn.getNewCursor()
        stm = 'SELECT * FROM parts'
        cursor.execute(stm)
        parts = []
        rows = cursor.fetchall()
        for row in rows:
            p = Part(row[0], row[1], row[2], row[3], row[4], row[5])
            parts.append(p)
        return parts

    def select(self, partsId):
        cursor = self.conn.getNewCursor()
        stm = ' SELECT * FROM parts' \
              'WHERE ' + partsId + ' = partsId'
        cursor.execute(stm)
        row = cursor.fetchall()
        p = Part(row[0], row[1], row[2], row[3], row[4], row[5])
        return p

    def insert(self, part):
        pass

    def update(self, part):
        pass

    def delete(self, partsId):
        pass
