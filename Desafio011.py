#pega largura e altura de una parede
#e diz quantos litros de tinta sera
#necessário para pinta-la

l = float (input ('\nDigite a largura: '))
h = float (input ('Digite a altuta: '))
a = l*h
lt = a / 2
print ('\nA parede possui {:.2f} metros quadrados.'.format(a))
print ('E serão necessários {:.2f} litros de tinta para pinta-la'.format(lt))