from flask import render_template, request, redirect, url_for,jsonify, make_response
from app.db import db
from passlib.hash import pbkdf2_sha256
import uuid
from app.checkLogin import is_member
from app.errorResponse import not_found_error
from typing import Final
from app.successReponse import success_with_data

NOT_FOUND_GROUP: Final = "해당하는 방이 없습니다."

@is_member
def group(username, userUUID):
    return render_template('group.html', username=username)

@is_member
def create_group(username, userUUID):
    data = request.json
    
    title = data.get("title")
    date = data.get("date")
    
    group_code = str(uuid.uuid4()).split('-')[0] 
    group_data = {
        'title' : title, 'date' : date, 'userUUID' : userUUID, 'group_uuid': group_code
    }
    
    db.groups.insert_one(group_data)
    
    return success_with_data(group_code)


@is_member
def find_group(username, userUUID):   
    data = request.json
    group_code = data.get("group_code")

    group = db.groups.find_one({"group_uuid" : group_code})
    
    if group is None:
        return not_found_error(NOT_FOUND_GROUP)
    
    else:
        response = success_with_data(group_code)
        return response

group_routes = {
    'group': group,
    'create_group': create_group,
    'find_group' : find_group
}
