from flask import (make_response, jsonify)
from app import errorConstant

def not_found_error(msg):
    response = make_response(jsonify({"msg": msg, "status" : errorConstant.NOT_FOUND}))
    response.status_code=errorConstant.NOT_FOUND
    response.headers['Content-Type'] = 'application/json'
    return response

def duplicated_error(msg):
    response = make_response(jsonify({"msg": msg, "status" : errorConstant.DUPLICATED}))
    response.status_code=errorConstant.DUPLICATED
    response.headers['Content-Type'] = 'application/json'
    return response

def valid_error(msg):
    response = make_response(jsonify({"msg": msg, "status" : errorConstant.NOT_VALID}))
    response.status_code=errorConstant.DUPLICATED
    response.headers['Content-Type'] = 'application/json'
    return response