'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere
U$:1,00 = R$3,27
'''

cart = float(input('Digite o valor de sua carteira: R$'))

us = 3.27
compra = cart/us

print('De acordo com o valor de sua carteira, você pode comprar U${:.2f}'.format(compra))

