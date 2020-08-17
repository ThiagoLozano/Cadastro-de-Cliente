# Biblioteca.
import mysql.connector


# Cria a Classe EntrarNoBanco
class EntrarNoBanco:
    def __init__(self):
        # Cria a conexão com o BD.
        self.myBD = mysql.connector.connect(host="localhost", user="root", password="", database="lojaPython")

        # Cria um Cursor.
        self.cursor = self.myBD.cursor()
        self.cursor.execute('USE lojaPython')

    def CadastrarNovoCliente(self):
        while True:
            print('\n==============================')
            print('{:^30}'.format('CADASTRANDO UM NOVO CLIENTE'))
            print('=' * 30)

            # Primeiro Nome.
            p_nome = str(input('Primeiro Nome: ')).capitalize()

            # Valida o Nome.
            while len(p_nome) >= 255 or len(p_nome) <= 0:
                print('\033[31mErro: Dado Inválido!\033[m')
                p_nome = str(input('Primeiro Nome: ')).capitalize()

            # Último Nome.
            u_nome = str(input('Último Nome: ')).capitalize()

            # Valida o último nome.
            while len(u_nome) >= 255 or len(u_nome) <= 0:
                print('\033[31mErro: Dado inválido!\033[m')
                u_nome = str(input('Último Nome: ')).capitalize()

            # Idade.
            while True:
                try:
                    idade = int(input('Idade: '))
                    if idade >= 100 or idade <= 0:
                        raise ValueError()
                except ValueError:
                    print('\033[31mErro: Tipo de Dado Inválido\033[m')
                else:
                    break

            # Sexo.
            sexo = str(input('Sexo(M/F): ')).upper()

            # Valida o Sexo.
            while len(sexo) > 2 or len(sexo) <= 0 or sexo != 'M' and sexo != 'F':
                print('\033[31mErro: Dado Inválido\033[m')
                sexo = str(input('Sexo: ')).upper()

            # Endereço.
            endereco = str(input('Endereço: ')).capitalize()

            # Valida o Endereço.
            while len(endereco) > 255 or len(endereco) <= 0:
                print('\033[31mErro: Dado Inválido\033[m')
                endereco = str(input('Endereço: ')).capitalize()

            # Cidade
            cidade = str(input('Cidade: ')).capitalize()

            # Valida a cidade.
            while len(cidade) > 255 or len(cidade) <= 0:
                print('\033[31mErro: Dado Inválido\033[m')
                cidade = str(input('Cidade: ')).capitalize()

            # Estado.
            estado = str(input('Estado (Sigla): ')).upper()

            # Valida o Estado.
            while len(estado) > 2 or len(estado) <= 0:
                print('\033[31mErro: Dado Inválido\033[m')
                estado = str(input('Estado (Sigla): ')).upper()

            # Avaliação.
            while True:
                try:
                    avaliacao = int(input('Avaliação da Loja (0 á 5): '))
                    if avaliacao > 5 or avaliacao < 0:
                        raise ValueError()
                except ValueError:
                    print('\033[31mErro: Tipo de Dado Inválido\033[m')
                else:
                    break

            # Insere os valores dentro da Tabela
            self.cursor.execute(
                "INSERT INTO Cliente VALUES (DEFAULT, '{}', '{}', {}, '{}', '{}', '{}', '{}', {})".format(p_nome,
                                                                                                          u_nome,
                                                                                                          idade, sexo,
                                                                                                          endereco,
                                                                                                          cidade,
                                                                                                          estado,
                                                                                                          avaliacao))
            break

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

    def ListarClientes(self):
        print('\n==============================')
        print('{:^30}'.format('CONSULTANDO TODOS OS CLIENTES'))
        print('=' * 30)

        # Retorna todos os registros já inseridos na tabela.
        self.cursor.execute("SELECT * FROM Cliente")

        select = self.cursor.fetchall()

        print()
        for x in select:
            print(x)
        print()

    def Menu(self):
        while True:
            print('=' * 30)
            print('{:^28}'.format('MENU'))
            print('=' * 30)
            print('''1) Cadastrar Novo Cliente
2) Buscar Cliente
3) Lista de Clientes
4) Sair''')
            print('==============================')
            escolha = str(input('Digite sua opção: '))
            print('==============================')
            if escolha == '1':
                self.CadastrarNovoCliente()
            elif escolha == '2':
                self.BucarCliente()
            elif escolha == '3':
                self.ListarClientes()
            elif escolha == '4':
                break


usuario = EntrarNoBanco()
usuario.Menu()
