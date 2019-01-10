'''
Desafio057: Faca um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F. Caso esteja errado, peça
a digitação novamente até ter um valor correto.
'''
sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]

while sexo not in 'MmFf':
    sexo = input('Dados inválidos!\nDigite seu sexo [M/F]: ').strip().upper()[0]
    
print('\nObrigado!\nSexo "{}" registrado com sucesso!'.format(sexo))
