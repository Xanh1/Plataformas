from flask import Blueprint, jsonify, make_response, request
from models.rol import Rol

api = Blueprint('api', __name__)

@api.route('/')

def home():
    return make_response(
        jsonify({"msg": "OK",
                 "code": 200,
                 }),
        401
    )


@api.route('/suma/<a>/<b>')
def suma(a, b):
    c = float(a) + float(b)
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "data":{"suma es: ": c}}), 
        200
    )

@api.route('/sumar', methods = ["POST"])
def suma_post():
    data = request.json
    #print(data["a"])
    c = float(data["a"]) + float(data["b"])
    #c = 0
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "data":{"suma es: ": c}}), 
        200
    )