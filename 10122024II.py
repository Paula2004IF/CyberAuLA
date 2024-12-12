'''
Faça um programa de banco de sangue. Neste programa, há as seguintes opções:

1 - Cadastrar doação
2 - Obter bolsa de sangue
3 - Listar bolsas disponíveis

* Na opção 1, você deve inserir os dados de uma doação que acabou de ser feita: tipo sanguíneo, cpf e data de doação.
  Considere que uma pessoa só pode doar uma bolsa de sangue por dia.
* Na opção 2, o usuário deve inserir um tipo sanguíneo e o programa deve obter a bolsa desse tipo que está há mais
  tempo guardada. Essa bolsa deve ser, então, removida do estoque.
* Na opção 3, o programa deve mostrar uma tabela com todas as bolsas disponíveis.
'''

cadastros = {
    'A+': [], 'A-': [], 'B+': [], 'B-': [], 'O+': [], 'O-': [], 'AB+': [], 'AB-': []
}

#cadastros['A+'].append( ('000.000.000-00', '10/12/24') ) # Inserir uma doação
#cpf, data = cadastros['A+'].pop(0) # Obter bolsa do tipo A+

while True:
    print('1 - Cadastro')
    print('2 - Obter')
    print('3 - Listar')
    op = input('Opção: ')
    if op == '1':
        tipo = input('Tipo sanguíneo: ').upper()
        cpf = input('CPF do doador: ')
        data = input('Data de doação: ')
        cadastros[tipo].append( (cpf, data) )
        print('Doação registrada!')
    elif op == '2':
        tipo = input('Tipo sanguíneo: ').upper()
        cpf, data = cadastros[tipo].pop(0)
        print('CPF do doador:', cpf)
        print('Data de doação:', data)
    elif op == '3':
        print('CPF | TIPO SANGUÍNEO | DATA DE DOAÇÃO')
        for tipo, bolsas in cadastros.items():
            for cpf, data in bolsas:
                print(f'{cpf} | {tipo} | {data}')
    else:
        print('Opção inválida!')

