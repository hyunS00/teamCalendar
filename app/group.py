from flask import render_template, request, redirect, url_for,jsonify
from app.db import db
from passlib.hash import pbkdf2_sha256
import uuid
from app.checkLogin import is_member

@is_member
def group(username, userUUID):
    return render_template('group.html', username=username)

@is_member
def create_group(username, userUUID):
    title_receive = request.form['title']
    start_date_receive = request.form['date']
    group_uuid = str(uuid.uuid4()).split('-')[0] 
    group_data = {
        'title' : title_receive, 'date' : start_date_receive, 'userUUID' : userUUID, 'group_uuid': group_uuid
    }

    db.groups.insert_one(group_data)
    return redirect(url_for("schedul", title=title_receive, group_code=group_uuid))

@is_member
def find_group(username, userUUID):   
    # 방 찾은 이후에 해당 방 스케줄로 들어가기
    group_code = request.form['group_code']
    group = db.groups.find_one({"groupd_code" : group_code})
    return render_template("schedul.html", group_code= group_code)

group_routes = {
    'group': group,
    'create_group': create_group,
    'find_group' : find_group
}
