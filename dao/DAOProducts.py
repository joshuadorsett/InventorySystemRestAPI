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
        cursor = self.conn.getNewCursor()
        stm = 'INSERT INTO products (name, price, stock, min, max) ' \
              'VALUES (' + product._name + ', ' + product._price + ', ' + product._stock + ',' \
              + product._min + ', ' + product._max + ')'
        cursor.execute(stm)
        return "new product was inserted"

    def update(self, product):
        cursor = self.conn.getNewCursor()
        stm = 'UPDATE products ' \
              'SET name = ' + product._name + ', ' \
              + 'price = ' + product._price + ', ' \
              + 'stock = ' + product._stock + ', ' \
              + 'min = ' + product._min + ', ' \
              + 'max = ' + product._max \
              + 'WHERE productsId = ' + product.getId() + ';'
        cursor.execute(stm)
        return "product was updated"

    def delete(self, productId):
        cursor = self.conn.getNewCursor()
        stm = 'DELETE FROM products WHERE productId = ' + productId + ';'
        cursor.execute(stm)
        return "product was deleted"
