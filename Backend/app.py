from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hola():
    diccionario = {
        'nombre': 'Juan',
        'apellido': 'Teheran',
        'correo': 'jdteheran@uninorte.edu.co'
        }
    return jsonify(diccionario)

@app.route('/login', methods=['POST'])
def login():
    variable = json.loads(request.data.decode("utf-8"))
    print(variable)
    print(variable['user'])
    print(variable['password'])
    return 'login exitoso'

