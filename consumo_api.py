# O módulo requests ele é utilizado para executar requsições ao serviços web
# O requests não vem disponível diretamente nas bibliotecas padrões do Python,
#   sendo assim é necessário que seja feita a instalação utilizando o regerenciador de
#   pacotes PIP.
#   > pip install requests
import requests

# Armazenar em uma variável o endereço completo da api
url = 'http://127.0.0.1:5000/api/produtos'

# Ententendo que a rota em questão utiliza um método GET, é necessário que o método .get
#   seja executado.
# O método get vai retornar uma requesição
retorno = requests.get( url )
print( retorno )

# O método .json ele caputra os dado que chegaram na API no forma de JSON, e converte em
#   uma estruta de coleções do Python
dados = retorno.json()
print( dados )