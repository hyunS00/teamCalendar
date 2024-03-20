from flask import (make_response, jsonify)
from app import errorConstant

def not_found_error(msg):
    response = make_response(jsonify({"msg": msg, "status" : errorConstant.NOT_FOUND}))
    response.headers['Content-Type'] = 'application/json'
    return response