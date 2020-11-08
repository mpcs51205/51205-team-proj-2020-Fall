from flask import Flask,request,jsonify
from class_types import Item_base, Acknowledgement, Endpoint, User
from tinydb import TinyDB, Query
import requests
import json
import pprint
import argparse

app = Flask(__name__)
endpoints = {}
headers = {'Content-Type':'application/json'}
with open("endpoints.json") as endpoints_config:
    data = json.load(endpoints_config)
    for idx,ep in enumerate(data['services']):
        endpoints[ep['domain']] = Endpoint(ep['domain'],ep['ip'],ep['port'])

@app.route("/create_auction_item", methods=['PUT'])
def create_auction_item():
    r=requests.put(endpoints['auction'].get_prefix() + "create_auction_item", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

@app.route("/get_all_auction_items", methods=['GET'])
def get_all_auction_items():
    r=requests.get(endpoints['auction'].get_prefix() + "get_all_auction_items", headers=headers)
    return jsonify(r.json())

@app.route("/get_auction_items_by_key/<string:key>", methods=['GET'])
def get_auction_items_by_key(key):
    r=requests.get(endpoints['auction'].get_prefix() + "get_auction_items_by_key/" + key, headers=headers)
    return jsonify(r.json())

@app.route("/create_user", methods=['PUT'])
def create_user():
    r=requests.put(endpoints['user'].get_prefix() + "create_user", data=json.dumps(request.json), headers=headers)
    return jsonify(r.json())

@app.route('/login', methods=['POST'])
def login():
    r=requests.post(endpoints['user'].get_prefix() + "login", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6666, debug=True)