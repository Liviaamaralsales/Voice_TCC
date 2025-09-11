import sys
import os
from flask import Flask, render_template
from controller.auth_controller import auth_bp

# Adiciona a raiz do projeto ao path (só precisa uma vez)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

# Chave secreta (use sempre config)
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_longa_e_aleatoria_para_producao_1234567890'

# Registra o blueprint de autenticação
app.register_blueprint(auth_bp)

# Rota inicial -> redireciona para login (mais semântico)
@app.route("/")
def index():
    return render_template("PaginaLogin/PaginaLogin.html")

if __name__ == "__main__":
    app.run(debug=True)
