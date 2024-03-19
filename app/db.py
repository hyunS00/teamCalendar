from pymongo import MongoClient

# MongoDB 설정
client = MongoClient('mongodb://localhost:27017/')
db = client['first-jungle']

# user 컬렉션
users = db['users']
groups = db["groups"]
