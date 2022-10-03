
from flask import Flask, render_template, request
from src.db.connect import obtener_todos_estudiantes, registrar_estudiante
import json
app = Flask(__name__)

@app.route('/')
def login():
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
