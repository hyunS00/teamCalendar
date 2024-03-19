from flask import render_template, request, redirect, url_for
from app.db import db

def signup():
    # todo : 회원가입 페이지로 변경하기
    return render_template('signup.html')

def signup_post():
    username = request.form['username']
    userId = request.form['userId']
    password = request.form['password']
    if db.users.find_one({'userId': userId}):
        print("이미 존재하는 사용자입니다. 다른 아이디 선택해주세요.")
    else:
        db.users.insert_one({'username': username, 'password': password})
        return render_template("lobby.html")
    
signup_routes = {
    'signup': signup,
    'signup_post': signup_post
}
