# app.py
from flask import Flask
from app.signup import signup_routes
from app.group import group_routes
from app.lobby import lobby_routes
from app.login import login_routes
from app.schedule import scedul_routes

app = Flask(__name__)

# 라우트 등록
app.add_url_rule('/signup', 'signup', signup_routes['signup'] , methods=['GET'])
app.add_url_rule('/signup', 'signup_post', signup_routes['signup_post'], methods=['POST'])

app.add_url_rule('/login', 'login', login_routes['login'] , methods=['GET'])
app.add_url_rule('/login', 'login_post', login_routes['login_post'], methods=['POST'])

app.add_url_rule('/group','group',group_routes['group'],methods=['GET'])
app.add_url_rule('/create_group','create_group',group_routes['create_group'],methods=['POST'])
app.add_url_rule('/lobby','lobby',lobby_routes['lobby'],methods=['GET'])
app.add_url_rule('/schedule','schedul',scedul_routes['schedul'],methods=["GET"])


if __name__ == '__main__':
    app.run(debug=True, port=4000)