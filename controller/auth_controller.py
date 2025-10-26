
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from model import usuario_model


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        data_nascimento = request.form["dataNascimento"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmarSenha = request.form["confirmarSenha"]

        # --- Validações ---
        if confirmarSenha != senha:
            flash("Erro: senha e confirmação não conferem")
            return redirect(url_for("auth.cadastro"))

        if len(nome) < 3 or len(nome) > 100:
            flash("Nome deve ter entre 3 e 100 caracteres.")
            return redirect(url_for("auth.cadastro"))

        if len(email) < 10 or len(email) > 100:
            flash("Email deve ter entre 10 e 100 caracteres.")
            return redirect(url_for("auth.cadastro"))

        if len(senha) < 8 or len(senha) > 50:
            flash("Senha deve ter entre 8 e 50 caracteres.")
            return redirect(url_for("auth.cadastro"))

        if usuario_model.buscar_usuario_por_email(email):
            flash("Usuário já cadastrado com este e-mail.")
            return redirect(url_for("auth.cadastro"))

        # --- Cadastro ---
        senha_hash = generate_password_hash(senha)
        usuario_model.cadastrar(nome, data_nascimento, email, senha_hash)

        flash("Usuário cadastrado com sucesso!")
        return redirect(url_for("auth.login"))

    return render_template("PaginaTelaLogin.html")

# ROTA DE LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = usuario_model.buscar_usuario_por_email(email)

        # Ajuste dependendo de como o model retorna os dados
        if usuario and check_password_hash(usuario["senha"], senha):  
            session["usuario"] = usuario["email"]
            flash("Login realizado com sucesso!")
            return redirect(url_for("home"))  # redireciona para home
        else:
            flash("E-mail ou senha inválidos")
            return redirect(url_for("auth.login"))

    return render_template("PaginaTelaLogin.html")


# ROTA DE LOGOUT
@auth_bp.route('/logout')
def logout():
    session.pop("usuario", None)
    flash("Você saiu da conta.")
    return redirect(url_for("auth.login"))

