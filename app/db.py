from pymongo import MongoClient

# MongoDB 설정
client = MongoClient('mongodb://mdtest:mdtest@3.83.48.49',27017)
db = client['first-jungle']

# user 컬렉션
users = db['users']
# 그룹 컬렉션
groups = db["groups"]
# 스케줄 컬렉션
schedule = db["schedule"]
