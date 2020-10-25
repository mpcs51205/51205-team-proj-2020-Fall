from flask import Flask,request,jsonify
from class_types import Item_base, Acknowledgement
from tinydb import TinyDB, Query

app = Flask(__name__)

next_item_key = 0
key_items={}
def increment_item_key():
    global next_item_key
    next_item_key += 1

items_db = TinyDB('items.json')
for item in items_db:
    if(int(item['key']) > next_item_key):
        next_item_key = int(item['key'])
    key_items[item['key']] = Item_base(item['key'],item['name'])
increment_item_key()
print("next_item_key: ",next_item_key)

@app.route("/create_auction_item", methods=['PUT'])
def create_item():
    items_db.insert({'key': next_item_key, 'name': request.json['name']})
    key_items[next_item_key] = Item_base(next_item_key,request.json['name'])
    increment_item_key()
    return jsonify(Acknowledgement(True).serialize()),200

@app.route("/get_all_auction_items", methods=['GET'])
def get_all_auction_items():
    return jsonify([item.serialize() for item in key_items.values()]),200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6664, debug=True)
