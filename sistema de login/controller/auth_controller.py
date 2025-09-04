from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from model import usuario_model
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# ROTA DE CADASTRO
@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        email = request.form["email"]
        rm = request.form["rm"]
        senha = request.form["senha"]
        confirmarSenha = request.form["confirmarSenha"]

        # Validações
        if confirmarSenha != senha:
            flash("Erro: senha e confirmação não conferem")
            return redirect(url_for("auth.cadastro"))

        if len(email) < 10 or len(email) > 40:
            flash("Email deve ter entre 10 e 40 caracteres.")
            return redirect(url_for("auth.cadastro"))

        if len(rm) != 5:
            flash("RM deve ter exatamente 5 caracteres.")
            return redirect(url_for("auth.cadastro"))

        if len(senha) < 8 or len(senha) > 50:
            flash("Senha deve ter entre 8 e 50 caracteres.")
            return redirect(url_for("auth.cadastro"))

        if usuario_model.buscar_usuario_por_email(email):
            flash("Usuário já cadastrado.")
            return redirect(url_for("auth.cadastro"))

        # Cadastro
        senha_hash = generate_password_hash(senha)
        usuario_model.cadastrar(rm, email, senha_hash)

        flash("Usuário cadastrado com sucesso!")
        return redirect(url_for("auth.login"))  # Vai para a tela de login

    return render_template("PaginaCadastro/PaginaCadastro.html")


# ROTA DE LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = usuario_model.buscar_usuario_por_email(email)
        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario"] = usuario["email"]
            flash("Login realizado com sucesso!")
            # Redireciona para uma rota após login, por exemplo dashboard
            return redirect(url_for("main.dashboard"))  
        else:
            flash("E-mail ou senha inválidos")
            return redirect(url_for("auth.login"))

    return render_template("PaginaLogin/PaginaLogin.html")


# ROTA DE LOGOUT (opcional)
@auth_bp.route('/logout')
def logout():
    session.pop("usuario", None)
    flash("Você saiu da conta.")
    return redirect(url_for("auth.login"))
