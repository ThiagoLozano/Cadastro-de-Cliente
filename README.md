# PROJETO PYTHON: Cadastra Cliente

> Um sistema simples de cadastro com conexão direta a um banco de Dados Local.

   O projeto tem como objetivo, cadastrar um Cliente(usuário) com seus dados pessoais dentro de um menu interativo
usando o próprio Python Console.
    Esses dados são armazenados em um Banco de Dados, assim, ao reiniciar o Console os dados não são perdidos ou
apagados.
    O sistema foi criado para o estudo da linguagem Python, usando um caso de entrada, saída e armazenamento de dados
junto a Linhagem SLQ.

# Tecnologias Utilizadas
> Python 3

> MySQL

# Exemplo de Uso

Criação do BD:
```
CREATE DATABASE LojaPython
USE LojaPython
```

Criação da Tabela:
```
CREATE TABLE IF NOT EXISTS Cliente(
ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
Primeiro_Nome VARCHAR(255) NOT NULL,
Ultimo_Nome VARCHAR(255) NOT NULL,
Idade INT NOT NULL,
Sexo CHAR(1) NOT NULL,
Endereco VARCHAR(255) NOT NULL,
Cidade VARCHAR(255) NOT NULL,
Estado CHAR(2) NOT NULL,
Avaliacao INT NOT NULL);
```

# Bibliotecas e Configurações

Biblioteca Python Utilizada.

```
import mysql.connect
```

Configuração do Python para se conectar com o MySQL.
```
myBD = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LojaPython"
)

cursor = myBD.cursor()
cursor.execute('USE lojaPython')
```
