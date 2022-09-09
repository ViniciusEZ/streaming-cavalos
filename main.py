from database_user.user import iscpfvalid, collect_info
from database_user.db import connect, select, insert_sql

con = connect('streaming.db')

baseurl = 'https://viacep.com.br/ws/'
endpoint = '/json/'
options = ['login', 'sign up']
user_infos = ['Usuario', 'Nome', 'Sobrenome', 'Idade', 'Cpf', 'Cep']
list_info = []
movies = ['A espera de um milagre', 'De Volta Ao Futuro', 'Click', 'LOGOUT']


print('STREAMING CAVALOS')
while True:
    for index, option in enumerate(options):
        print(f'{index+1} - {option}')

    user = input('Escolha uma opção: ')
    if user == '1':
        for data in user_infos:
            if data == 'cpf':
                user_data = input(f'{data}: ')
                while iscpfvalid(user_data):
                    user_data = input('CPF inválido. Digite novamente: ')
            else:
                user_data = input(f'{data}: ')
                if data == 'cep':
                    while not collect_info(baseurl, endpoint, user_data):
                        user_data = input('CEP inválido. Digite Novamente: ')

            list_info.append(user_data)
        cep_info = collect_info(baseurl, endpoint, user_data)

        for info in cep_info.values():
            list_info.append(info)
            print(info)

        confirmation = input('As informações estão corretas? [Y/n]')
        if confirmation == 'Y':
            final_info = input('Número da casa: ')
            list_info.append(final_info)
            final_info = input('Senha: ')
            list_info.append(final_info)
            insert_sql(con, list_info)

    if user == '2':
        username = input("Digite o seu usuário: ")
        password = input("Digite a sua senha: ")
        while not select(con, username, password):
            print('Usuário ou senha incorretos. Digite novamente.')
            username = input("Digite o seu usuário: ")
            password = input("Digite a sua senha: ")
        print()
        print("Bem-vindo ao Streaming Cavalos, aqui está o nosso catálogo de filmes...")
        for index, opt in enumerate(movies):
            print(f'{index+1} - {opt}')
        user_option = input("Escolha uma opção: ")
        if user_option == '4':
            print()
            print('Volte sempre!')
            break

con.close()















