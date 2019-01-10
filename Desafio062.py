'''
Desafio062: Melhore o Desafio061, perguntando para o usuario se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 termos.
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo),end=' -> ')
        termo += razao
        cont+=1
    print('Pausa....') 
    mais = int(input('Quantos termos voce quer ver a mais? '))
print('FIM') 
print('\nForam mostrados {} termos da Progressão Aritmética'.format(total))  
