#Desafio33 Ler 3 numeros e falar qual é maior e menor

n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if ((n1 > n2) & (n1 > n3)):
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
if((n2 > n1) & (n2 > n3)):
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
if((n3 > n1) & (n3 > n2)):
    maior = n3
    if n2 > n1:
        menor = n1
    else:
        menor = n2    

print('{} é o maior número e {} é o menor!'.format(maior, menor))
    
