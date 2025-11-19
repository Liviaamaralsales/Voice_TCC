from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from model import usuario_model
from functools import wraps

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        data_nascimento = request.form["dataNascimento"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmarSenha = request.form["confirmarSenha"]

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

        senha_hash = generate_password_hash(senha)
        usuario_model.cadastrar(nome, data_nascimento, email, senha_hash)
        flash("Usuário cadastrado com sucesso!")
        return redirect(url_for("auth.login"))

    return render_template("index.html")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        usuario = usuario_model.buscar_usuario_por_email(email)

        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario"] = usuario["email"]
            flash("Login realizado com sucesso!")
            return redirect(url_for("home"))
        else:
            flash("E-mail ou senha inválidos")
            return redirect(url_for("auth.login"))

    return render_template("index.html")

@auth_bp.route("/excluir_conta", methods=["POST"])
def excluir_conta():
    if "usuario_id" not in session:
        return jsonify({'success': False, 'message': 'Você precisa estar logado para excluir sua conta.'}), 401

    data = request.get_json()
    senha = data.get('password')

    user_id = session["usuario_id"]
    usuario = usuario_model.buscar_usuario_por_id(user_id)

    if not usuario:
        return jsonify({'success': False, 'message': 'Usuário não encontrado.'}), 404

    if not check_password_hash(usuario["senha"], senha):
        return jsonify({'success': False, 'message': 'Senha incorreta.'}), 403

    sucesso = usuario_model.excluir_usuario(user_id)
    if sucesso:
        session.clear()
        return jsonify({'success': True, 'message': 'Conta excluída com sucesso.'})
    else:
        return jsonify({'success': False, 'message': 'Erro ao excluir a conta.'}), 500

@auth_bp.route('/logout')
def logout():
    session.pop("usuario", None)
    flash("Você saiu da conta.")
    return redirect(url_for("auth.login"))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario" not in session:
            flash("Você precisa estar logado para acessar esta página.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route("/redefinir", methods=["POST"])
def redefinir():
    email = request.form.get("email")
    nova_senha = request.form.get("senha")

    usuario = usuario_model.buscar_usuario_por_email(email)
    if not usuario:
        flash("E-mail não encontrado.")
        return redirect(url_for("configuracoes"))

    nova_senha_hash = generate_password_hash(nova_senha)
    usuario_model.atualizar_senha(usuario["id"], nova_senha_hash)
    flash("Senha redefinida com sucesso! Faça login.")
    return redirect(url_for("auth.login"))
