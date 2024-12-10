cadastros = {
    '000.000.000-00': ('Fulano', 'fulano@gmail.com', '01/01/1990'),
    '001.001.001-01': ('Ciclano', 'ciclano@gmail.com', '02/02/1992')
}

while True:
    print("Menu de Opções:")
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Remover")
    print("4 - Sair")
    print("5 - Listar todos os cadastros")
    opcao = input("Escolha uma opção: ")

    if opcao == "4":
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
    elif opcao == "5":
        if not cadastros:
            print("Nenhum cadastro encontrado.")
        else:

            for cpf, (nome, email, data_nascimento) in cadastros.items():
                print(f"CPF: {cpf}")
                print(f"Nome: {nome}")
                print(f"Email: {email}")
                print(f"Data de Nascimento: {data_nascimento}")
                print("----")
    else:
        print("Opção inválida! Tente novamente.")
