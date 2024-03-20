from flask import request, redirect, url_for,make_response
from app import authConstant
from app.checkLogin import is_member

@is_member
def signout(username, userUUID):
    response = make_response(redirect(url_for("login")))
    response.delete_cookie(authConstant.COOKIE_TOKEN_KEY)
    return response

signout_routes = {
    'signout' :signout
}