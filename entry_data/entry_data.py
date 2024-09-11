from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField, IntegerField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class Login(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    
    submit = SubmitField('Entrar')
    

class Register(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired(), EqualTo('repeat_password')])
    repeat_password = PasswordField('Repita sua senha', validators=[DataRequired()])
    email = EmailField('Digite seu e-mail', validators=[DataRequired()])
    remember = BooleanField('Lembrar-me')
    
    
    submit = SubmitField('Entrar')
    
    
class Registration_School(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=5, max=255)])
    email = EmailField(validators=[DataRequired()])
    cep = StringField(validators=[DataRequired()])
    telephone = StringField(validators=[DataRequired()])
    
    
    submit = SubmitField('Junte-se a nós!')
    
class Register_Student(FlaskForm):
    aluno_name = StringField(validators=[DataRequired(), Length(min=5, max=60)])
    ano_letivo = IntegerField(validators=[DataRequired()])
    status = StringField(default='ativa')  # ativa, trancada, cancelada, concluída
    periodo_letivo = StringField(validators=[DataRequired(),Length(min=5, max=50)])  # ex: 1º semestre
    modalidade = StringField(validators=[DataRequired(), Length(min=3, max=20)])  # presencial, EAD, híbrido
    data_cancelamento = DateField(validators=[DataRequired()])
    notas_finais = TextAreaField()  # pode ser usado JSON para mais flexibilidade
    forma_pagamento = StringField(validators=[DataRequired(), Length(min=5, max=50)])
    observacoes = TextAreaField()