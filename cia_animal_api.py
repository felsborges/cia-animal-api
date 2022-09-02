# Importar o flask que foi instalado dentro do venv
from flask import (
    Flask,
    # O módulo jsonify é utilizado para converter uma coleção qualquer em
    #   um documento no formato json
    jsonify
)

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

# Denição da rota através do decorador .route
# A rota que foi criada está utilização o formato dinâmico de definições rota.
# A parte dinâmica da rota é identifica pelos símbolos < e >
# NOTE: As rotas não tem relações entre si
@app.route('/api/produtos/<produto_nome>')
# O parâmetro utilizado na função é o mesmo nome utilizado na parte dinâmica da rota
def produto_detalhes(produto_nome): # View function (Funão de visão)
    # Conexão com banco de dados
    con = sqlite3.connect('cia-animal.db')

    # Criação do cursor
    cur = con.cursor()

    # A variável SQL é uma instrução de banco de dados, que é representada com um texto no
    #   Python, sendo assim não existe uma validação pelo Python, a validação só acontece
    #   no momento que a consulta é enviada para o banco de dados utilizando o cursor que
    #   no código em questão é representado pela variável 'cur'
    # Para simplicar a codificação do SQL é interessante utilizar as aspas duplas como
    #   simbolos para definir textos
    # Uma forma de aplicar um filtro dinâmico na consulta que será enviada, é a utilização
    #   de alguma forma de interpolação
    sql = f"SELECT nome, descricao, valor FROM produtos WHERE nome = '{produto_nome}'"

    # Executar a consulta utilizando o cursor
    cur.execute( sql )

    # Para caso de consulta que retornam somente um registro,
    #   o uso do fetchone (busca um registro) é o método mais indicado para este tipo ação
    # NOTE: o fetchone retorma somente uma tupla, quando o fetchall
    #   retorna uma lista de tuplas
    dados = cur.fetchone()

    # Fechar a conexão
    con.close()

    # Toda função de visão deve ter um retorno
    # No caso que a informação armazenda na variável 'dados' é uma tupla, se faz necessário
    #   a utilização do jsonify
    return jsonify(dados)
