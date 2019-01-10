'''
Desafio052: leia um numero inteiro e
diga se é ou nao um numero primo
(divisivel por 1 e por ele mesmo apenas)
'''
num = int(input('Digite um numero inteiro: '))
tot = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))

if tot == 2:
    print('É primo')
else:
    print('NÃO é primo!')
