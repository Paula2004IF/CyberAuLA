'''FAÇA UM PROGRAMA DE BANCO DE SANGUE.
LEIA E IMPRIMA AS OPÇÕES:
1-CADASTRAR DOAÇÃO 
2-OBTER BOLSA DE SANGUE
3-LISTAR BOLSAS DISPONÍVEIS



OPÇAO 1: INSERIR OS DADOS DE UMA DOAÇÃO JÁ REALIZADA: 
TIPO SAGUÍNEO, CPF E A DATA DA DOAÇÃO, DISPONHA QUE 
O CADASTRO ACEITA APENAS UMA DOAÇÃO/DIA.
OPÇÃO 2: USUÁRIO INSERE UM TIPO SANGUÍNEO E O PROGRAMA
RETORNA A BOLSA DE SANGUE COM MAIS TEMPO NO ESTOQUE.
OPÇÃO 3: LISTAR ESTOQUE.


UTILIZE A FILA (FIRST IN FIRST OUT)'''


cadastros = {
        'A+':[], 'A-':[], 'B+':[], 'B-':[], 'O+':[], 'O-':[], 'AB+':[], 'AB-':[],
}


#cadastros['A+].append(('000.000.00-00', '10/12/2024'))
#Inserir uma doação
#cpf, data = cadastros['A+].pop(0)
#obter bolsa do tipo A+

from datetime import datetime

# Dicionário para armazenar as doações, usando listas para implementar a fila
#banco_de_sangue = {
 #   'A+': [],
  #  'A-': [],
   # 'B+': [],
    #'B-': [],
    #'O+': [],
    #'O-': [],
    #'AB+': [],
    #'AB-': []
#}

'''while True:
    print("Menu de Opções:")
    print("1 - Cadastrar Doação")
    print("2 - Obter Bolsa de Sangue")
    print("3 - Listar Bolsas Disponíveis")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa...")
        break
    elif opcao == "1":
        tipo_sanguineo = input("Digite o tipo sanguíneo (A+, A-, B+, B-, O+, O-, AB+, AB-): ").upper()
        if tipo_sanguineo not in banco_de_sangue:
            print("Tipo sanguíneo inválido. Tente novamente.")
            continue
        cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
        data_doacao = input("Digite a data da doação (DIA/MES/ANO): ")
        try:
            data_formatada = datetime.strptime(data_doacao, "%d/%m/%Y")
        except ValueError:
            print("Data inválida. Tente novamente.")
            continue
        
        # Verificar se já existe uma doação do mesmo CPF no mesmo dia
        doacao_existente = False
        for doacao in banco_de_sangue[tipo_sanguineo]:
            if doacao[0] == cpf and doacao[1] == data_doacao:
                doacao_existente = True
                break
        
        if doacao_existente:
            print("Doação já registrada para este CPF nesta data.")
        else:
            banco_de_sangue[tipo_sanguineo].append((cpf, data_doacao))
            print("Doação cadastrada com sucesso!")
    elif opcao == "2":
        tipo_sanguineo = input("Digite o tipo sanguíneo desejado (A+, A-, B+, B-, O+, O-, AB+, AB-): ").upper()
        if tipo_sanguineo not in banco_de_sangue:
            print("Tipo sanguíneo inválido. Tente novamente.")
            continue
        
        if banco_de_sangue[tipo_sanguineo]:
            doacao = banco_de_sangue[tipo_sanguineo].pop(0)  # Remove a primeira doação na lista
            print(f"Bolsa de sangue obtida com sucesso! CPF: {doacao[0]}, Data da Doação: {doacao[1]}")
        else:
            print(f"Não há bolsas de sangue disponíveis para o tipo {tipo_sanguineo}.")
    elif opcao == "3":
        print("Bolsas de Sangue Disponíveis:")
        for tipo, doacoes in banco_de_sangue.items():
            print(f"Tipo {tipo}:")
            if not doacoes:
                print("  Nenhuma bolsa disponível.")
            else:
                for cpf, data_doacao in doacoes:
                    print(f"  CPF: {cpf}, Data da Doação: {data_doacao}")
    else:
        print("Opção inválida! Tente novamente.")
'''



from datetime import datetime

# Dicionário para armazenar as doações, usando listas para implementar a fila
banco_de_sangue = {
    'A+': [],
    'A-': [],
    'B+': [],
    'B-': [],
    'O+': [],
    'O-': [],
    'AB+': [],
    'AB-': []
}

while True:
    print("Menu de Opções:")
    print("1 - Cadastrar Doação")
    print("2 - Obter Bolsa de Sangue")
    print("3 - Listar Bolsas Disponíveis")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa...")
        break
    elif opcao == "1":
        tipo_sanguineo = input("Digite o tipo sanguíneo (A+, A-, B+, B-, O+, O-, AB+, AB-): ").upper()
        if tipo_sanguineo not in banco_de_sangue:
            print("Tipo sanguíneo inválido. Tente novamente.")
            continue
        cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
        data_doacao = input("Digite a data da doação (DIA/MES/ANO): ")
        try:
            data_formatada = datetime.strptime(data_doacao, "%d/%m/%Y")
        except ValueError:
            print("Data inválida. Tente novamente.")
            continue
        
        # Verificar se já existe uma doação do mesmo CPF no mesmo dia
        doacao_existente = False
        for doacao in banco_de_sangue[tipo_sanguineo]:
            if doacao[0] == cpf and doacao[1] == data_doacao:
                doacao_existente = True
                break
        
        if doacao_existente:
            print("Doação já registrada para este CPF nesta data.")
        else:
            banco_de_sangue[tipo_sanguineo].append((cpf, data_doacao))
            print("Doação cadastrada com sucesso!")
    elif opcao == "2":
        tipo_sanguineo = input("Digite o tipo sanguíneo desejado (A+, A-, B+, B-, O+, O-, AB+, AB-): ").upper()
        if tipo_sanguineo not in banco_de_sangue:
            print("Tipo sanguíneo inválido. Tente novamente.")
            continue
        
        if banco_de_sangue[tipo_sanguineo]:
            doacao = banco_de_sangue[tipo_sanguineo].pop(0)  # Remove a primeira doação na lista
            print(f"Bolsa de sangue obtida com sucesso! CPF: {doacao[0]}, Data da Doação: {doacao[1]}")
        else:
            print(f"Não há bolsas de sangue disponíveis para o tipo {tipo_sanguineo}.")
    elif opcao == "3":
        print("Bolsas de Sangue Disponíveis:")
        for tipo, doacoes in banco_de_sangue.items():
            print(f"Tipo {tipo}:")
            if not doacoes:
                print("  Nenhuma bolsa disponível.")
            else:
                for cpf, data_doacao in doacoes:
                    print(f"  CPF: {cpf}, Data da Doação: {data_doacao}")
    else:
        print("Opção inválida! Tente novamente.")
