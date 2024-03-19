from datetime import timedelta, datetime
from flask_jwt_extended import create_access_token

def provide(userUUID, userName):
    expiredTime = datetime.today() + timedelta(days=1)
    payload = {
        'userUUID' : userUUID,
        'username' : userName,
        'exp': expiredTime
    }
        
    # 토큰을 발급한다.
    token = create_access_token(identity=userUUID, additional_claims=payload)
    return token, expiredTime