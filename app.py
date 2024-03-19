from flask import Flask
from app.signup import signup_routes
from app.group import group_routes
from app.lobby import lobby_routes
from app.login import login_routes
from app.schedule import scedul_routes

from flask_jwt_extended import JWTManager
from app.config import app
from app.authConstant import SECRET_KEY

app = Flask(__name__)
jwt= JWTManager(app)
app.config['JWT_SECRET_KEY'] = SECRET_KEY


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
    app.run('0.0.0.0', debug=True, port=5000)