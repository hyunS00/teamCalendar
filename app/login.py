from flask import (render_template, request, make_response, redirect, url_for, jsonify)
from app import db
from passlib.hash import pbkdf2_sha256
from app import authConstant
from app import tokenProvider
from app.errorResponse import not_found_error
from typing import Final

NOT_FOUND_USER: Final = "해당하는 사용자가 없습니다."

# 로그인 페이지
def login():
    return render_template('login.html')

# 로그인 요청
def login_post():
    userId = request.form['userId']
    password = request.form['password']
    
    user = db.users.find_one({'userId': userId})
    if user is None:
        return not_found_error(NOT_FOUND_USER)
    
    hashedPassword=user["password"]
    if(pbkdf2_sha256.verify(password, hashedPassword)):
        return not_found_error(NOT_FOUND_USER)
    
    else:
        userId = user.get('userId')
        userName = user.get('username')
    
        # 토큰 발급
        token, expiredTime = tokenProvider.provide(userId, userName)
        
        # 쿠키에 토큰 담기
        response = make_response(redirect(url_for('lobby'))) 
        response.set_cookie(authConstant.COOKIE_TOKEN_KEY, token, expires=expiredTime) 
        return response
            
login_routes = {
    'login': login,
    'login_post': login_post
}
