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

@app.route("/inventory/add", methods=["POST"])
def add_inventory():
    data = request.json
    if not all(k in data for k in ("name", "quantity", "threshold")):
        return jsonify({"error": "Missing required fields"}), 400
    result = add_item(data)
    return jsonify(result)

@app.route("/inventory/update", methods=["POST"])
def update_inventory():
    data = request.json
    if not all(k in data for k in ("name", "delta")):
        return jsonify({"error": "Missing required fields"}), 400
    result = update_item(data)
    return jsonify(result)
