#Desafio104.py
'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante a função input() do Python, so que fazendo a validação para aceitar
apenas um valor numerico.
Ex: n = leiaInt('Digite um n')

n = leiaInt('Digite um numero: ')
print(f"Você acabou de digitar o numero {n}")
>>> Digite um numero: 4
>>> Voce acabou de digitar o numero 4

>>> Digite um numero: 
>>> Erro: Digite um numero inteiro

>>> Digite um numero: w
>>> Erro: Digite um numero inteiro valido
'''
def leiaInt(msg='Digite um numero: '):
        while True:
                num = input(msg)
                if num.isnumeric():
                        return int(num)
                        break
                else:
                        print('\[033[0;31mERRO: Digite um NUMERO valido!\033[m')
	


#Main
n = leiaInt()
print(f'Voce digitou o numero {n}')
