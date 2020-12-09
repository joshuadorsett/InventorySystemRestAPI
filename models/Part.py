from models.ModelsInterface import ModelsInterface


class Part(ModelsInterface):
    def __init__(self, id, name, price, stock, min, max):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock
        self._min = min
        self._max = max

    def getDict(self):
        return {
            'id': self._id,
            'name': self._name,
            'price': self._price,
            'stock': self._stock,
            'min': self._min,
            'max': self._max
        }

    def getId(self):
        return self._id
