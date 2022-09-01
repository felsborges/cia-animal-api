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
    #   este caminho é informado através de um texto, infornando o nome do arquivo
    con = sqlite3.connect('cia-animal.db')

    # Por padrão o retorno dos dados é uma lista de tuplas, mas se desejamos uma lista
    #   de dicionário o sqlite3 possuiu uma configuração na conexão para que esse retorno
    #   seja feito
    # con.row_factory = sqlite3.Row

    # Após a conexão é necessário estabeler um caminho de comunicação
    #   este caminho será chamdo de cursor, nele poderemos enviar comandos ao banco.
    # Os comando do banco de dados utilizaram a liguagem SQL
    cur = con.cursor()

    # Como boa prática, é interessante criar uma variável texto contendo a instrução SQL
    sql = 'SELECT nome FROM produtos'

    # A variável texto criada no passo anterior é passada por parâmetro para o método 
    #   execute é simplesmente executa o comando SQL
    cur.execute( sql )

    # Para os casos de comandos SELECT, o banco de dados deixa disponível o resultado,
    #   no entanto, este resultado deve ser coletado através do comando
    #   de bucar tudo (fetchall), e após será armazenado em uma variável qualquer.
    dados = cur.fetchall()

    # Quando não é mais necessário a utilização do banco de dados, é importante que ele
    #   seja encerrado através do comando close
    con.close()

    # Para que esta função retorne uma API é necessário que seja retornado um tipo de coleção
    #   podendo ser uma lista ou um dicionário
    return dados