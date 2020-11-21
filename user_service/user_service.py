from flask import Flask, request, jsonify
from class_types import User, Acknowledgement
from tinydb import TinyDB, Query, where

app = Flask(__name__)

users_db = TinyDB('users.json')

@app.route("/create_user", methods=['PUT'])
def create_user():
    User = Query()
    results = users_db.search(User['email'] == request.json['email'])
    if (len(results)) != 0:
        return jsonify(Acknowledgement(False).serialize()), 500
    else:
        users_db.insert({'email': request.json['email'], 'password': request.json['password'],
                         'login': False, 'suspend': False})
        return jsonify(Acknowledgement(True).serialize()), 200

@app.route('/login', methods=['POST'])
def login():
    User = Query()
    results = users_db.search(User['email'] == request.json['email'] and
                              User['password'] == request.json['password'] and
                              User['suspend'] == False)
    if len(results) == 1:
        id = results[0].doc_id
        users_db.update({'login': True}, doc_ids=[id])
        return jsonify(Acknowledgement(True).serialize()), 200
    else:
        return jsonify(Acknowledgement(False).serialize()), 404

@app.route('/logout', methods=['POST'])
def logout():
    users_db.update({'login': False}, doc_ids=[request.json['id']])
    return jsonify(Acknowledgement(True).serialize()), 200

@app.route('/suspend', methods=['POST'])
def suspend():
    users_db.update({'suspend': True}, doc_ids=[request.json['id']])
    return jsonify(Acknowledgement(True).serialize()), 200

# @app.route('/create_item_for_user', methods=['POST'])
# def create_item_for_user():

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6662, debug=True)
