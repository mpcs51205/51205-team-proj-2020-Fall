import requests
import json
from class_types import Item_base, Endpoint
from tinydb import TinyDB, Query
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("user")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)
endpoints = {}
users_db = TinyDB('users.json')
with open("endpoints.json") as endpoints_config:
    data = json.load(endpoints_config)
    for idx,ep in enumerate(data['services']):
        endpoints[ep['domain']] = Endpoint(ep['domain'],ep['ip'],ep['port'])
pp.pprint(endpoints)

dummy_user = {'name':args.user}
r= requests.put(endpoints['user'].get_prefix() + "user_login", data=json.dumps(dummy_user),headers={'Content-Type':'application/json'})
print(r.text,r.status_code)