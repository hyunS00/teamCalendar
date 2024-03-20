from flask import render_template, request
from app.checkLogin import is_member

def error():   
    return render_template("error.html")
    
error_routes = {
    'error': error,
}