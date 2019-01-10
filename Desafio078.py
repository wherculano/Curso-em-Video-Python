#Desafio078
'''
Ler 5 valores e guardar em uma lista.
No final mostral qual foi o maior e o menor valor
digitado e as suas posições na lista
'''

valores = [int(input('Digite o valor para a posição {}: '.format(i))) for i in range(5)]
print('=-'*30)
print('Você digitou os valores {}: '.format(valores))

maior = max(valores)
menor = min(valores)

print('O maior valor digitado foi o {} nas posições '.format(maior), end='')
for ind, val in enumerate(valores):
    if val == maior:
        print(f'{ind}...',end='')
        
print('\nO menor valor digitado foi o {} nas posições '.format(menor),end='')
for ind, val in enumerate(valores):
    if val == menor:
        print(f'{ind}...', end='')
