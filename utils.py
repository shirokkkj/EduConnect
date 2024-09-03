import jwt
import datetime
import os
import string

def create_token(username):
    payload = {
        'sub': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }
    return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')

def check_token(token):
    try:
        t = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms='HS256')
        return 'Authenticated'  
    except jwt.InvalidTokenError as invalidated:
        return 'Invalid Token'
    except jwt.ExpiredSignatureError as expirated:
        return 'Expirated Token'
    
    
def check_password(password):
    if len(password) < 8:
        return False
    
    if not any(c.isupper for c in password):
        return False
    
    if not any(c.islower for c in password):
        return False
    
    if not any(c.isdigit for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    
    return True