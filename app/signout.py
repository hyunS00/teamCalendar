from flask import request, redirect, url_for,make_response
from app.checkLogin import is_member
from app.cookieManager import delete_cookie

@is_member
def signout(username, userUUID):
    response = make_response(redirect(url_for("login")))
    return delete_cookie(response)

signout_routes = {
    'signout' :signout
}