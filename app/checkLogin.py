from flask import request, redirect, url_for
from flask_jwt_extended import decode_token
from jwt.exceptions import ExpiredSignatureError, DecodeError
from dotenv import load_dotenv
import os

load_dotenv()

def is_member(f):
    def decorated_function(*args, **kwargs):
        os.chdir('../')
        token_key = os.environ.get('COOKIE_TOKEN_KEY')
        token = request.cookies.get(token_key)
        if token is None:
            # 로그인 페이지로 리다이렉트
            return redirect(url_for("login"))
        try:
            username = decode_token(token)['username']
            userUUID = decode_token(token)['userUUID'] 
            # 토큰이 유효한 경우 함수 호출
            return f(username, userUUID, *args, **kwargs)
        except ExpiredSignatureError:
            # 토큰이 만료된 경우 로그인 페이지로 리다이렉트
            return redirect(url_for("login"))
        except DecodeError:
            return redirect(url_for("login"))
    return decorated_function
