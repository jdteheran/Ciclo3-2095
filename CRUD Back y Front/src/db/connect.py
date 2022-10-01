import sqlite3

conn = sqlite3.connect('db/estudiantes.sqlite')
print ("Opened database successfully")

print('holaaa')
conn.close()