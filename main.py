import mysql.connector

myBD = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lojaPython"
)

cursor = myBD.cursor()
cursor.execute('USE lojaPython')


def cadastrarCliente():
    while True:
        print('\n==============================')
        print('{:^30}'.format('CADASTRANDO UM NOVO CLIENTE'))
        print('=' * 30)

        p_nome = str(input('Primeiro Nome: ')).capitalize()
        while len(p_nome) >= 255 or len(p_nome) <= 0:
            print('Erro: Dado Inválido!')
            p_nome = str(input('Primeiro Nome: ')).capitalize()

        u_nome = str(input('Último Nome: ')).capitalize()
        while len(u_nome) >= 255 or len(u_nome) <= 0:
            print('Erro: Dado inválido!')
            u_nome = str(input('Último Nome: ')).capitalize()

        while True:
            try:
                idade = int(input('Idade: '))
                if idade >= 100 or idade <= 0:
                    raise ValueError()
            except ValueError:
                print('Erro: Tipo de Dado Inválido')
            else:
                break

        sexo = str(input('Sexo: ')).upper()
        while len(sexo) > 2 or len(sexo) <= 0 or sexo != 'M' and sexo != 'F':
            print('Erro: Dado Inválido')
            sexo = str(input('Sexo: ')).upper()

        endereco = str(input('Endereço: ')).capitalize()
        while len(endereco) > 255 or len(endereco) <= 0:
            print('Erro: Dado Inválido')
            endereco = str(input('Endereço: ')).capitalize()

        cidade = str(input('Cidade: ')).capitalize()
        while len(cidade) > 255 or len(cidade) <= 0:
            print('Erro: Dado Inválido')
            cidade = str(input('Cidade: ')).capitalize()

        estado = str(input('Estado (Sigla): ')).upper()
        while len(estado) > 2 or len(estado) <= 0:
            print('Erro: Dado Inválido')
            estado = str(input('Estado (Sigla): ')).upper()

        while True:
            try:
                avaliacao = int(input('Avaliação da Loja (0 á 5): '))
                if avaliacao > 5 or avaliacao < 0:
                    raise ValueError()
            except ValueError:
                print('Erro: Tipo de Dado Inválido')
            else:
                break

        cursor.execute(
            "INSERT INTO Cliente VALUES (DEFAULT, '{}', '{}', {}, '{}', '{}', '{}', '{}', {})".format(p_nome, u_nome,
                                                                                                      idade, sexo,
                                                                                                      endereco, cidade,
                                                                                                      estado,
                                                                                                      avaliacao))
        break


def buscarCliente():
    print('\n==============================')
    print('{:^29}'.format('BUSCANDO UM CLIENTE'))
    print('=' * 30)

    busca_pNome = str(input('Primeiro Nome: '))
    busca_uNome = str(input('Último Nome: '))

    cursor.execute("""SELECT * FROM Cliente
                   WHERE Primeiro_Nome = '{}' AND Ultimo_Nome = '{}' """.format(busca_pNome, busca_uNome))

    select = cursor.fetchall()

    for x in select:
        print(x)


def consultarCliente():
    print('\n==============================')
    print('{:^30}'.format('CONSULTANDO TODOS OS CLIENTES'))
    print('=' * 30)

    cursor.execute("SELECT * FROM Cliente")

    select = cursor.fetchall()

    for x in select:
        print(x)

    print('\n')


while True:
    print('=' * 30)
    print('{:^28}'.format('MENU'))
    print('=' * 30)
    print('''1) Cadastrar Novo Cliente
2) Buscar Cliente(s) Expecífico(s)
3) Consultar Clientes
4) Sair''')
    print('==============================')
    escolha = str(input('Digite sua opção: '))
    print('==============================')
    if escolha == '1':
        cadastrarCliente()
    elif escolha == '2':
        buscarCliente()
    elif escolha == '3':
        consultarCliente()
    elif escolha == '4':
        break
