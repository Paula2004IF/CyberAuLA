# Inicialização das listas para armazenar os dados cadastrais
nomes = []
sobrenomes = []
cpfs = []
emails = []
telefones = []

#lalalalalala

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

    # Adiciona os dados nas respectivas listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    cpfs.append(cpf)
    emails.append(email)
    telefones.append(telefone)

# Exibe os dados cadastrados em formato de tabela
print("\nDados Cadastrais:")
print(f"{'Nome':<15} {'Sobrenome':<15} {'CPF':<15} {'Email':<30} {'Telefone':<15}")
print("-" * 90)

for i in range(quantidade):
    print(f"{nomes[i]:<15} {sobrenomes[i]:<15} {cpfs[i]:<15} {emails[i]:<30} {telefones[i]:<15}")
