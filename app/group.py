from flask import render_template, request, redirect, url_for,jsonify
from app.db import db
from app.checkLogin import is_member

@is_member
def group():
    return render_template('group.html')

@is_member
def create_group():
    title_receive = request.form['title']
    start_date_receive = request.form['date']
    password_recive = request.form['password']
    userId_receive = request.form['userid']

    group_data = {
        'title' : title_receive, 'date' : start_date_receive, 'password' : password_recive, 'user' : userId_receive
    }

    db.group.insert_one(group_data)

    return render_template("schedul.html", title=title_receive)

group_routes = {
    'group': group,
    'create_group': create_group
}
