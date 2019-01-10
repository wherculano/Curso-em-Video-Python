#Desafio096
'''CONTROLE DE TERRENOS
>>> "Largura: " 10
>>> "Comptimento: " 25.5
>>> 255
'''
def calc_area(larg, comp):
	return larg * comp
	
print('CONTROLE DE TERRENO'.center(30,'-'))

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
print('-='*21)
print(f'A area de um terreno {largura}x{comprimento} é de {calc_area(largura,comprimento):.2f}m2')
