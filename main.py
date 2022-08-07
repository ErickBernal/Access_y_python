import sys
from os import getcwd
import pyodbc
#print (pyodbc.drivers())
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\pilloubool\Desktop\EjemploAccess\Database1.accdb;')

cursor =conn.cursor()

#cursor.execute('SELECT * FROM Ventas')

cursor.execute('''
INSERT INTO  Categorías (IdCat,Categoría)   
VALUES(16,\'Edificios\')''')
conn.commit()

cursor.execute('SELECT * FROM Categorías')
for row in cursor.fetchall():
    print(row)


cursor.close()
conn.close()