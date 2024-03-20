from flask import render_template, request, redirect, url_for,jsonify, make_response
from app.db import db
from passlib.hash import pbkdf2_sha256
import uuid
from app.checkLogin import is_member
from app.errorResponse import not_found_error
from typing import Final

NOT_FOUND_GROUP: Final = "해당하는 방이 없습니다."

@is_member
def group(username, userUUID):
    return render_template('group.html', username=username)

@is_member
def create_group(username, userUUID):
    title_receive = request.form['title']
    start_date_receive = request.form['date']
    group_code = str(uuid.uuid4()).split('-')[0] 
    group_data = {
        'title' : title_receive, 'date' : start_date_receive, 'userUUID' : userUUID, 'group_uuid': group_code
    }

    db.groups.insert_one(group_data)
    return redirect(url_for("schedule", group_code=group_code))

@is_member
def find_group(username, userUUID):   
    data = request.json
    group_code = data.get("group_code")

    group = db.groups.find_one({"group_uuid" : group_code})
    
    if group is None:
        return not_found_error(NOT_FOUND_GROUP)
    
    else:
        return redirect(url_for("schedule", group_code=group_code))

group_routes = {
    'group': group,
    'create_group': create_group,
    'find_group' : find_group
}
