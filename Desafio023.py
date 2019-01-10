#Desafio 23
n = int(input('\nDigite um numero entre 1 e 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('\nUnidade: {}'.format(u))
print('Dezena: {:>2}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {:>2}'.format(m))