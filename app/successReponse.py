from flask import (make_response, jsonify)
from app import errorConstant
from typing import Final
from http import HTTPStatus

SUCCESS_STATUS_CODE: Final = 200

def success():
    response = make_response(jsonify({"status" : SUCCESS_STATUS_CODE}))
    response.status_code = SUCCESS_STATUS_CODE
    response.headers['Content-Type'] = 'application/json'
    return response

def success_with_data(code):
    response = make_response(jsonify({"status" : SUCCESS_STATUS_CODE, "code":code}))
    response.status_code = SUCCESS_STATUS_CODE
    response.headers['Content-Type'] = 'application/json'
    
    return response

def success_with_data(code):
    SUCCESS_STATUS_CODE = 200
    response = make_response(jsonify({"status": SUCCESS_STATUS_CODE, "code": code}))
    response.status_code = SUCCESS_STATUS_CODE
    response.headers['Content-Type'] = 'application/json'
    return response
