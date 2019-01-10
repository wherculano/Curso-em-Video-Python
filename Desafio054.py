'''
Desafio054: Leia o ano de nascimento
de 7 pessoas. No final mostre quantas
pessoas ainda não atingiram a maioridade
e quantas ja sao maiores
'''
from datetime import datetime

atual = datetime.now().year
ano = []
maior = 0
menor = 0

for i in range(7):
    a = int(input('Ano de nasc.: '))
    ano.append(a)
    if (atual-ano [i]) >= 21:
        maior += 1
    else:
        menor += 1

print('\nMaiores de idade: {}'.format(maior))
print('Menores de idade: {}'.format(menor))
    

