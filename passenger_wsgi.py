import sys, os

# Caminho absoluto do projeto
project_path = os.path.dirname(os.path.abspath(__file__))

# Adiciona a raiz do projeto ao sys.path
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Adiciona subpastas necessárias
sys.path.append(os.path.join(project_path, "controller"))
sys.path.append(os.path.join(project_path, "chat"))
sys.path.append(os.path.join(project_path, "model"))

# Importa a aplicação Flask
from app import app as application
