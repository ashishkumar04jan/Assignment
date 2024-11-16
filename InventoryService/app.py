from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/inventory_db"  # Replace with your MongoDB URI
mongo = PyMongo(app)

@app.route('/inventory/<int:product_id>', methods=['GET'])
def get_inventory(product_id):
    logger.info("Fetching inventory for product_id: %s", product_id)
    print("get_inventory")
    inventory = mongo.db.inventory.find_one({"product_id": product_id})
    if inventory:
        return jsonify({"product_id": inventory["product_id"], "stock": inventory["stock"]})
    return jsonify({"error": "Product not found"}), 404

@app.route('/inventory', methods=['POST'])
def add_inventory():
    logger.info("Fetching inventory for product_id: %s", request.json)
    print("add_inventory")
    data = request.json
    new_inventory = {
        "product_id": data['product_id'],
        "stock": data['stock']
    }
    mongo.db.inventory.insert_one(new_inventory)
    print("inserted value")
    return jsonify({"message": "Inventory added"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
