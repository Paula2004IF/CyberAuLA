# Lista para armazenar tuplas com os dados cadastrais
cadastros = []

# Solicita ao usuário a quantidade de cadastros que deseja fazer
quantidade = int(input("Quantas pessoas deseja cadastrar? "))

# Loop para cadastrar a quantidade de pessoas especificada
for i in range(quantidade):
    print(f"\nCadastro {i+1}")
    
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    # Cria uma tupla com os dados e adiciona na lista de cadastros
    cadastro = (nome, sobrenome, cpf, email, telefone)
    cadastros.append(cadastro)

# Exibe os dados cadastrados em formato de tabela
print("\nDados Cadastrais:")
print(f"{'Nome':<15} {'Sobrenome':<15} {'CPF':<15} {'Email':<30} {'Telefone':<15}")
print("-" * 90)

for cadastro in cadastros:
    print(f"{cadastro[0]:<15} {cadastro[1]:<15} {cadastro[2]:<15} {cadastro[3]:<30} {cadastro[4]:<15}")
