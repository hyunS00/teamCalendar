from flask import (render_template, request, make_response, redirect, url_for)
from app import db
from passlib.hash import pbkdf2_sha256
from datetime import timedelta, datetime
from app import authConstant
from app import tokenProvider

# 로그인 페이지
def login():
    return render_template('login.html')

# 로그인 요청
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
        userId = user.get('userId')
        userName = user.get('username')
    
        # 토큰 발급
        token, expiredTime = tokenProvider.provide(userId, userName)
        
        # 쿠키에 토큰 담기
        response = make_response(redirect(url_for('lobby.html'))) 
        response.set_cookie(authConstant.COOKIE_TOKEN_KEY, token, expires=expiredTime) 
        return response
            
login_routes = {
    'login': login,
    'login_post': login_post
}
