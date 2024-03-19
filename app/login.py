from flask import (render_template, request, make_response, redirect, url_for)
from app import db
from passlib.hash import pbkdf2_sha256
from datetime import timedelta, datetime
from flask_jwt_extended import create_access_token
from app import authConstant
from app import tokenProvider


def login():
    # todo : 로그인 페이지로 변경하기
    return render_template('index.html')

def login_post():
    userId = request.form['userId']
    password = request.form['password']
    
    user = db.users.find_one({'userId': userId})
    if user is None:
        print("해당하는 사용자가 없습니다.")
    
    hashedPassword=user["password"]
    if(pbkdf2_sha256.verify(password, hashedPassword)):
        print("비밀번호가 일치하지 않습니다.")
    
    else:
        # userId와 userName을 가져옵니다.
        userId = user.get('userId')
        userName = user.get('username')
    
        # 토큰을 발급받습니다.
        token, expiredTime = tokenProvider.provide(userId, userName)
        
        # 토큰을 쿠키에 발급한다.
        response = make_response(redirect(url_for('lobby.html'))) 
        response.set_cookie(authConstant.COOKIE_TOKEN_KEY, token, expires=expiredTime) 
        return response
            
login_routes = {
    'login': login,
    'login_post': login_post
}
