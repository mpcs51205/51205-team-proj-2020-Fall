import requests
import json
from class_types import Item_base, Endpoint
from tinydb import TinyDB, Query
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("item_name")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)
endpoints = {}
items_db = TinyDB('items.json')
with open("endpoints.json") as endpoints_config:
    data = json.load(endpoints_config)
    for idx,ep in enumerate(data['services']):
        endpoints[ep['domain']] = Endpoint(ep['domain'],ep['ip'],ep['port'])
pp.pprint(endpoints)

dummy_item = {'name':args.item_name}
#print(endpoints['auction'].get_prefix() + "create_auction_item")
r= requests.put(endpoints['auction'].get_prefix() + "create_auction_item", data=json.dumps(dummy_item),headers={'Content-Type':'application/json'})
print(r.text,r.status_code)

