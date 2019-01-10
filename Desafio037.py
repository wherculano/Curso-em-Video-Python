#Desafio037 - Binario, Octal e Hexadecimal

sair = 's'
while sair == 's':
    n = int(input('\nDigite um número inteiro: '))
    op = int(input('\nAgora escolha para qual base deseja converte-lo:\
\n1- Binário\n2- Octal\n3- Hexadecimal\n'))
    if op == 1:
        print('{} em Binário = {}\n'.format(n, str(bin(n)).replace('0b','')))
    elif op == 2:
        print('{} em Octal = {}\n'.format(n,str(oct(n)).replace('0o','')))
    elif op == 3:
        print('{} em Hexadecimal = {}\n'.format(n,str(hex(n)).replace('0x','')))
    else:
        print('Opção inválida!\n')
    sair = input('Deseja continuar?\n(S/N): ').lower()
