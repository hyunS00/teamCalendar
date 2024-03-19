from flask import render_template, request
from app import authConstant
from app.checkLogin import is_member

@is_member
def lobby(username):   
    return render_template("lobby.html", username=username)
    
lobby_routes = {
    'lobby': lobby,
}