from flask import Flask, render_template, make_response, redirect, url_for, flash, request
from entry_data.entry_data import Login, Register
import os
import bcrypt
from dotenv import load_dotenv
from utils import create_token, check_token, check_password

salt = bcrypt.gensalt()

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    
    token = request.cookies.get('acess_token')
    if token:
        return redirect(url_for('home'))
    
    if form.validate_on_submit():
        
        cookie = make_response(redirect(url_for('home')))
        token = create_token(form.name.data)
        cookie.set_cookie('acess_token', token, secure=True)
        return cookie
    else:
        flash('Usuário não encontrado.', 'error')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    token = request.cookies.get('acess_token')
    if token:
        return redirect(url_for('home'))
    
    error_message = 'None'
    form = Register()
    if form.validate_on_submit():
        try:
            if check_password(str(form.repeat_password.data)):
                cookie = make_response(redirect(url_for('home')))
                token = create_token(form.name.data)
                cookie.set_cookie('acess_token', token, secure=True)
                return cookie
            else:
                error_message = 'Sua senha é muito fraca.'
        except:
            error_message = 'Houve algum erro no seu registro. Por favor, tente novamente.'
    return render_template('register.html', form=form, error_message=error_message)


@app.route('/home')
def home():
    token = request.cookies.get('acess_token')
    if not token or not check_token(token):
        return redirect(url_for('login'))
    
    return render_template('home.html')


app.run(debug=True)