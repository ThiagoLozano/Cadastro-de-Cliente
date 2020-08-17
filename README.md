# PROJETO PYTHON: Cadastro do Cliente

> Um sistema simples de cadastro com conexão direta a um banco de Dados Local.

  Criar um Banco de Dados MySQL contendo os campos:
- ID;
- Primeiro_Nome ;
- Ultimo_Nome ;
- Idade;
- Sexo ;
- Endereço;
- Cidade ;
- Estado ;
- Avaliação.

O programa deve se conectar com o BD e fazer modificações dentro dele, através de opções que podem ser selecionadas
dentro de um menu, como:
- Cadastrar um novo Cliente;
- Buscar por um Cliente Específico;
- Consultar todos os Clientes.
O programa deve finalizar apenas quando o usuário não desejar mais fazer alterações.

# Tecnologias Utilizadas
* **_Python 3;_**
* **_MySQL;_**
* **_WampServer (para a conexão local do BD)._**


# Exemplo de Uso

### Classe:
```
class EntrarNoBanco:
    def __init__(self):
        # Cria a conexão com o BD.
        self.myBD = mysql.connector.connect(host="localhost", user="root", password="", database="lojaPython")

        # Cria um Cursor.
        self.cursor = self.myBD.cursor()
        self.cursor.execute('USE lojaPython')
```
![Conexão do BD](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/Classe.PNG)

### Função que busca Clientes no BD:
```
    def BucarCliente(self):
        print('\n==============================')
        print('{:^29}'.format('BUSCANDO UM CLIENTE'))
        print('=' * 30)

        # Pergunta para o usuário.
        busca_pNome = str(input('Primeiro Nome: '))
        busca_uNome = str(input('Último Nome: '))

        # Passa pela tabela procurando os valores inseridos.
        self.cursor.execute("""SELECT * FROM Cliente
                        WHERE Primeiro_Nome = '{}' AND Ultimo_Nome = '{}' """.format(busca_pNome, busca_uNome))

        select = self.cursor.fetchall()

        print()
        for x in select:
            print(x)
        print()
```
![Busca Cliente](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/Funcao.PNG)

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

> Como o BD não foi criado dentro do Python é necessário que a parte do _CREATE DATABASE_ seja executado primero no
MySQL, o resto é por conta do código.

# Bibliotecas e Configurações

### Biblioteca Python Utilizada.

```
import mysql.connector
```
![Biblioteca](https://github.com/ThiagoLozano/Cadastro-de-Cliente/blob/master/Screenshot/Biblioteca.PNG)

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
