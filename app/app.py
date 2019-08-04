from flask import Flask, request, abort, jsonify
from flask_pymongo import PyMongo
import os
from collections import defaultdict
import numpy as np
from utils import parse_date, get_age
from validator import validate_imports

app = Flask(__name__)

def result_wrapper(result):
    return jsonify({
        "data": result
    })

def get_import_id():
    return DB['counters'].find_one_and_update(
        {"_id" : 31337},
        {'$inc' : {"import_id":1}},
        new=True
    )['import_id']


@app.route('/test', methods=['GET'])
def test():
    return result_wrapper(get_import_id())

@app.route('/imports', methods=['POST'])
def imports():
    """
    Принимает на вход набор с данными о жителях в формате json.
    """
    data = request.json['citizens']
    try:
        validate_imports(data)
    except:
        abort(400)
    
    import_id = str(get_import_id())
    DB.create_collection(import_id)
    DB[import_id].insert_many(data)
    result = { 'import_id' : int(import_id)}
    return result_wrapper(result), 201

@app.route('/imports/<string:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def change_citizen_info(import_id, citizen_id):
    """
    Изменяет информацию о жителе в указанном наборе данных.
    """
    return result_wrapper({}), 200

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
    return result_wrapper(result), 200

@app.route('/imports/<string:import_id>/citizens/birthdays', methods=['GET'])
def get_citizen_presents(import_id):
    """
    Возвращает жителей и количество подарков, которые они будут покупать своим
    ближайшим родственникам (1-го порядка), сгруппированных по месяцам из
    указанного набора данных.
    """
    if import_id not in DB.list_collection_names():
        abort(400)

    result = list(DB[import_id].find())
    presents = {month:dict() for month in range(1, 13)}
    citizens = dict()
    for record in result:
        citizens[record['citizen_id']] = {'birth_date' : record['birth_date'], 'relatives' : record['relatives']}
    for citizen in citizens.keys():
        for relative in citizens[citizen]['relatives']:
            month = parse_date(citizens[relative]['birth_date']).month
            presents[month][citizen] = presents[month].get(citizen, 0) + 1
    answer = {}
    for month in range(1,13):
        key = str(month)
        answer[key] = list()
        for present in presents[month].keys():
            answer[key].append({"citizen_id" : present, "presents" : presents[month][present]})
    return result_wrapper(answer), 200

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
    for record in result:
        towns[record['town']].append(get_age(parse_date(record['birth_date'])))

    answer = []
    for town in towns.keys():
        percentiles = list(map(int, np.percentile(towns[town], [50, 75, 99], interpolation='linear')))
        answer.append({
            "town" : town, 
            "p50" : percentiles[0],
            "p75" : percentiles[1],
            "p99" : percentiles[2]
        })
    return result_wrapper(answer), 200


if __name__ == "__main__":
    app.config["MONGO_URI"] = os.environ.get('MONGODB_CONNECT_STRING')
    mongo = PyMongo(app)
    DB = mongo.cx['yandex-backend']

    if 'counters' not in DB.list_collection_names():
        DB['counters'].insert_one({'_id' : 31337,'import_id':0})

    app.run(debug=True, host='0.0.0.0', port=8080)
