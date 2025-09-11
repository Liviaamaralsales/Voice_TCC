
import pymysql
from werkzeug.security import generate_password_hash


db_config = {
    "host": "localhost",
    "user": "root",
    "database": "voice",
     "cursorclass": pymysql.cursors.DictCursor
    }
def get_db_connection():
    return pymysql.connect(**db_config) # if its all great, return connection correct

def buscar_usuario_por_rm_e_email(rm, email): #create function to search rm and email
    conn = get_db_connection()
    try:
       with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM usuarios WHERE rm = %s AND email = %s', (rm, email))
            return cursor.fetchone()
    finally:
        conn.close() #close connection

def cadastrar(rm, email, senha_hash): # the function serves to register user in BD, if its possible with password_hash, to upgrade security.
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO usuarios (rm, email, senha) VALUES (%s, %s, %s) 
            ''', (rm, email, senha_hash)) #protect data, to login 
            conn.commit()
    finally:
        conn.close() #close connection
def buscar_usuario_por_email(email): #create function to search just email 
        conn = get_db_connection()
        try:
             with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
                return cursor.fetchone()
        finally:
            conn.close() #close connection
