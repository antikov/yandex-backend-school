from flask import Flask, request, abort, jsonify
from flask_pymongo import PyMongo
import os
from collections import defaultdict
import numpy as np
from utils import parse_date, get_age
from validator import validate_imports, validate_patch
from pymongo import ReturnDocument

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

def get_table_name(import_id):
    return f"import_{import_id}"

@app.route('/imports', methods=['POST'])
def imports():
    """
    Принимает на вход набор с данными о жителях в формате json.
    """
    data = request.json
    try:
        validate_imports(data)
    except:
        abort(400)
    import_id = get_import_id()
    import_table = get_table_name(import_id)
    DB.create_collection(import_table)
    #if empty:
    if len(data['citizens']) > 0:
        DB[import_table].insert_many(data['citizens'])
    result = { 'import_id' : import_id}
    return result_wrapper(result), 201

@app.route('/imports/<string:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def change_citizen_info(import_id, citizen_id):
    """
    Изменяет информацию о жителе в указанном наборе данных.
    """

    import_table = get_table_name(import_id)
    if import_table not in DB.list_collection_names():
        abort(404)
    
    current = DB[import_table].find_one({"citizen_id" : citizen_id})
    if not current:
        abort(404)

    data = request.json
    try:
        validate_patch(data)
        # validate relatives
        if 'relatives' in data:
            # cant be own relative
            assert citizen_id not in data['relatives']

            # dublicate check
            assert len(data['relatives']) == len(set(data['relatives']))

            #bad citizen_id in relatives check
            for relative in data['relatives']:
                assert DB[import_table].find({"citizen_id" : relative})
    except:
        abort(400)

    if 'relatives' in data:
        # delete old relatives
        for relative in current['relatives']:
            DB[import_table].find_one_and_update({"citizen_id" : relative}, {"$pull" : citizen_id})
        # add new relatives
        for relative in data['relatives']:
            DB[import_table].find_one_and_update({"citizen_id" : relative}, {"$addToSet" : citizen_id})

    #patch
    result = DB[import_table].find_one_and_update({ "citizen_id" : citizen_id}, { "$set" : data}, return_document=ReturnDocument.AFTER)
    if result:
        return result_wrapper(result), 200
    else:
        abort(500)

@app.route('/imports/<string:import_id>/citizens', methods=['GET'])
def get_citizens(import_id):
    """
    Возвращает список всех жителей для указанного набора данных.
    """
    import_table = get_table_name(import_id)
    if import_table not in DB.list_collection_names():
        abort(404)

    result = list(DB[import_table].find())
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
    import_table = get_table_name(import_id)
    if import_table not in DB.list_collection_names():
        abort(404)

    result = list(DB[import_table].find())
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
    import_table = get_table_name(import_id)
    if import_table not in DB.list_collection_names():
        abort(404)

    result = list(DB[import_table].find())
    towns = defaultdict(list)
    for record in result:
        towns[record['town']].append(get_age(parse_date(record['birth_date'])))

    answer = []
    for town in towns.keys():
        percentiles = [round(percentile, 2) for percentile in np.percentile(towns[town], [50, 75, 99], interpolation='linear')]
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
        DB['counters'].insert_one({'_id' : 31337, 'import_id' : 0})

    app.run(debug=True, host='0.0.0.0', port=8080)
