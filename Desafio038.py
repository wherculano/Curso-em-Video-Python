#Desafio038
n1 = int(input('\nDigite um numero inteiro qualquer: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 > n2:
    print('{} > {}'.format(n1,n2))
elif n2 > n1:
    print('{} > {}'.format(n2, n1))
else:
    print('{} = {}'.format(n1, n2))
