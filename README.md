# PROJETO PYTHON: Cadastro do Cliente

> Um sistema simples de cadastro com conexão direta a um banco de Dados Local.

  O projeto tem como objetivo, cadastrar um Cliente com seus dados pessoais dentro de um menu interativo
usando o próprio Python Console.
    Esses dados são armazenados em um Banco de Dados, assim, ao reiniciar o Console os dados não são perdidos ou
apagados.
    O sistema foi criado para o estudo da linguagem Python, usando um caso de entrada, saída e armazenamento de dados
junto a Linguagem SLQ.

# Tecnologias Utilizadas
* **_Python 3;_**
* **_MySQL;_**
* **_WampServer (para a conexão local do BD)._**


# Exemplo de Uso

### Criação do BD:
```
CREATE DATABASE IF NOT EXISTS LojaPython;
USE LojaPython;
```
![Criação do BD](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/CriaBD.PNG)

### Criação da Tabela:
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
![Criação da Tabela](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/TabelaBD.PNG)

> Como o BD não foi criado dentro do Python é necessário que a parte do _CREATE DATABASE_ seja executado primero no MySQL, o resto é por conta do código.

# Bibliotecas e Configurações

### Biblioteca Python Utilizada.

```
import mysql.connector
```
![Biblioteca](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/Import.PNG)

### Configuração do Python para se conectar com o MySQL.
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
![Configuração](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/Conexao.PNG)

# Menu do Console
* Foi criado um menu simples de interação com o usuário, apenas para simular um cadastro de forma intuitiva.
* Uma parte importante do código é a validação dos dados que o usuário digitar para que não haja nenhum tipo de conflito com o BD.

### Opções do menu
* Cadastrar um Cliente Novo;
* Buscar Cliente(s) Expecífico(s);
* Consultar Clientes já Cadastrados;
* Sair do Menu.
