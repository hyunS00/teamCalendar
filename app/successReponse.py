from flask import (make_response, jsonify)
from app import errorConstant
from typing import Final
from http import HTTPStatus

SUCCESS_STATUS_CODE: Final = 200

def success():
    response = make_response()
    response.status_code=HTTPStatus.OK
    response.headers['Content-Type'] = 'application/json'
    
    return response

