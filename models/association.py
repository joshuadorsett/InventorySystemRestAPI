class Association:
    def __init__(self, partId, productId):
        self.partId = partId
        self.productId = productId

    def makeDict(self):
        return {
            'partId': self.partId,
            'productId': self.productId
        }