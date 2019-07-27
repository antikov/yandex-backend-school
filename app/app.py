from flask import Flask,request, redirect
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

@app.route('/')
def index():
    return str(next(DB['asa'].find()))
    #return str(next(mongo.cx['yandex-backend']['asa'].find()))
    #return str(mongo.cx.database_names())
    return str(next(mongo.db['asa'].find()))
    online_users = mongo.db['yandex-backend']['asa'].find({"online": True})
    data = {'1':'2'}
    mongo['yandex-backend'].users.insert_one(data)
    return "Hello, World!"

@app.route('/imports/<import_id>/citizens/<citizen_id>', methods=['PATCH'])
def change_citizen_info(import_id, citizen_id):
    return None

@app.route('/imports', methods=['POST'])
def imports():
    return "hi"


if __name__ == "__main__":
    app.config["MONGO_URI"] = os.environ.get('MONGODB_CONNECT_STRING')
    mongo = PyMongo(app)
    DB = mongo.cx['yandex-backend']
    app.run(debug=True, host='0.0.0.0', port=8080)
