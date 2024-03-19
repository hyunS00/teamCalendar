from flask import Flask
from flask_jwt_extended import JWTManager
from app.authConstant import SECRET_KEY

app = Flask(__name__)
jwt= JWTManager(app)
app.config['JWT_SECRET_KEY'] = SECRET_KEY