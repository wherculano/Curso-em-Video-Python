#Desafio092
'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário incluindo o total
de gols feitos durante o campeonato.
'''

jogador = dict()
jogador['nome'] = input('Digite o nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = [int(input(f' Quantos gols na partida {_}: ')) for _ in range(partidas)]
jogador['total'] = sum(jogador['gols'])

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f'O campo {str(k).upper()} tem o valor {v}')

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, gols in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {gols} gols')
print(f'Foi um total de {jogador["total"]} gols.')
    
