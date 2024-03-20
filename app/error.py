from flask import render_template, request
from app import authConstant
from app.checkLogin import is_member

def error(username, userId):   
    return render_template("error.html")
    
error_routes = {
    'error': error,
}