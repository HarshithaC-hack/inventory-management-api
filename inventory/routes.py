# Flask routes
from flask import Flask, request, jsonify
from inventory.logic import *

app = Flask(__name__)

@app.route("/inventory/add", methods=["POST"])
def add_inventory():
    data = request.json
    result = add_item(data)
    return jsonify(result)

@app.route("/inventory/update", methods=["POST"])
def update_inventory():
    data = request.json
    result = update_item(data)
    return jsonify(result)

@app.route("/inventory/all", methods=["GET"])
def get_inventory():
    return jsonify(get_all_items())