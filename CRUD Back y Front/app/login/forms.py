from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Iniciar Sesión')
