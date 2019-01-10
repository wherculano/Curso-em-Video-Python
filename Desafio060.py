'''
Desafio060: Faca um programa que leia um numero qualquer e mostre o fatorial
Ex.: 5*4*3*2*1 = 120
'''
print('''-----CALCULO DE FATORIAL----
[1] Para Laço FOR
[2] Para Laço WHILE
[3] Para Builtin
[4] Para SAIR
''')
fat = 1
cont = 1
from math import factorial
while True:
    try:
        op = int(input('\nOpção: '))
    except:
        print('Digite apenas Opções válidas!')
     
    if op == 4:
        print('Saindo.....')
        quit()
    else:
        num = int(input('Fatorial de: '))

        if op == 1:
            for i in range(1,num+1):
                fat *= i
            break
        elif op == 2:
            while cont <= num:
                fat *= cont
                cont += 1
            break
        elif op == 3:
            fat = factorial(num)
        else:
            print('Digite apenas Opções válidas!')
    break
    
for i in range(num,0,-1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
print('{}'.format(fat))
