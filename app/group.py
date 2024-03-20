from flask import render_template, request, redirect, url_for,jsonify
from app.db import db
from passlib.hash import pbkdf2_sha256
import uuid
from app.checkLogin import is_member

@is_member
def group(username, userId):
    return render_template('group.html', username=username)

@is_member
def create_group(username, userUUID):
    title_receive = request.form['title']
    start_date_receive = request.form['date']
    group_uuid = str(uuid.uuid4()).split('-')[0] 
    group_data = {
        'title' : title_receive, 'date' : start_date_receive, 'userUUID' : userUUID, 'group_uuid': group_uuid
    }

    result = db.groups.insert_one(group_data)
    id = str(result.inserted_id)
    return render_template("schedul.html", title=title_receive)

group_routes = {
    'group': group,
    'create_group': create_group
}
