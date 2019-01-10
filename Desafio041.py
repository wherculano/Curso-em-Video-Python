#Desafio041
from datetime import datetime

ano_atual = datetime.now().year
print('\n\t','-'*4,'NATAÇÃO','-'*4)

ano_nasc = int(input('Ano Nasc.: '))
idade = ano_atual - ano_nasc

print('\n','-'*3,'Categoria de acordo com a idade','-'*3)
print('Voce tem {} anos de idade'.format(idade))

if idade < 9:
    print('E esta na modalidade MIRIM')
elif idade >= 9 and idade < 14:
    print('E esta na modalidade INFANTIL')
elif idade >= 14 and idade < 19:
    print('E esta na modalidade JUNIOR')
elif idade >= 19 and idade < 20:
    print('E esta na modalidade SÊNIOR')
else:
    print('E esta na modalidade MASTER')