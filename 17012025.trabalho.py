def q1():
    # Solicitar informações ao usuário
    valor_avista = float(input("Informe o valor à vista do bem: R$ "))
    valor_entrada = float(input("Informe o valor da entrada: R$ "))
    quantidade_parcelas = int(input("Informe a quantidade de parcelas: "))
    taxa_juros_mensal = float(input("Informe a taxa de juros mensal (%): "))

# Calcular valor a financiar
    valor_financiar = valor_avista - valor_entrada

# Calcular valor da parcela usando a fórmula do valor presente das prestações
# Fórmula: Parcela = valor_financiar * [ (1 + taxa_juros_mensal)^quantidade_parcelas * taxa_juros_mensal ] / [ (1 + taxa_juros_mensal)^quantidade_parcelas - 1 ]
    taxa_juros_mensal /= 100  # Converter taxa de juros para decimal
    parcela = valor_financiar * ( (1 + taxa_juros_mensal)**quantidade_parcelas * taxa_juros_mensal ) / ( (1 + taxa_juros_mensal)**quantidade_parcelas - 1 )

# Exibir valor da parcela
    print(f"O valor da parcela será de R$ {parcela:.2f}")


    q1()