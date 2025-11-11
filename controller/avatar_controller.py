from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from model import usuario_model
from controller.auth_controller import login_required  # importa o decorador do teu auth_bp

avatar_bp = Blueprint('avatar', __name__)

@avatar_bp.route('/perfil')
def perfil():
    usuario_id = session["usuario_id"]
    avatar = usuario_model.buscar_avatar(usuario_id)
    if not avatar:
        avatar = "avatar_padrao.png"
    return render_template("PaginaConfig.html", usuario_avatar=avatar)

@avatar_bp.route('/avatar', methods=['GET', 'POST'])
def atualizar_avatar():
    usuario_id = session["usuario_id"]

    if request.method == 'POST':
        avatar = request.form['avatar']
        usuario_model.atualizar_avatar(usuario_id, avatar)
        flash("Avatar atualizado com sucesso!")
        return redirect(url_for("avatar.perfil"))

    return render_template("PaginaConfig.html")
