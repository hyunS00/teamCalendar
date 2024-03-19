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

    db.groups.insert_one(group_data)
    return render_template("schedul.html", title=title_receive)

group_routes = {
    'group': group,
    'create_group': create_group
}
