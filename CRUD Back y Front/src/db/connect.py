import sqlite3
import os

url = os.path.abspath(os.getcwd()) + '/db/estudiantes.sqlite'

def obtener_todos_estudiantes():
    conn = sqlite3.connect(url)

    crsr = conn.cursor()
    crsr.execute('SELECT * FROM estudiantes')
    result = crsr.fetchall()

    conn.close()

    return result

def registrar_estudiante(estudiante):
    conn = sqlite3.connect(url)

    crsr = conn.cursor()
    crsr.execute('INSERT INTO estudiantes (nombre, apellido, celular, correo, contrasena) VALUES("{}","{}","{}","{}","{}")'
                    .format(estudiante['nombre'], estudiante['apellido'], estudiante['celular'], estudiante['correo'], estudiante['contrasena']))
    
    conn.commit()
    
    conn.close()

def eliminar_estudiante_by_id(id):
    conn = sqlite3.connect(url)

    crsr = conn.cursor()
    crsr.execute('DELETE FROM estudiantes WHERE id={}'.format(id))
    
    conn.commit()
    
    conn.close()

def obtener_estudiante_by_correo(correo):
    conn = sqlite3.connect(url)

    crsr = conn.cursor()
    crsr.execute('SELECT * FROM estudiantes where correo="{}"'.format(correo))
    result = crsr.fetchone()

    conn.close()

    return result