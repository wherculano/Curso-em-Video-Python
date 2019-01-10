#Desafio043
peso = float(input('\nQual seu peso: '))
altura = float(input('Qual sua altura: '))
	
imc = peso / (altura**2)
print('Seu IMC = {:.2f}'.format(imc))

if imc < 18.5:
    print('Voce está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Voce esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('Voce esta com sobrepeso')
elif imc >=30 and imc < 40:
    print('Voce esta com obesidade')
else:
    print('Voce esta com obesidade morbida')
    
