"""
Desafio046: Mostrar na tela uma contagem regressiva para o estouro de fogos
de artificio de 10 a 0 com uma pause de 1 segundo entre eles
"""

from time import sleep
print('=-'*5+'CONTAGEM REGRESSIVA'+'-='*5)
for i in range(10,0,-1):
    print(i)
    sleep(1)
print('=-'*5+'FELIZ ANO NOVO!!!'+'-='*5)

