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

# only user/admin service should call remove_auction_item
@app.route("/remove_auction_item/<int:key>", methods=['PUT'])
def remove_auction_item(key):
    r=requests.put(endpoints['auction'].get_prefix() + "remove_auction_item/"+str(key), headers=headers)
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

# front end can directly call create user, return 200 or 404
@app.route("/create_user", methods=['PUT'])
def create_user():
    r=requests.put(endpoints['user'].get_prefix() + "create_user", data=json.dumps(request.json), headers=headers)
    return jsonify(r.json())

# only user can call login, return 200 or 404
@app.route('/login', methods=['POST'])
def login():
    r=requests.post(endpoints['user'].get_prefix() + "login", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

# only user can call logout, return 200
@app.route('/logout', methods=['POST'])
def logout():
    r=requests.post(endpoints['user'].get_prefix() + "logout", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

# user and admin can call suspend, return 200
@app.route('/suspend', methods=['POST'])
def suspend():
    r=requests.post(endpoints['user'].get_prefix() + "suspend", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

# user and admin can call remove_account, return 200
@app.route('/remove_account', methods=['POST'])
def remove_account():
    r=requests.post(endpoints['user'].get_prefix() + "remove_account", data=json.dumps(request.json),headers=headers)
    return jsonify(r.json())

# user can call create_item_for_user and it will return acknowledgement
@app.route('/create_item_for_user/<int:user_key>', methods=['POST'])
def create_item_for_user(user_key):
    r=requests.post(endpoints['user'].get_prefix() + "create_item_for_user/" + str(user_key), data=json.dumps(request.json), headers=headers)
    return jsonify(r.json())

# user can call update_item_for_user and it will return acknowledgement
@app.route('/update_item_for_user/<int:user_key>/<int:item_key>', methods=['POST'])
def update_item_for_user(user_key, item_key):
    r=requests.post(endpoints['user'].get_prefix() + "update_item_for_user/" + str(user_key) + "/" + str(item_key), data=json.dumps(request.json), headers=headers)
    return jsonify(r.json())

# user can remove_item_for_user and it will return acknowledgement
@app.route('/remove_item_for_user/<int:user_key>/<int:item_key>', methods=['POST'])
def remove_item_for_user(user_key, item_key):
    r=requests.post(endpoints['user'].get_prefix() + "remove_item_for_user/" + str(user_key) + "/" + str(item_key), data=json.dumps(request.json), headers=headers)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6666, debug=True)
