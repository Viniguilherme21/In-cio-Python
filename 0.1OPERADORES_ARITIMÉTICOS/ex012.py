'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
'''

valor = float(input('Qual valor do produto? R$'))

desc = valor - (valor * 0.05)

print('Com 5% de desconto, o produto custará: R${:.2f}'.format(desc))

