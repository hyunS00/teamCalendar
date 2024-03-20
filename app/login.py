from flask import (render_template, request, make_response, redirect, url_for, jsonify)
from app import db
from passlib.hash import pbkdf2_sha256
from app import tokenProvider
from app.errorResponse import not_found_error
from app.successReponse import success
from typing import Final
from app.cookieManager import set_cookie

NOT_FOUND_USER: Final = "해당하는 사용자가 없습니다."

# 로그인 페이지
def login():
    return render_template('login.html')

# 로그인 요청
def login_post():
    data = request.json

    userId = data.get("userId")
    password= data.get("password")
    print("패스워드")
    print(password)
    
    user = db.users.find_one({'userId': userId})
    if user is None:
        return not_found_error(NOT_FOUND_USER)
    
    print(userId)
    hashedPassword=user["password"]
    
    if(pbkdf2_sha256.verify(password, hashedPassword)):
        userId = user.get('userId')
        userName = user.get('username')
        userUUID = str(user['_id'])
        # 토큰 발급
        token, expiredTime = tokenProvider.provide(userUUID, userName)
        
        # 쿠키에 토큰 담기
        response = success()
        set_cookie(response, token, expiredTime)
        return response
    else:
        return not_found_error(NOT_FOUND_USER)
            
login_routes = {
    'login': login,
    'login_post': login_post
}
