from flask import (make_response, jsonify)
from app import errorConstant
from typing import Final
from http import HTTPStatus

SUCCESS_STATUS_CODE: Final = 200

def success():
    response = make_response(jsonify({"message": "Success"}))
    response.status_code = SUCCESS_STATUS_CODE
    response.headers['Content-Type'] = 'application/json'
    
    return response

