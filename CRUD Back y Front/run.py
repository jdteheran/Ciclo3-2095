
from flask import Flask, render_template, request, redirect, url_for
from src.db.connect import obtener_todos_estudiantes, registrar_estudiante, eliminar_estudiante_by_id, obtener_estudiante_by_correo
from src.email.correo import enviar_correo
from app.login.forms import FormInicio
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clave secreta'

@app.route('/', methods=['GET', 'POST'])
def login():
    form = FormInicio()

    if not(form.validate_on_submit()):
        return render_template('login/index.html', form=form)
    
    usuario = form.usuario.data
    estudiante_bd = obtener_estudiante_by_correo(usuario)

    if not(estudiante_bd):
        return render_template('login/index.html', form=form)
    
    contrasena = form.contrasena.data

    if not(contrasena == estudiante_bd[5]):
        return render_template('login/index.html', form=form)

    return redirect(url_for('home'))



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        estudiantes = obtener_todos_estudiantes()
        return render_template('index.html', estudiantes=estudiantes)
    elif request.method == 'POST':
        estudiante = json.loads(request.data.decode('utf_8'))
        #validaciones
        registrar_estudiante(estudiante)
        return 'registro exitoso'

@app.route('/get_all_students', methods=['GET'])
def get_all_students():
    estudiantes = obtener_todos_estudiantes()
    return estudiantes

@app.route('/eliminar_by_id', methods=['DELETE'])
def eliminar_by_id():
    estudiante_id = int(json.loads(request.data.decode('utf_8'))['id'])
    eliminar_estudiante_by_id(estudiante_id)
    return 'holaa'