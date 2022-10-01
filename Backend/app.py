from flask import Flask, jsonify, request, render_template
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html', hola='Uninorte')
    