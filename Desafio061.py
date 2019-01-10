'''
Desafio061: Refaca o Desafio051, lendo o primeiro termo e a razao de uma PA,
mostrando os 10 primeiros termos da progressao usando a estrutura while
'''
print('\n-=-=-=PROGRESSÃO ARITMÉTICA-=-=-=')
pt = int(input('\nPrimeiro termo: '))
rz = int(input('Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo),end=' -> ')
    termo += rz
    cont+=1
print('FIM')
