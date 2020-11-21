import requests
import json
from class_types import Item_base, Endpoint
from tinydb import TinyDB, Query
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)
endpoints = {}
items_db = TinyDB('items.json')
with open("endpoints.json") as endpoints_config:
    data = json.load(endpoints_config)
    for idx,ep in enumerate(data['services']):
        endpoints[ep['domain']] = Endpoint(ep['domain'],ep['ip'],ep['port'])
#pp.pprint(endpoints)

dummy_item = {'name':'giannis antetokounmpo', 'start_time':'2020-11-21 11:30:05', 'end_time':'2020-11-21 12:30:05', 'category':'nba_draft', 'start_bidding_price':'100000', 'buyout_price':'1000000', 'user_key':'0'}

#r= requests.put(endpoints['mediator'].get_prefix() + "create_auction_item", data=json.dumps(dummy_item),headers={'Content-Type':'application/json'})
#print(r.json(),r.status_code)

#r=requests.get(endpoints['mediator'].get_prefix() + "get_auction_items_by_key/" + args.key, headers={'Content-Type':'application/json'})
#print(r.json())

#r=requests.get(endpoints['mediator'].get_prefix() + "get_all_auction_items", headers={'Content-Type':'application/json'})
#print(r.json())

r=requests.get(endpoints['mediator'].get_prefix() + "get_auction_items_by_category/nba_draft", headers={'Content-Type':  'application/json'})
print(r.json())

