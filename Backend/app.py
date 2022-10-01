from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hola():
    return 'Hola mundo'

@app.route('/contacto')
def contacto():
    return 'pantalla de contacto'


@app.route('/perfil')
def pefil():
    return 'pantalla de perfil'

@app.route('/api/<string:nombre>')
def saludar(nombre):
    return 'mandamos un saludo a:' + nombre

@app.route('/api2')
@app.route('/api2/<string:nombre>')
@app.route('/api2/<string:nombre>/<string:apellido>')
def credencial(nombre='vacio', apellido='vacio'):
    return 'el apellido de {} es {}'.format(nombre, apellido)