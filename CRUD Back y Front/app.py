from flask import Flask, render_template
from src.db.connect import conn as conexion
app = Flask(__name__)

@app.route('/')
def login():
    return 'Login'


@app.route('/home')
def home():
    return render_template('index.html')
