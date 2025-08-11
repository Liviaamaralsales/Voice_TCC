from flask import Blueprint, render_template, request, redirect, url_for, flash, session 
from model import usuario_model
from werkzeug.security import generate_password_hash, check_password_hash


auth_bp = Blueprint('auth', __name__) # começa a definir o blueprint para autenticação

@auth_bp.route('/cadastro', methods=['GET', 'POST'])  # define nessa linha a rota de cadastro, que vai pegar as informações do usuário e postar no form
def cadastro():
    if request.method == "POST":
        email = request.form["email"]
        rm = request.form["rm"]
        senha = request.form["senha"]  # pega os dados do formulário de cadastro para verificar
        confirmarSenha = request.form["confirmarSenha"]  # pega a confirmação de senha do formulário
        
        if confirmarSenha != senha:  # verifica se a confirmação de senha é igual à senha
            flash("Erro, coloque a senha igual ")  # se não for igual, retorna erro

        
        if len (email ) < 10 or len (email) > 40:
            return jsonify({"erro": "Email deve ter entre 10 e 40 caracteres."})  # verifica se o email, rm e senha estão dentro dos limites de caracteres
        
            
        if len (rm) < 5 or len (rm) > 5:
            return jsonify({"erro": "RM deve ter exatamente 5 caracteres."})
        
        if len (senha) < 8 or len (senha) > 50:
            return jsonify({"erro": "Senha deve ter entre 8 e 50 caracteres."})
        
        # verifica se a senha e a confirmação de senha são iguais

        if usuario_model.buscar_usuario_por_email( email):
            print("Usuário já cadastrado com esse RM ou e-mail.")
            return redirect(url_for("auth.cadastro"))  # se o usuário já estiver cadastrado, redireciona para a página de login
        
        senha_hash = generate_password_hash(senha)
        usuario_model.cadastrar(rm, email, senha_hash) # chama a função cadastrar do model.usuario_model, que vai inserir os dados no banco de dados
        
        print("Usuário cadastrado com sucesso!") # se o usuário for cadastrado com sucesso, retorna essa mensagem
        return redirect(url_for("auth.cadastro"))  # redireciona para a página de login após o cadastro
        
        
    return render_template("PaginaCadastro/PaginaCadastro.html") # aqui rennderiza a página de cadastro, que é a PaginaLogin.html ( Ambas estão juntas no template)