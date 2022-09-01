# Importar o flask que foi instalado dentro do venv
from flask import Flask

# Criar a apliação (motor) para a execução da aplicação web
app = Flask(__name__)

# Para esta dinâmica iremos criar a rota /api/produtos para listar os produtos
# LEMBRE: a rota é definida dentro da variável da aplição
@app.route('/api/produtos')
# A função produtos por estar definida logo após a rota é considera uma função para visões (view function)
def produtos(): # View Function
    dic = {
        'Chave1': 'Valor de teste'
    }
    return dic