"""
Desafio089 - Crie um programa que leia nome e duas notas de varios alunos
e guarde tudo em uma lista composta. No final mostre um boletim contendo a media
de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente
"""
alunos = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2 
    alunos.append( [nome, [n1, n2], media] )
    sair = input('Deseja sair? [S/N] ')
    if sair in 'sS':
        break

print('-='*30)

print(f'{"Nº ":<2}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)

for i,a in enumerate(alunos):
	print('{:<4}{:<10}{:>8.1f}'.format(i,a[0],a[2]))

print('-'*30)
while True:
    try:
        op = int(input('Mostrar notas de qual aluno acima?\nDigite o número ou 999 para sair: '))
        if op == 999:
            print('Saindo...')
            break
        elif op <= len(alunos):
            print('-'*30)
            print('Notas de {} são {}'.format(alunos[op][0], alunos[op][1]))
            print('-'*30)
    except IndexError:
        print('Não há nenhum aluno com este número!')
        print('-'*30)