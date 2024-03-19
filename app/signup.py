from flask import (render_template, request, make_response, redirect, url_for)
from app import db
from app import authConstant
from app import tokenProvider

def signup():
    return render_template('signup.html')

def signup_post():
    username = request.form['username']
    userId = request.form['userId']
    password = request.form['password']
    if db.users.find_one({'userId': userId}):
        print("이미 존재하는 사용자입니다. 다른 아이디 선택해주세요.")
    else:
        db.users.insert_one({'userId': userId, 'username': username, 'password': password})
        
        # 토큰을 발급받습니다.
        token, expiredTime = tokenProvider.provide(userId, username)
        
        # 토큰을 쿠키에 발급한다.
        response = make_response(redirect(url_for('lobby', username=username))) 
        response.set_cookie(authConstant.COOKIE_TOKEN_KEY, token, expires=expiredTime) 
        return response
    
signup_routes = {
    'signup': signup,
    'signup_post': signup_post
}
