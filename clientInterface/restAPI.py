from flask import Flask, jsonify, request, abort

from models.part import Part
from models.products import Product

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
def getAllParts():
    print('all products requested')
    productDictList = []
    for product in products:
        productDictList.append(product.makeDict())
    return jsonify(productDictList)


# this function gets called when there is a GET request for /parts/id
@rest.route('/parts/<int:id>', methods=['GET'])
def getParts(id):
    for part in parts:
        if part.id == id:
            return jsonify(part.makeDict())
    else:
        return 'id not found'


@rest.route('/products/<int:id>', methods=['GET'])
def getProducst(id):
    for product in products:
        if product.id == id:
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
        if part.id == id:
            parts.insert(part.id, newPart)
            parts.remove(part.id + 1)


# this selects a certain part to delete
@rest.route('/parts/<int:id>', methods=['DELETE'])
def deleteParts(id):
    for part in parts:
        if part.id == id:
            parts.remove(part.id)


if __name__ == '__main__':
    rest.run(debug=True)
