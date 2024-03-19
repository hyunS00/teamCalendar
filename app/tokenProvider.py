from datetime import timedelta, datetime
from flask_jwt_extended import create_access_token

def provide(userId, userName):
    expiredTime = datetime.today() + timedelta(minutes=60 * 60 * 24)
    payload = {
        'id': userId,
        'username' : userName,
        'exp': expiredTime
    }
        
    # 토큰을 발급한다.
    token = create_access_token(identity=userId)
    return token, expiredTime