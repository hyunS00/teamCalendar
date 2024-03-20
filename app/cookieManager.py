from app.envManager import get_value

def set_cookie(response, token, expiredTime):
    token_key = get_value('COOKIE_TOKEN_KEY')
    return response.set_cookie(token_key, token, expires=expiredTime) 

def delete_cookie(response):
    token_key = get_value('COOKIE_TOKEN_KEY')
    response.delete_cookie(token_key)
    return response