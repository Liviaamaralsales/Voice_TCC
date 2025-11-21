import sys
import os

# -------------------------------------------------------
# Ajustes de path para garantir que o HostGator encontre tudo
# -------------------------------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(base_dir, "controller"))
sys.path.append(os.path.join(base_dir, "chat"))
sys.path.append(os.path.join(base_dir, "model"))

# Mantendo seu path original para compatibilidade
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# -------------------------------------------------------
from flask import Flask, render_template, session
from controller.auth_controller import auth_bp
from controller.auth_controller import login_required
from chat.chatbot import chatbot_bp
from controller.avatar_controller import avatar_bp

# Inicialização da aplicação Flask
app = Flask(__name__, template_folder="public/templates", static_folder="public/static")
app.config['SECRET_KEY'] = 'uma_chave_secreta_segura'

# -------------------------------------------------------
# Registro dos Blueprints
# -------------------------------------------------------
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chatbot_bp, url_prefix="/chatbot")
app.register_blueprint(avatar_bp, url_prefix="/avatar")

# -------------------------------------------------------
# Rotas principais
# -------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

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
    usuario_id = session.get("usuario_id")

    # busca avatar no banco
    avatar = None
    if usuario_id:
        from model import usuario_model
        resultado = usuario_model.buscar_avatar(usuario_id)

        if isinstance(resultado, dict):
            avatar = resultado.get("avatar")
        else:
            avatar = resultado

    if not avatar:
        avatar = "avatar_padrao.png"

    print("Avatar final enviado pro template:", avatar)
    return render_template("PaginaConfig.html", usuario_avatar=avatar)

@app.route("/classes")
def classes():
    return render_template("PaginaEscolhaClasse.html")

@app.route("/video")
def video():
    return render_template("PaginaClassVideo.html")

# -------------------------------------------------------
# Exercícios
# -------------------------------------------------------
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

# -------------------------------------------------------
# Jogos
# -------------------------------------------------------
@app.route("/jogo-memoria")
@login_required
def jogo_memoria():
    return render_template("PaginaJogoMemoria.html")

@app.route("/jogo-formar-frase")
@login_required
def jogo_formar_frase():
    return render_template("PaginaJogoFormarFrase.html")

@app.route("/jogo-vocabulario")
@login_required
def jogo_vocabulario():
    return render_template("PaginaJogoVocabulario.html")

# -------------------------------------------------------
# Páginas de escolha
# -------------------------------------------------------
@app.route("/activities")
@login_required
def activities():
    return render_template("PaginaEscolhaAtividades.html")  

@app.route("/games")
@login_required
def games():
    return render_template("PaginaEscolhaGames.html") 

# -------------------------------------------------------
# Execução local
# -------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
