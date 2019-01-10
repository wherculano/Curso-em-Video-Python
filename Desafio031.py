#Desafio31 - Distancia da Viagem e Passagem

dist = int(input('Distancia da viagem em Km: '))

if dist > 200:
    val = dist * 0.45
    print('Sua viagem possui {}Km de distancia e a passagem ficará no valor de R${:.2f}'.format(dist, val))
else:
    val = dist * 0.5
    print('Sua viagem possui {}Km de distancia e a passagem ficará no valor de R${:.2f}'.format(dist,val))

    
