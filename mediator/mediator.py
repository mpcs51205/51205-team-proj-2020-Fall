from flask import Flask,request,jsonify
from class_types import Item_base, Acknowledgement_base, Endpoint, User
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

#only user service should call create_auction_item
# request json should have append the following fields attached:
# ['name']
# ['start_time']
# ['end_time']
# ['category']
# ['start_bidding_price']
# ['buyout_price']
# ['user_key']
@app.route("/create_auction_item", methods=['PUT'])
def create_auction_item():
    r=requests.put(endpoints['auction'].get_prefix() + "create_auction_item", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

# only user/admin service should call update_auction_item
@app.route("/update_auction_item/<int:key>", methods=['PUT'])
def update_auction_item(key):
    r=requests.put(endpoints['auction'].get_prefix() + "update_auction_item/"+str(key), data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

#only user/admin service should call remove_auction_item
@app.route("/remove_auction_item/<int:key>", methods=['PUT'])
def remove_auction_item(key):
    r=requests.put(endpoints['auction'].get_prefix() + "remove_auction_item/"+str(key), data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

# fronend can directly call get_all_auction_items either for user or admin
@app.route("/get_all_auction_items", methods=['GET'])
def get_all_auction_items():
    r=requests.get(endpoints['auction'].get_prefix() + "get_all_auction_items", headers=headers)
    return jsonify(r.json())

# only user/admin should call get_auction_items_by_category to get details of items of one category
# category field should only contain alphabet letters or numbers, no special charactor(such as space) allowed.
@app.route("/get_auction_items_by_category/<string:category>", methods=['GET'])
def get_auction_items_by_category(category):
    r=requests.get(endpoints['auction'].get_prefix() + "get_auction_items_by_category/" + category, headers=headers)
    return jsonify(r.json())

# only user/admin should call get_auction_items_by_key to get details of an item
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

@app.route('/logout', methods=['POST'])
def logout():
    r=requests.post(endpoints['user'].get_prefix() + "logout", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

@app.route('/suspend', methods=['POST'])
def suspend():
    r=requests.post(endpoints['user'].get_prefix() + "suspend", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6666, debug=True)
