import sys
import os
# garante que o Python encontra a raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from controller.auth_controller import auth_bp
from controller.auth_controller import login_required
from chat.chatbot import chatbot_bp  # importa o blueprint do chatbot

app = Flask(__name__, template_folder="public/templates", static_folder="public/static")

# garante que o Python encontra a raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# chave secreta (ideal mover pra config/variável de ambiente em produção)
app.config['SECRET_KEY'] = 'uma_chave_secreta_segura'

# ----------------- Registro dos Blueprints -----------------
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chatbot_bp, url_prefix="/chatbot")

# ----------------- Rotas principais -----------------
@app.route("/")
def index():
    return render_template("PaginaTelaLogin.html")

@app.route("/cadastro")
def cadastro():
    return render_template("PaginaTelaCadastro.html")

@app.route("/home")
@login_required
def home():
    return render_template("PaginaHome.html")

@app.route("/apoiadores")
@login_required
def apoiadores():
    return render_template("PaginaApoiadores.html")

@app.route("/configuracoes")
@login_required
def configuracoes():
    return render_template("PaginaConfig.html")


# ----------------- Exercícios -----------------
@app.route("/exercicios")
@login_required
def exercicios():
    return render_template("PaginaExercicios.html")

@app.route("/exercicio-lacunas")
@login_required
def exercicio_lacunas():
    return render_template("PaginaLacunas.html")

@app.route("/exercicio-erros")
@login_required
def exercicio_erros():
    return render_template("PaginaCorrecaoErros.html")

@app.route("/exercicio-escuta")
@login_required
def exercicio_escuta():
    return render_template("PaginaEscuta.html")

# ----------------- Jogos -----------------
@app.route("/jogo-memoria")
@login_required
def jogo_memoria():
    return render_template("PaginaJogoMemoria.html")

@app.route("/jogo-formar-frase")
@login_required
def jogo_formar_frase():
    return render_template("PaginaJogoFormarFrase.html")

# ----------------- Pagina Escolhas -----------------
@app.route("/activities")
@login_required
def activities():
    return render_template("PaginaEscolhaAtividades.html")  

@app.route("/games")
@login_required
def games():
    return render_template("PaginaEscolhaGames.html") 

# ----------------- Inicialização -----------------
if __name__ == "__main__":
    app.run(debug=True)
