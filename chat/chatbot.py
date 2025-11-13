from flask import Flask, Blueprint, render_template, request
import google.generativeai as genai
import urllib.parse
import requests

# Cria o blueprint
chatbot_bp = Blueprint('chatbot', __name__, template_folder='../public/templates')

# Configuração da chave da API
genai.configure(api_key="AIzaSyAlPlQTdYzuJoRsqLZb5ec1dEAH0i2ABA0")

# Inicializa o modelo Gemini 2.5 Flash
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Função de tradução com API gratuita Lingva
def traduzir_lingva(texto, source_lang, target_lang):
    texto_escapado = urllib.parse.quote(texto)
    url = f"https://lingva.ml/api/v1/{source_lang}/{target_lang}/{texto_escapado}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        resultado = response.json()
        return resultado.get("translation", "Erro: resposta sem tradução")
    except Exception as e:
        return f"Erro: {e}"

# Mapeia idioma por nome
def mapear_idioma(nome):
    nome = nome.lower()
    if nome in ['ingles', 'english', 'en']:
        return 'en'
    elif nome in ['portugues', 'português', 'pt']:
        return 'pt'
    else:
        return None

# Função principal do chatbot
def responder_como_chatbot(mensagem):
    mensagem = mensagem.lower().strip()

    if mensagem.startswith("me traduza"):
        partes = mensagem.split("para")
        if len(partes) == 2:
            texto = partes[0].replace("me traduza", "").strip()
            destino = partes[1].strip()
            idioma_destino = mapear_idioma(destino)
            if idioma_destino:
                idioma_origem = 'pt' if idioma_destino == 'en' else 'en'
                return traduzir_lingva(texto, idioma_origem, idioma_destino)
            else:
                return "Idioma de destino não reconhecido."
        else:
            return "Formato inválido. Tente: me traduza [texto] para [idioma]"

    elif any(p in mensagem for p in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
        return "Olá! Como posso te ajudar hoje?"

    elif "como você está" in mensagem or "tudo bem" in mensagem:
        return "Estou ótimo, obrigado por perguntar! E você?"

    elif "qual seu nome" in mensagem:
        return "Eu sou um chatbot com inteligência Gemini, criado para te ajudar!"

    elif "obrigado" in mensagem or "obrigada" in mensagem:
        return "De nada! Sempre que precisar, estou aqui."

    elif "tchau" in mensagem or "até logo" in mensagem:
        return "Tchau! Até a próxima!"

    return resposta_gemini(mensagem)

# Chamada ao modelo Gemini 2.5 Flash
def resposta_gemini(pergunta):
    try:
        resposta = model.generate_content(pergunta)
        return resposta.text
    except Exception as e:
        return f"Erro com Gemini: {e}"

# Rota principal
@chatbot_bp.route('/', methods=['GET', 'POST'])
def chat():
    texto_usuario = None
    resposta_bot = None

    if request.method == 'POST':
        texto_usuario = request.form['texto']
        resposta_bot = responder_como_chatbot(texto_usuario)

    return render_template('PaginaChatbot.html', texto_usuario=texto_usuario, traducao=resposta_bot)
