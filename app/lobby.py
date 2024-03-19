from flask import render_template, request
from app import authConstant
from app.checkLogin import is_member

@is_member
def lobby():   
    return render_template("lobby.html")
    
lobby_routes = {
    'lobby': lobby,
}