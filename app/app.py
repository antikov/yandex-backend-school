from flask import Flask, request, abort, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import time
import datetime
from collections import defaultdict
import numpy as np


app = Flask(__name__)


def result_wrapper(result):
    return jsonify({
        "data": result
    })

@app.route('/imports', methods=['POST'])
def imports():
    """
    Принимает на вход набор с данными о жителях в формате json.
    """
    result = request.json['citizens']
    print(result)
    import_id = "".join(str(time.time()).split("."))
    DB.create_collection(import_id)
    DB[import_id].insert_many(result)
    result = { 'import_id' : import_id}
    return result_wrapper(result), 201

@app.route('/imports/<string:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def change_citizen_info(import_id, citizen_id):
    """
    Изменяет информацию о жителе в указанном наборе данных.
    """
    return result_wrapper({})

@app.route('/imports/<string:import_id>/citizens', methods=['GET'])
def get_citizens(import_id):
    """
    Возвращает список всех жителей для указанного набора данных.
    """

    if import_id not in DB.list_collection_names():
        abort(400)

    result = list(DB[import_id].find())
    for record in result:
        del record['_id']
    return result_wrapper(result)

@app.route('/imports/<string:import_id>/citizens/birthdays', methods=['GET'])
def get_citizen_presents(import_id):
    """
    Возвращает жителей и количество подарков, которые они будут покупать своим
    ближайшим родственникам (1-го порядка), сгруппированных по месяцам из
    указанного набора данных.
    """
    return result_wrapper({})

@app.route('/imports/<string:import_id>/towns/stat/percentile/age', methods=['GET'])
def get_town_statistics(import_id):
    """
    Возвращает статистику по городам для указанного набора данных в разрезе
    возраста жителей: p50, p75, p99, где число - это значение перцентиля.
    """
    if import_id not in DB.list_collection_names():
        abort(400)
    result = list(DB[import_id].find())

    towns = defaultdict(list)
    today = datetime.date.today()
    get_age = lambda born: today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    for record in result:
        towns[record['town']].append(get_age(datetime.datetime.strptime(record['birth_date'],"%d.%m.%Y")))

    answer = []
    for town in towns.keys():
        percentiles = list(map(int, np.percentile(towns[town], [50, 75, 99], interpolation='linear')))
        answer.append({
            "town" : town, 
            "p50" : percentiles[0],
            "p75" : percentiles[1],
            "p99" : percentiles[2]
        })
    return result_wrapper(answer)


if __name__ == "__main__":
    app.config["MONGO_URI"] = os.environ.get('MONGODB_CONNECT_STRING')
    mongo = PyMongo(app)
    DB = mongo.cx['yandex-backend']
    app.run(debug=True, host='0.0.0.0', port=8080)
