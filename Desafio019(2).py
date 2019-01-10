import random

registro = []

opc = int(input('\n1- Cadastrar novo sorteado\n2- Consultar o banco de registros\n3- Sortear\n0- Sair\nOpcão: '))

if opc >= 0 and opc <= 3:
    while opc != 0:
        if opc == 1:
             registro.append(input('Digite o que será registrado: '))
             print('\nGravado com sucesso')
             opc = int(input('\n1 para cadastrar um novo sorteado\n2 para consultar o banco de registros\n3 para sortear\n0 para sair\nOpcão: '))

        elif opc == 2:
            print(registro)
            opc = int(input('\n1 para cadastrar um novo sorteado\n2 para consultar o banco de registros\n3 para sortear\n0 para sair\nOpcão: '))

        elif opc == 3:
            print(random.choice(registro))
            opc = int(input('\n1 para cadastrar um novo sorteado\n2 para consultar o banco de registros\n3 para sortear\n0 para sair\nOpcão: '))
else:
    print('Digite apenas números válidos!')
