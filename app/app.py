from flask import Flask, request, redirect
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

@app.route('/')
def index():
    return str(next(DB['asa'].find()))
    # return str(next(mongo.cx['yandex-backend']['asa'].find()))
    # return str(mongo.cx.database_names())
    # return str(next(mongo.db['asa'].find()))
    # online_users = mongo.db['yandex-backend']['asa'].find({"online": True})
    # data = {'1':'2'}
    # mongo['yandex-backend'].users.insert_one(data)
    # return "Hello, World!"

@app.route('/imports', methods=['POST'])
def imports():
    """
    Принимает на вход набор с данными о жителях в формате json.
    """
    return "hi"

@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def change_citizen_info(import_id, citizen_id):
    """
    Изменяет информацию о жителе в указанном наборе данных.
    """
    return None

@app.route('/imports/<int:import_id>/citizens', methods=['GET'])
def get_citizens(import_id):
    """
    Возвращает список всех жителей для указанного набора данных.
    """
    return None

@app.route('/imports/<int:import_id>/citizens/birthdays', methods=['GET'])
def get_citizen_presents(import_id):
    """
    Возвращает жителей и количество подарков, которые они будут покупать своим
    ближайшим родственникам (1-го порядка), сгруппированных по месяцам из
    указанного набора данных.
    """
    return None

@app.route('imports/<int:import_id>/towns/stat/percentile/age', methods=['GET'])
def get_town_stats(import_id):
    """
    Возвращает статистику по городам для указанного набора данных в разрезе
    возраста жителей: p50, p75, p99, где число - это значение перцентиля.
    """
    return None


if __name__ == "__main__":
    app.config["MONGO_URI"] = os.environ.get('MONGODB_CONNECT_STRING')
    mongo = PyMongo(app)
    DB = mongo.cx['yandex-backend']
    app.run(debug=True, host='0.0.0.0', port=8080)
