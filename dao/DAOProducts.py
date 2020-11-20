from dao.Connection import Connection
from dao.DAOInterface import DAOInterface
from models.Products import Product


class DAOProducts(DAOInterface):
    conn = Connection()

    def selectAll(self):
        cursor = self.conn.getNewCursor()
        stm = '''SELECT * FROM products;'''
        cursor.execute(stm)
        products = []
        rows = cursor.fetchall()
        for row in rows:
            p = Product(row[0], row[1], row[2], row[3], row[4], row[5])
            products.append(p)
        return products

    def select(self, productId):
        cursor = self.conn.getNewCursor()
        stm = ' SELECT * FROM products WHERE ' + productId + ' = "productsId";'
        cursor.execute(stm)
        row = cursor.fetchall()
        p = Product(row[0], row[1], row[2], row[3], row[4], row[5])
        return p

    def insert(self, product):
        pass

    def update(self, product):
        pass

    def delete(self, productId):
        pass
