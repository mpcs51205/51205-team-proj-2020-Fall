from flask import Flask,request,jsonify
from class_types import Item_base, Acknowledgement_base, Item_Auction, Item_Ack
from tinydb import TinyDB, Query

app = Flask(__name__)

items_db = TinyDB('items.json')


@app.route("/bid_item", methods=['POST'])
def bid_item():
    item_key = request.json['item_key']
    user_key = request.json['user_key']
    bid_price = request.json['bid_price']
    if items_db.contains(doc_id=item_key):
        itemsdb.get(doc_id=item_key)

@app.route("/create_auction_item", methods=['PUT'])
def create_auction_item():
    key = items_db.insert({'name': request.json['name'], 'start_time':request.json['start_time'], 'end_time': request.json['end_time'], 'category': request.json['category'], 'start_bidding_price': request.json['start_bidding_price'], 'buyout_price': request.json['buyout_price'], 'user_key': request.json['user_key'], 'winning_bidder_key':-1, 'highest_bidding_price':-1, 'auction_state':'created'})
    items_db.update({'key':key}, doc_ids=[key])
    return jsonify(Item_Ack(True, key).serialize())

@app.route("/update_auction_item/<int:key>", methods=['PUT'])
def update_auction_item(key):
    if items_db.contains(doc_id=key):
        # find the item from db using key and update its properties
        items_db.update(request.json, doc_ids=[key])
        return jsonify(Item_Ack(True, key).serialize())
    return jsonify(Item_Ack(False, key).serialize())

@app.route("/remove_auction_item/<int:key>", methods=['PUT'])
def remove_auction_item(key):
    # find the item from db using key and delete the record from db
    if items_db.contains(doc_id=key):
        items_db.remove(doc_ids=[key])
        return jsonify(Item_Ack(True, key).serialize())
    return jsonify(Item_Ack(False, key).serialize())

@app.route("/get_all_auction_items", methods=['GET'])
def get_all_auction_items():
    #item_list = []
    #for item in items_db:
        #item_list.append((item['key'],item['name']))
    #return jsonify([item.serialize() for item in item_list])
    return jsonify(items_db.all())

@app.route("/get_auction_items_by_key/<int:key>", methods=['GET'])
def get_auction_items_by_key(key):
    query = Query()
    ret = items_db.search(query.key == key)
    #item_list = []
    #for item in ret:
        #item_list.append(Item_base(item['key'],item['name']))
    #return jsonify([item.serialize() for item in item_list])
    return jsonify(ret)

@app.route("/get_auction_items_by_category/<string:category>", methods=['GET'])
def get_auction_items_by_category(category):
    query = Query()
    ret = items_db.search(query.category == category)
    #item_list = []
    #for item in ret:
        #auction_item = Item_Auction(item['key'])
        # TODO populate all properties of Item_Auction and send it back.
        #item_list.append(auction_item)
    #return jsonify([item.serialize() for item in item_list])
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6664, debug=True)
