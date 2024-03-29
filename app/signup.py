from flask import (render_template, request, make_response, redirect, url_for)
from app import db
from app import tokenProvider
from passlib.hash import pbkdf2_sha256
from app.errorResponse import valid_error
from app.errorResponse import duplicated_error
from app.successReponse import success
from typing import Final
from app.cookieManager import set_cookie

MIN_LENGTH_USER_ID: Final = 5

DUPLICATED_USER_MESSAGE: Final = "이미 존재하는 사용자입니다."
MIN_LENGTH_USER_ID_MESSAGGE: Final = "아이디는 5글자 이상입니다."


# 회원가입 페이지
def signup():
    return render_template('signup.html')

# 회원가입 요청
def signup_post():
    data = request.json
    username = data.get("username")
    userId = data.get("userId")
    password= data.get("password")

    hashed_password = pbkdf2_sha256.hash(password)
    
    
    if db.users.find_one({'userId': userId}):
        return duplicated_error(DUPLICATED_USER_MESSAGE)
    elif len(userId)< MIN_LENGTH_USER_ID:
        return valid_error(MIN_LENGTH_USER_ID_MESSAGGE)
    else:
        result = db.users.insert_one({'userId': userId, 'username': username, 'password': hashed_password})
        
        # 토큰을 발급한다.
        userUUID = str(result.inserted_id)
        token, expiredTime = tokenProvider.provide(userUUID, username)
        
        # 토큰을 쿠키에 담는다.
        response = success()
        set_cookie(response, token, expiredTime)
        return response
    
signup_routes = {
    'signup': signup,
    'signup_post': signup_post
}
