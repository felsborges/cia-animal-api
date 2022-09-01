# Importar o flask que foi instalado dentro do venv
from flask import Flask

# Para que seja possivel conectar-se a um banco de dados é necessário utilizar o DBI
# Neste caso utilizaremos o SGBD SQLite, sendo assim devemos importa o módulo sqlite3
import sqlite3

# Criar a apliação (motor) para a execução da aplicação web
app = Flask(__name__)

# Para esta dinâmica iremos criar a rota /api/produtos para listar os produtos
# LEMBRE: a rota é definida dentro da variável da aplição
@app.route('/api/produtos')
# A função produtos por estar definida logo após a rota é considera
#   uma função para visões (view function)
def produtos(): # View Function
    # O primeiro passo para o uso do banco de dados é a conexão
    # Para estabelecer uma conexão é que seja informado o caminho da conexão
    #   este caminho é informado através de um texto
    con = sqlite3.connect('cia-animal.db')

    dic = {
        'Chave1': 'Valor de teste'
    }

    # Para que esta função retorne uma API é necessário que seja retornado um tipo de coleção
    #   podendo ser uma lista ou um dicionário
    return dic