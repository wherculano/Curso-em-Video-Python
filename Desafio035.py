#Desafio35 - Formar um triangulo

r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if (r1+r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1:
    print('É  possível criar um triangulo')
else:
    print('Não é possivel criar um triângulo')
