import sys
import os
# garante que o Python encontra a raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from controller.auth_controller import auth_bp
from chatbot.chatbot import chatbot_bp  # importa o blueprint do chatbot


# garante que o Python encontra a raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

# chave secreta (ideal mover pra config/variável de ambiente em produção)
app.config['SECRET_KEY'] = 'uma_chave_secreta_segura'

# ----------------- Registro dos Blueprints -----------------
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chatbot_bp, url_prefix="/chatbot")

# ----------------- Rotas principais -----------------
@app.route("/")
def index():
    return render_template("PaginaLogin/PaginaLogin.html")

@app.route("/cadastro")
def cadastro():
    return render_template("PaginaCadastro/index.html")

@app.route("/home")
def home():
    return render_template("home.html")

# ----------------- Exercícios -----------------
@app.route("/exercicios")
def exercicios():
    return render_template("exercicios/pg_exercicios/index.html")

@app.route("/exercicio-lacunas")
def exercicio_lacunas():
    return render_template("exercicios/exercicioslacunas/index.html")

@app.route("/exercicio-erros")
def exercicio_erros():
    return render_template("exercicios/exercicio erros/index.html")

@app.route("/exercicio-escuta")
def exercicio_escuta():
    return render_template("exercicios/exerciciodeescuta/index.html")

# ----------------- Jogos -----------------
@app.route("/jogo-memoria")
def jogo_memoria():
    return render_template("exercicios/PG_JOGODAMEMORIA/index.html")

@app.route("/jogo-formar-frase")
def jogo_formar_frase():
    return render_template("exercicios/PG_JOGODAMEMORIA/jogoFormarFrase.html")

# ----------------- Inicialização -----------------
if __name__ == "__main__":
    app.run(debug=True)
