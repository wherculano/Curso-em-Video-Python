#--MUNDO 3--
#Desafio 76
'''
Crie um programa que tenha uma tupla unica com nomes de produtos e seus
respectivos precos na sequencia.
No final, mostre uma listagem de precos, organizando os dados em forma tabular.
Ex.: Lapis..................R$ 1.75 (os caracteres estão alinhados ao maior numero)
Borracha 2.00, Caderno, 15.90, Estojo 25.00, Transferidor 4.20, Compasso 9.99, Mochila 120.32,
Canetas 22.30 e Livro 34.90
'''
prod = ('Lapis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,
        'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

print('{:=^30}'.format('LISTA DE MATERIAIS'))
for itens in range(0, len(prod),2):
    print('{:.<20}R$ {:>6.2f}'.format(prod[itens], prod[itens+1]))


