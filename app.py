from flask import Flask
from app.signup import signup_routes
from app.group import group_routes
from app.lobby import lobby_routes
from app.login import login_routes
from app.schedule import schedule_routes
from app.error import error_routes
from app.signout import signout_routes
from flask_jwt_extended import JWTManager
from app.authConstant import SECRET_KEY

app = Flask(__name__)
jwt= JWTManager(app)
app.config['JWT_SECRET_KEY'] = SECRET_KEY

app.add_url_rule('/', 'lobby', lobby_routes['lobby'] , methods=['GET'])
app.add_url_rule('/signup', 'signup', signup_routes['signup'] , methods=['GET'])
app.add_url_rule('/signup', 'signup_post', signup_routes['signup_post'], methods=['POST'])
app.add_url_rule('/signout','signout',signout_routes['signout'])


app.add_url_rule('/login', 'login', login_routes['login'] , methods=['GET'])
app.add_url_rule('/login', 'login_post', login_routes['login_post'], methods=['POST'])

app.add_url_rule('/group','group',group_routes['group'],methods=['GET'])
app.add_url_rule('/create_group','create_group',group_routes['create_group'],methods=['POST'])
app.add_url_rule('/find_group','find_group',group_routes['find_group'],methods=['POST'])
app.add_url_rule('/lobby','lobby',lobby_routes['lobby'],methods=['GET'])
app.add_url_rule('/schedule/<group_code>','schedule', schedule_routes['schedule'],methods=["GET"])
app.add_url_rule('/schedule_post/<group_code>','schedule_post',schedule_routes['schedule_post'],methods=["POST"])

app.add_url_rule('/error','error',error_routes['error'],methods=["GET"])

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=3000)
