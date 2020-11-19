from flask import Flask, jsonify, request, abort

from models.Part import Part
from models.Products import Product

# define the server object
rest = Flask(__name__)

# mock database
testPart = Part(0, "Hammer", 6.78, 689, 2, 23)
testProduct = Product(0, "ToolKit", 68.89, 320, 7, 90)
parts = []
products = []
parts.append(testPart)
products.append(testProduct)


# this function gets called when there is a GET request for /parts
@rest.route('/parts', methods=['GET'])
def getAllParts():
    print('all parts requested')
    partsDictList = []
    for part in parts:
        partsDictList.append(part.makeDict())
    return jsonify(partsDictList)


@rest.route('/products', methods=['GET'])
def getAllProducts():
    print('all products requested')
    productDictList = []
    for product in products:
        productDictList.append(product.makeDict())
    return jsonify(productDictList)


# this function gets called when there is a GET request for /parts/id
@rest.route('/parts/<int:id>', methods=['GET'])
def getParts(id):
    for part in parts:
        partId = part.getId()
        if partId == id:
            return jsonify(part.makeDict())
    else:
        return 'id not found'


@rest.route('/products/<int:id>', methods=['GET'])
def getProducts(id):
    for product in products:
        productId = product.getId()
        if productId == id:
            return jsonify(product.makeDict())
    else:
        return 'id not found'


# when post method is received this converts json to dictionary item
# and adds it to inventory
@rest.route('/parts', methods=['POST'])
def addParts():
    if not request.json:
        abort(400)
    newPart = Part(
        request.json['id'],
        request.json['name'],
        request.json['price'],
        request.json['stock'],
        request.json['min'],
        request.json['max']
    )
    parts.append(newPart)
    return jsonify(newPart.makeDict())


@rest.route('/products', methods=['POST'])
def addProducts():
    if not request.json:
        abort(400)
    newProduct = Product(
        request.json['id'],
        request.json['name'],
        request.json['price'],
        request.json['stock'],
        request.json['min'],
        request.json['max']
    )
    products.append(newProduct)
    return jsonify(newProduct.makeDict())


# this selects a certain part to delete
@rest.route('/parts/<int:id>', methods=['PUT'])
def updateParts(id):
    newPart = Part(
        request.json['id'],
        request.json['name'],
        request.json['price'],
        request.json['stock'],
        request.json['min'],
        request.json['max']
    )
    for part in parts:
        partId = part.getId()
        if partId == id:
            parts.insert(partId, newPart)
            parts.remove(partId + 1)


@rest.route('/products/<int:id>', methods=['PUT'])
def updateProducts(id):
    newProduct = Product(
        request.json['id'],
        request.json['name'],
        request.json['price'],
        request.json['stock'],
        request.json['min'],
        request.json['max']
    )
    for product in products:
        productId = product.getId()
        if productId == id:
            products.insert(productId, newProduct)
            products.remove(productId + 1)


# this selects a certain part to delete
@rest.route('/parts/<int:id>', methods=['DELETE'])
def deleteParts(id):
    for part in parts:
        partId = part.getId()
        if partId == id:
            parts.remove(partId)


@rest.route('/products/<int:id>', methods=['DELETE'])
def deleteProducts(id):
    for product in products:
        productId = product.getId()
        if productId == id:
            products.remove(productId)


if __name__ == '__main__':
    rest.run(debug=True)
