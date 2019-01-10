#Desafio042
r1 = int(input('\nReta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('Com essas retas é possivel criar um triângulo ',end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Nao é possível criar um triângulo')