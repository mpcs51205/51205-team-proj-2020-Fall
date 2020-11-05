from flask import Flask,request,jsonify
from class_types import User, Acknowledgement
from tinydb import TinyDB, Query

app = Flask(__name__)

users_db = TinyDB('users.json')

@app.route("/create_user", methods=['PUT'])
def create_user():
    users_db.insert({'email': request.json['email'], 'password': request.json['password']})
    return jsonify(Acknowledgement(True).serialize()), 200

@app.route('/login', methods=['POST'])
def login():
    User = Query()
    results = users_db.search(User['email'] == request.json['email'] & 
    User['password'] == request.json['password'])
    if len(results) == 1:
        return jsonify(Acknowledgement(True).serialize()), 200
    else:
        return jsonify(Acknowledgement(False).serialize()), 404
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6662, debug=True)