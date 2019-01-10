'''
Desafio056: Leia nome, idade e sexo de
4 pessoas e no final o programa deve
mostrar a media de idade, nome do 
homem mais velho e quantas mulheres
tem menos de 20 anos
'''
media = 0.
soma = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulheres20 = 0

for i in range(1,5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Qual sua idade: '))
    sexo = input('Qual seu sexo? M/F: ').strip()
    soma+= idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
print('')   
print('\033[1;34m-='*5+'Resultado'+'-='*5+'\033[m')
media = soma / 4
print('Media de idade: {}'.format(media))
print('O Homem mais velho se chama {} e tem {} anos'.format(nomeVelho,maiorIdadeHomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres20))

