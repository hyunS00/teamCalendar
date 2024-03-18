# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from app.signup import signup_routes
from app.group import group_routes

app = Flask(__name__)

# 라우트 등록
app.add_url_rule('/signup', 'signup', signup_routes['signup'] , methods=['GET'])
app.add_url_rule('/signup', 'signup_post', signup_routes['signup_post'], methods=['POST'])
app.add_url_rule('/group','group',group_routes['group'],methods=['GET'])
app.add_url_rule('/create_group','create_group',group_routes['create_group'],methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)