#Desafio29 - Sistema de Multa

vel = float(input('\nDigite a velocidade do carro: '))
val = 7
print('Você estava a {:.2f}Km/h'.format(vel))

if vel > 80:
    val = (vel-80) * val
    print('Você ultrapassou os limites de velocidade e deverá pagar R${:.2f} de multa'.format(val))
print('Tenha um bom dia! Dirija com segurança!')