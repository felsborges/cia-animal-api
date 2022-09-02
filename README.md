# API da Cia do Animal

Para que possamos criar uma API é necessário criar o ambiente virutal (venv), com o seguinte comando:

    python -m venv venv

Após é necessário a ativação do venv utilizando o seguinte comando:
LEMBRE: o venv muitas vezes não está ativo logo que inicia o terminal, o comando de ativação é necessário toda a vez que forem executar uma aplicação.

    venv\Scripts\activate

Com o ambiente virual devidamente ativado é necessário instalar o flask, utilizando o gerenciador de pacotes chamado de PIP. Segue o comando para a instalação:

    pip install flask

O projeto desenvolvido utiliza o módulo 'requests' que não está presente nos módulos padrões disponíveis no Python, com isso é necesário que seja feita a instalação.

    pip install requests

## Execução

- O motor do flask deve ser executado em um termial independe \
Para executar a aplicação flask é necessário executar o seguinte comando:

    set FLASK_APP=cia_animal_api
    flask --debug run

NOTE: o comando de definição do módulo é executado somente uma vez no ambiente, sendo assim para seguir na execucação basta executa o comando flask run.
A sugestão é utilizar o parâmetro --debug para facilitar a identificação de erros no desenvolvimento.

- A aplicação de consumo da API deve ser executada de maneira indepente, ou seja, em um outro terminal

    python -m consumo_api

