'''
Desafio065: Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execução mostre a media entre todos os valores e qual foi o maior
e o menor valores. O programa deve perguntar ao usuario se ele quer ou não
continuar a digitar valores.
'''
sair = 'n'
maior = menor = media = soma = cont = 0

while not sair in 'sS':
    n = int(input('Número: '))
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
    sair = input('Deseja sair?[S/N]: ').strip()[0]
    
media = soma / cont

print('\nNúmeros: {}'.format(cont))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
print('Media: {}'.format(media))
print('Soma: {}'.format(soma))
        
        
