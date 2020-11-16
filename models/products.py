class Product:
    def __init__(self, id, name, price, stock, min, max):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.min = min
        self.max = max

    def makeDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'min': self.min,
            'max': self.max
        }
