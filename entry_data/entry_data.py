from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField
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
    adress = StringField(validators=[DataRequired()])
    telephone = StringField(validators=[DataRequired()])
    
    
    submit = SubmitField('Junte-se a nós!')