
import pymysql

# Configuração da conexão
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",   # ⚠️ Coloque sua senha do MySQL aqui
    "database": "voice",
    "cursorclass": pymysql.cursors.DictCursor
}

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    return pymysql.connect(**db_config)


def buscar_usuario_por_rm_e_email(rm, email):
    """Busca usuário pelo RM e Email."""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM usuarios WHERE rm = %s AND email = %s',
                (rm, email)
            )
            return cursor.fetchone()
    finally:
        conn.close()


def cadastrar(nome, data_nascimento, email, senha_hash):
    """Cadastra um novo usuário no banco de dados."""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (nome, data_nascimento, email, senha) VALUES (%s, %s, %s, %s)",
                (nome, data_nascimento, email, senha_hash)
            )
            conn.commit()
    finally:
        conn.close()


def buscar_usuario_por_email(email):
    """Busca usuário pelo Email."""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            return cursor.fetchone()
    finally:
        conn.close()
