import jwt
import datetime
import os
import string
import phonenumbers
import requests


def create_token(username):
    payload = {
        'sub': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }
    return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')

def check_token(token):
    try:
        t = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms='HS256')
        return t
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


def validate_phone_numbers(phonenumber):
    try:
        phone = phonenumbers.parse(phonenumber)
        if not phonenumbers.is_valid_number(phone):
            return False
    except phonenumbers.NumberParseException as error:
        return False
    
    return True


def check_cep(cep):
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return {
                'cep': data.get('cep'),
                'logradouro': data.get('logradouro'),
                'complemento': data.get('complemento'),
                'bairro': data.get('bairro'),
                'cidade': data.get('localidade'),
                'estado': data.get('uf')
            }
        else:
            return 'CEP não encontrado.'
    else:
        return 'Erro ao buscar CEP.'
    

def return_token(cookie):
    return check_token(cookie)