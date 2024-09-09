from flask import make_response, render_template, flash, redirect, url_for, request
from helpers.utils import create_token, check_token, check_password, validate_phone_numbers, check_cep
from entry_data.entry_data import Login, Register, Registration_School
from models.db_models import Schools
from helpers.database_handler import get_session_for_school
from config_app import db

def config_routes(app):
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

    @app.route('/schools', methods=['GET', 'POST'])
    def schools():
        form = Registration_School()
        token = request.cookies.get('acess_token')
        
        error_message = 'None'
        
        if request.method == 'POST':
            if form.validate_on_submit():
                
                if validate_phone_numbers(form.telephone.data):
                    if isinstance(check_cep(form.cep.data), dict):
                        new_school = Schools(name=form.name.data, email=form.email.data, adress=form.cep.data, telephone=form.telephone.data)
                        db.session.add(new_school)
                        db.session.commit()
                        get_session_for_school(form.name.data.replace(' ', ''))
                        return redirect(url_for('inf'))
                    else:
                        error_message = 'CEP Inválido.'
                else:
                    error_message = 'Número inserido é inválido.'
            else:
                print(form.name.data, form.errors)
        
        if not token or not check_token(token):
            return redirect(url_for('login'))
        
        return render_template('create_school.html', form=form, error_message=error_message)


    @app.route('/infos-school')
    def inf():
        return render_template('infos_createSchool.html')