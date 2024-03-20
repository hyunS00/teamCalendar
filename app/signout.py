from flask import request, redirect, url_for,make_response
from app.checkLogin import is_member
import os
from dotenv import load_dotenv

load_dotenv()

@is_member
def signout(username, userUUID):
    response = make_response(redirect(url_for("login")))
    os.chdir('../')
    token_key = os.environ.get('COOKIE_TOKEN_KEY')
    response.delete_cookie(token_key)
    return response

signout_routes = {
    'signout' :signout
}