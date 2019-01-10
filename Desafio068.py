'''
Desafio68 - Faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador PERDER, mostrando o total
de vitorias consecutivas que ele conquistou no final do jogo.
'''
from random import randint

print('-'*10, 'PAR OU IMPAR','-'*10)
vit = 0
res = ''
pc = randint(1,10)

while True:
    vc = int(input('Diga um valor: '))
    op = input('PAR ou IMPAR? -> [P/I]: ').strip().upper()
    soma = vc+pc
    print('-'*45)
    print(f'Você jogou {vc} e o computador {pc}. Total de {soma}.', end='')
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print(f'Deu {res}')
    print('-'*45)
    
    if (op == 'P' and res == 'PAR') or (op == 'I' and res == 'IMPAR'):
        print('Você venceu!')
        vit += 1
    else:
        print('Você perdeu!')
        break
    print('Vamos jogar novamente...')
    print('-'*45)
print(f'Você venceu {vit} vezes')
