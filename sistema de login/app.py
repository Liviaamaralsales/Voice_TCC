import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, session

from controller.auth_controller import auth_bp

from flask import Flask, render_template, request, redirect, url_for, flash, session

from model import usuario_model  # importa o módulo usuario_model para manipular o banco de dados de ususuarios

from werkzeug.security import generate_password_hash, check_password_hash

#Adiciona a raiz do projeto ao path ANTES dos imports locais

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.auth_controller import auth_bp
app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_longa_e_aleatoria_para_producao_1234567890'
app.secret_key = 'chave_secreta_segura' 
app.register_blueprint(auth_bp) #register the routes with blueprints, example: auth.example, and he integrate with auth_controler, for not have  problems with route, others = entre outros or outros.



@app.route("/")
def index():
    
    return render_template("PaginaLogin/PaginaLogin.html") # here he return paginalogin because its route first

if __name__ == '__main__':
    app.run(debug=True)