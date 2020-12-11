import psycopg2
from flask import Flask, jsonify, request, abort

from dao.DAOParts import DAOParts
from dao.DAOProducts import DAOProducts
from models.Part import Part
from models.Products import Product

# define the server object
rest = Flask(__name__)

# instantiate Database Access Objects
partsDao = DAOParts()
productsDao = DAOProducts()

# this function gets called when there is a GET request for /parts
@rest.route('/parts', methods=['GET'])
def getAllParts():
    print('all parts requested')
    parts = partsDao.selectAll()
    partsDictList = []
    for part in parts:
        partsDictList.append(part.makeDict())
    return jsonify(partsDictList)

@rest.route('/products', methods=['GET'])
def getAllProducts():
    print('all products requested')
    products = productsDao.selectAll()
    productDictList = []
    for product in products:
        productDictList.append(product.makeDict())
    return jsonify(productDictList)

# this function gets called when there is a GET request for /parts/id
@rest.route('/parts/<int:id>', methods=['GET'])
def getParts(id):
    part = partsDao.select(id)
    return jsonify(part.makeDict())

@rest.route('/products/<int:id>', methods=['GET'])
def getProducts(id):
    product = productsDao.select(id)
    return jsonify(product.makeDict())

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
    partsDao.insert(newPart)
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
    productsDao.insert(newProduct)
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
    parts = partsDao.selectAll()
    for part in parts:
        partId = part.getId()
        if partId == id:
            partsDao.update(newPart)
    return jsonify(newPart.makeDict())

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
    products = productsDao.selectAll()
    for product in products:
        productId = product.getId()
        if productId == id:
            productsDao.update(newProduct)
    return jsonify(newProduct.makeDict())

# this selects a certain part to delete
@rest.route('/parts/<int:id>', methods=['DELETE'])
def deleteParts(id):
    parts = partsDao.selectAll()
    for part in parts:
        partId = part.getId()
        if partId == id:
            partsDao.delete(partId)
            return jsonify(part.makeDict())


@rest.route('/products/<int:id>', methods=['DELETE'])
def deleteProducts(id):
    products = productsDao.selectAll()
    for product in products:
        productId = product.getId()
        if productId == id:
            productsDao.delete(productId)
            return jsonify(product.makeDict())


if __name__ == '__main__':
    connection = psycopg2.connect(
        dbname="InventorySystemDB",
        user="joshua",
        password="password",
        host="localhost",
        port="5433"
    )
    rest.run(debug=True)
