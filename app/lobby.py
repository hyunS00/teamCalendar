from flask import render_template, request
from app.checkLogin import is_member

@is_member
def lobby(username, userId):   
    return render_template("lobby.html", username=username)
    
lobby_routes = {
    'lobby': lobby,
}