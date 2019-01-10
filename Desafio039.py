#Desafio039
from datetime import datetime


ano_nasc = int(input('Em qual ano você nasceu: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nasc
print('Voce tem {} anos'.format(idade))

if idade < 18:
    print('\nVocê ainda vai se alistar\nFalta(m) {} ano(s)\n'.format(18-idade))
elif idade == 18:
    print('\nJá está na hora de se alistar!')
else:
    print('\nJa se passaram {} anos que você deveria ter se alistado'.format(idade-18))
