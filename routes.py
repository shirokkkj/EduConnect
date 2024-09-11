from flask import make_response, render_template, flash, redirect, url_for, request
from helpers.utils import create_token, check_token, check_password, validate_phone_numbers, check_cep
from entry_data.entry_data import Login, Register, Registration_School, Register_Student
from models.db_models import Schools
from helpers.database_handler import get_session_for_school, get_matricula, Matricula
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
    
    
    @app.route('/matrículas')
    def matriculas():
        cookie_acess = request.cookies.get('acess_token')
        token_acess = check_token(cookie_acess)
        
        if not token_acess or not isinstance(token_acess, dict):
            return redirect(url_for('home'))
        
        
        mapping_tokens = {
            'Colégio Dinâmico': 'colégiodinâmico',
            'School Test': 'testschool'
        }
        
        all_matriculas = []
        
        escola = mapping_tokens.get(token_acess.get('sub'))
        print(escola)
        
        fetched_matricula = get_matricula(escola)
        
        for matricula in fetched_matricula:
            all_matriculas.append(matricula)
                       
        return render_template('matriculas.html', matriculas=all_matriculas)

    @app.route('/add_matricula', methods=['GET', 'POST'])
    def add_matricula():
        form = Register_Student()
        cookie_acess = request.cookies.get('acess_token')
        token_acess = check_token(cookie_acess)
        
        mapping_tokens = {
            'Colégio Dinâmico': 'colégiodinâmico',
            'School Test': 'testschool'
        }
        
        session = get_session_for_school(mapping_tokens.get(token_acess.get('sub')))
        
        if request.method == 'POST':
            if form.validate_on_submit():
                print('validated')
                nova_matricula = Matricula(
                    aluno_name=form.aluno_name.data,
                    ano_letivo=form.ano_letivo.data,
                    status=form.status.data,
                    periodo_letivo=form.periodo_letivo.data,
                    modalidade=form.modalidade.data,
                    data_cancelamento=form.data_cancelamento.data,
                    notas_finais=form.notas_finais.data,
                    forma_pagamento=form.forma_pagamento.data,
                    observacoes=form.observacoes.data
                )
                session.add(nova_matricula)
                session.commit()
                return redirect(url_for('matriculas'))
            else:
                print(form.errors)
        
        
        return render_template('create_matricula.html', form=form)


    @app.route('/infos-school')
    def inf():
        return render_template('infos_createSchool.html')
    
    
    @app.route('/logout')
    def logout():
        cookie = make_response(redirect(url_for('login')))
        
        cookie.set_cookie('acess_token', expires=0, secure=True)
        
        return cookie