'''
Faça um programa de cadastramento de pessoas com os seguintes requisitos:

1 - O programa mostra um menu de opções em loop. As opções são:
    1 - Cadastrar
    2 - Buscar
    3 - Remover
    4 - Listar
2 - Na opção Cadastrar, o usuário insere um CPF no formato XXX.XXX.XXX-XX,
    um nome, um email e uma data de nascimento no formato DIA/MES/ANO, e
    estes dados são cadastrados.
3 - Na opção Buscar, o usuário insere um CPF de um cadastro e o programa
    mostra os dados da pessoa com esse CPF (nome, email e data de nascimento).
4 - Na opção Remover, o usuário insere um CPF de um cadastro e o programa
    deleta esse cadastro.
5 - Na opção Listar, o programa deve mostrar uma lista de cadastros.

Utilize um dicionário de tuplas para registrar os cadastros.
'''

cadastros = dict()

while True:
    print('1 - Cadastrar')
    print('2 - Buscar')
    print('3 - Remover')
    op = input('Opção: ')
    if op == '1':
        cpf = input('CPF: ')
        nome = input('Nome: ')
        email = input('Email: ')
        nascimento = input('Data de nascimento: ')
        cadastros[cpf] = (nome, email, nascimento) # Adiciona o cadastro ao dicionário
    elif op == '2':
        cpf = input('CPF: ')
        if cpf in cadastros.keys():    
            dados = cadastros[cpf] # Busca o cadastro no dicionário
            nome, email, nascimento = dados # Separa os dados da tupla obtida
            print(nome, email, nascimento)
        else:
            print('CPF não cadastrado')
    elif op == '3':
        cpf = input('CPF: ')
        if cpf in cadastros.keys():
            del cadastros[cpf] # Remover a cadastro do dicionário
        else:
            print('CPF não cadastrado')
    else:
        print('Opção inválida!')

