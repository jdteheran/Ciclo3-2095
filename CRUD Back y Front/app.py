
from flask import Flask, render_template, request
from src.db.connect import obtener_todos_estudiantes, registrar_estudiante, eliminar_estudiante_by_id
from src.email.correo import enviar_correo
import json
app = Flask(__name__)

@app.route('/')
def login():
    enviar_correo('correo', 'correo desde app', 'este es mi mensaje de correo')
    return 'Login'


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