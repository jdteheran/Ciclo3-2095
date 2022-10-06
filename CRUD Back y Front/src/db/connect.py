import sqlite3


def obtener_todos_estudiantes():
    conn = sqlite3.connect('db/estudiantes.sqlite')

    crsr = conn.cursor()
    crsr.execute('SELECT * FROM estudiantes')
    result = crsr.fetchall()

    conn.close()

    return result

def registrar_estudiante(estudiante):
    conn = sqlite3.connect('db/estudiantes.sqlite')

    crsr = conn.cursor()
    crsr.execute('INSERT INTO estudiantes (nombre, apellido, celular, correo, contrasena) VALUES("{}","{}","{}","{}","{}")'
                    .format(estudiante['nombre'], estudiante['apellido'], estudiante['celular'], estudiante['correo'], estudiante['contrasena']))
    
    conn.commit()
    
    conn.close()

def eliminar_estudiante_by_id(id):
    conn = sqlite3.connect('db/estudiantes.sqlite')

    crsr = conn.cursor()
    crsr.execute('DELETE FROM estudiantes WHERE id={}'.format(id))
    
    conn.commit()
    
    conn.close()
