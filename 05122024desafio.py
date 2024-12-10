'''Faça um programa de cadastramento de pessoas com os seguintes requisitos:

1 - O programa mostra um menu de opções em loop. As opções são:
    1 - Cadastrar
    2 - Buscar
    3 - Remover
2 - Na opção Cadastrar, o usuário insere um CPF no formato XXX.XXX.XXX-XX,
    um nome, um email e uma data de nascimento no formato DIA/MES/ANO, e
    estes dados são cadastrados.
3 - Na opção Buscar, o usuário insere um CPF de um cadastro e o programa
    mostra os dados da pessoa com esse CPF (nome, email e data de nascimento).
3 - Na opção Remover, o usuário insere um CPF de um cadastro e o programa
    deleta esse cadastro.

Utilize um dicionário de tuplas para registrar os cadastros.'''
cadastros = {}

while True:
    print("Menu de Opções:")
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Remover")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa...")
        break
    elif opcao == "1":
        cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
        if not cpf or len(cpf) != 14 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
            print("CPF inválido. Tente novamente.")
            continue
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        data_nascimento = input("Digite a data de nascimento (DIA/MES/ANO): ")
        cadastros[cpf] = (nome, email, data_nascimento)
        print("Cadastro realizado com sucesso!")
    elif opcao == "2":
        cpf = input("Digite o CPF para busca: ")
        if cpf in cadastros:
            nome, email, data_nascimento = cadastros[cpf]
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Data de Nascimento: {data_nascimento}")
        else:
            print("Cadastro não encontrado.")
    elif opcao == "3":
        cpf = input("Digite o CPF para remover: ")
        if cpf in cadastros:
            del cadastros[cpf]
            print("Cadastro removido com sucesso!")
        else:
            print("Cadastro não encontrado.")
    else:
        print("Opção inválida! Tente novamente.")
