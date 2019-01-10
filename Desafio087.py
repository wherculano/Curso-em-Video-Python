"""
Desafio087 - Aprimore o desafio 86 mostrando no final:
A)A soma de todos os valores pares digitados
B)A soma dos valores da terceira coluna
C)O maior valor da segunda linha
Saida: A soma dos valores pares é 20
A soma dos valores da terceira coluna é 18
O maior valor da segunda linha é 6
"""

lista = []
pares, seg_col, terc_col = 0,0,0
for linha in range(3):
    for coluna in range(3):
        lista.append(int(input('Digite um valor para [{},{}]: '.format(linha, coluna))))

print('-='*30)

for n in range(len(lista)):
    print('[ {} ]'.format(lista[n]),end='')
    if (n+1) % 3 == 0:
        print()
        terc_col += lista[n]
    if lista[n] % 2 == 0:
        pares += lista[n]
    if (n+1) > 3 and (n+1) < 7:
        seg_col = max(lista[3:6])
        
print('-='*30)

#A
print('A soma dos valores pares é {}'.format(pares))
#B
print('A soma dos valores da terceira coluna é {}'.format(terc_col))
#C
print('O maior valor da segunda linha é {}'.format(seg_col))
