import requests
import json
from class_types import Item_base, Endpoint
from tinydb import TinyDB, Query
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key")
parser.add_argument("item_key")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)
endpoints = {}

with open("endpoints.json") as endpoints_config:
    data = json.load(endpoints_config)
    for idx,ep in enumerate(data['services']):
        endpoints[ep['domain']] = Endpoint(ep['domain'],ep['ip'],ep['port'])
# pp.pprint(endpoints)

dummy_user = {'email':"mpcs.uchicago.51205@gmail.com", 'password':"Michael Jordan"}
#r = requests.put(endpoints['test_mediator'].get_prefix() + "create_user", data = json.dumps(dummy_user),headers={'Content-Type':'application/json'})
#print(r.json(),r.status_code)

r = requests.post(endpoints['test_mediator'].get_prefix() + "login", data=json.dumps(dummy_user),headers={'Content-Type':'application/json'})
print(r.json(),r.status_code)

# new_email_updated_user = {'email':"newmichaeljordan@email.com", 'id':1}
# r = requests.post(endpoints['test_mediator'].get_prefix() + "update_email", data=json.dumps(new_email_updated_user),headers={'Content-Type':'application/json'})
# print(r.json(),r.status_code)

#new_password_updated_user = {'password':"new Michael Jordan", 'id':1}
#r = requests.post(endpoints['test_mediator'].get_prefix() + "update_password", data=json.dumps(new_password_updated_user),headers={'Content-Type':'application/json'})
#print(r.json(),r.status_code)

# user_id = {'id':1}
# r = requests.post(endpoints['test_mediator'].get_prefix() + "logout", data=json.dumps(user_id),headers={'Content-Type':'application/json'})
# print(r.json(), r.status_code)

# r = requests.post(endpoints['test_mediator'].get_prefix() + "suspend", data=json.dumps(user_id),headers={'Content-Type':'application/json'})
# print(r.json(), r.status_code)

# r = requests.post(endpoints['test_mediator'].get_prefix() + "remove_account", data=json.dumps(user_id),headers={'Content-Type':'application/json'})
# print(r.json(), r.status_code)

dummy_item = {'name':'lebron James', 'start_time':'2020-11-21 11:30:05', 'end_time':  '2020-12-21 12:30:05', 'category':'nba_draft', 'start_bidding_price':100000, 'buyout_price': 888000000, 'user_key':1}

r = requests.post(endpoints['test_mediator'].get_prefix() + "create_item_for_user/1", data=json.dumps(dummy_item), headers={'Content-Type':'application/json'})
print(r.json(), r.status_code)

# updated_dummy_item = {'name':'new new new kevin garnett', 'start_time':'2020-11-21 11:30:05', 'end_time':  '2020-11-21 12:30:05', 'category':'nba_draft', 'start_bidding_price':100000, 'buyout_price':   1000000, 'user_key':1}

# r = requests.post(endpoints['test_mediator'].get_prefix() + "update_item_for_user/" + args.key + "/" + args.item_key, data=json.dumps(updated_dummy_item), headers={'Content-Type':'application/json'})
# print(r.json(), r.status_code)

# key = {'item_key': 3}
# r = requests.post(endpoints['test_mediator'].get_prefix() + "remove_item_for_user/" + args.key + "/" + args.item_key, data=json.dumps(key), headers={'Content-Type':'application/json'})
# print(r.json(), r.status_code)

#item_to_add = {'item_key': 1, 'id': 1}
#r = requests.post(endpoints['test_mediator'].get_prefix() + "add_to_cart", data=json.dumps(item_to_add),headers={'Content-Type':'application/json'})
#print(r.json(),r.status_code)

#item_to_remove = {'item_key': 1, 'id': 1}
#r = requests.post(endpoints['test_mediator'].get_prefix() + "remove_from_cart", data=json.dumps(item_to_remove),headers={'Content-Type':'application/json'})
#print(r.json(),r.status_code)
