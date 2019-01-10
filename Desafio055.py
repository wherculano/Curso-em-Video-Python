'''
Desafio055: Leia o peso de 5 pessoas
e no final mostre qual foi o maior e
o menor peso lido
'''

pesos = []
for i in range(1,6):
    p = float(input('Qual seu peso: '))
    pesos.append(p)
    
print('\nMaior peso: {:.2f}'.format(max(pesos)))
print('Menor peso: {:.2f}'.format(min(pesos)))

"""
maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Digite o peso da {} pessoa: ').format(p))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
"""
