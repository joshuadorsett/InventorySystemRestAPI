from models.ModelsInterface import ModelsInterface


class Association(ModelsInterface):
    def __init__(self, partId, productId):
        self._partId = partId
        self._productId = productId

    def makeDict(self):
        return {
            'partId': self._partId,
            'productId': self._productId
        }