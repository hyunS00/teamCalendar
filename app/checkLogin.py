from flask import render_template, request, redirect
from flask_jwt_extended import decode_token
from jwt.exceptions import ExpiredSignatureError
from app import authConstant

def is_member(f):
    def decorated_function(*args, **kwargs):
        token = request.cookies.get(authConstant.COOKIE_TOKEN_KEY)
        
        if token is None:
            # 로그인 페이지로 리다이렉트
            return redirect('login.html')
        try:
            username = decode_token(token)['username']
            userUUID = decode_token(token)['userUUID'] 
            # 토큰이 유효한 경우 함수 호출
            return f(username, userUUID, *args, **kwargs)
        except ExpiredSignatureError:
            # 토큰이 만료된 경우 로그인 페이지로 리다이렉트
            return redirect("login.html")
    return decorated_function
