"""
EJECUTAR EN TERMINAL
python -m venv mi_entorno
mi_entorno\Scripts\activate
"""

import pyodbc
import psycopg2

sql_server_conect = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-D48KJDG\\SQLEXPRESS;"
    "DATABASE=Restaurante;"
    "UID=sa;"
    "PWD=12345678;"
)

pg_conn = psycopg2.connect(
    dbname="restaurante",
    user="desmon",
    password="12345678",
    host="localhost",
    port="5432"
)

sql_cursor = sql_server_conect.cursor()
pg_cursor = pg_conn.cursor()


sql_cursor.execute("SELECT Nombre, Apellido, CC, Correo, Celular FROM clientes;")
clientes = sql_cursor.fetchall()

insert_query = """
    INSERT INTO clientes (Nombre, Apellido, CC, Correo, Celular) 
    VALUES (%s, %s, %s, %s, %s)
"""

for cliente in clientes:
    pg_cursor.execute(insert_query, cliente)

pg_conn.commit()

# Cerrar conexiones
sql_cursor.close()
sql_server_conect.close()
pg_cursor.close()
pg_conn.close()

print("Migración completada...")