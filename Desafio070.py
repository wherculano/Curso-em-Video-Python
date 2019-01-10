#Desafio 70
'''Crie uma programa que leia o nome
e o preco de varios produtos. O programa
deve questionar se o usuario vai continuar.
No final deve mostrar o total da compra,
o produto acima de 1000 e o mais barato  '''

print('\n','='*5,'LISTA DE COMPRAS','='*5)
total = maior = menor = cont = 0
barato = ''
while True:
    produto = input('Produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maior += 1
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    op = ' '
    while op not in 'SN':
        op = input('Continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break


print('\n{:-^40}'.format('FIM DO PROGRAMA'))
print('\nTotal da compra R${:.2f}'.format(total))
print('{} produto(s) mais caro(s) que R$1000,00'.format(maior))
print('O produto mais barato foi o(a) {} que custou R${:.2f}'.format(barato,menor))








