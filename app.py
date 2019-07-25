from flask import Flask,request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def index():
    online_users = mongo.db.users.find({"online": True})
    data = {'1':'2'}
    mongo.db.users.insert_one(data)
    return "Hello, World!"

@app.route('/imports', methods=['POST'])
def imports():

    return "hi"


if __name__ == "__main__":
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo = PyMongo(app)
    app.run(debug=True, host='0.0.0.0', port=8080)
