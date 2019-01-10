'''
Desafio69 - Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer
ou não continuar. No final, mostre:
A- quantas pessoas tem mais de 18 anos
B- quantos homens foram cadastrados
C- Quantas mulheres tem menos de 20 anos
'''
sair = 'N'
mul = hom = maior = 0
while sair in 'Nn':
    print('-'*40)
    print('\tCADASTRE UMA PESSOA')
    print('-'*40)
    try:
        idade = int(input('Idade: '))
    except:
        print('Digite apenas numeros inteiros!')
        idade = int(input('Idade: '))
    try:
        sexo = input('Sexo [M/F]: ')
    except:
        print('Escolha apenas [M/F]')
        sexo = input('Sexo [M/F]: ')
    if sexo not in 'MmFf':
        sexo = input('Sexo [M/F]: ')        
    print('-'*40)
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        hom += 1
    if sexo in 'Ff' and idade < 20:
        mul += 1
    sair = input('Deseja sair? [S/N]: ')

print('-'*5,'FIM','-'*5)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {hom}')
print(f'Mulheres menores de 20 anos: {mul}')
