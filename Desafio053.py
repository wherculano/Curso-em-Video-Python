'''
Desafio053: Leia uma frase qualquer e diga se é um palindromo
'''
frase = input('Digite uma frase: ')
if frase == frase[::-1]:
    print('Esta frase é um palindromo!')
else:
    print('Esta frase não é um palindromo!')
