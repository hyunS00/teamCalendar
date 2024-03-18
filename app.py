# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from app.signup import signup_routes

app = Flask(__name__)

# MongoDB 설정
client = MongoClient('mongodb://localhost:27017/')
db = client['first-jungle']

# 라우트 등록
app.add_url_rule('/signup', 'signup', signup_routes['signup'] , methods=['GET'])
app.add_url_rule('/signup', 'signup_post', signup_routes['signup_post'], methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)