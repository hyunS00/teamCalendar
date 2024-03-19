from flask import render_template, request, redirect, url_for,jsonify
from app.db import db
from app.checkLogin import is_member

@is_member
def group(username, userId):
    return render_template('group.html', username=username)

@is_member
def create_group(username, userUUID):
    title_receive = request.form['title']
    start_date_receive = request.form['date']

    group_data = {
        'title' : title_receive, 'date' : start_date_receive, 'userUUID' : userUUID
    }

    result = db.groups.insert_one(group_data)
    group_code = str(result.inserted_id)
    return redirect(url_for("schedul", title=title_receive, groupId=group_code))

@is_member
def find_group(username, userUUID):   
    # 방 찾은 이후에 해당 방 스케줄로 들어가기
    group_code = request.form['group_code']
    group = db.groups.find_one({"_id" : group_code})
    return render_template("schedul.html", groupId= group_code)

group_routes = {
    'group': group,
    'create_group': create_group,
    'find_group' : find_group
}
