#Desafio079
'''
Digite varios valores numericos e cadastre-os em um lista.
Caso o numero ja exista dentro, ele não será adicionado.
No final, serão exibidos todos os valores unicos digitados
em ordem crescente.
'''
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado!')
    cont = input('Quer continuar? [S/N] -> ').upper()
    if cont == 'S':
        continue
    else:
        break
lista.sort()
print('Voce digitou os valores {}'.format(lista))
