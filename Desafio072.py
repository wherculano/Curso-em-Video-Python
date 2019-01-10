#--MUNDO 3--
#Desafio 72
'''
Crie um programaa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
O programa deverá também verificar se o usuário digitou o intervalo correto (0 a 20).
Ex.: Digite um numero entre 0 e 20: 90 (erro! tente novamente!)
Ex.: Digite um numero entre 0 e 20: 16. (vc digitou o numero dezesseis)
'''
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinte', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

indice = int(input('Digite um número entre 0 e 20: '))
while indice < 0 or indice > 20:
    print('Tente Novamente!')
    indice = int(input('Digite um número entre 0 e 20: '))
print('Você digitou o número {}'.format(numeros[indice]))

