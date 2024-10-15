'''
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado
'''

km = float(input('Digite a quantidade de km percorrido. km: '))
dias = int(input('Digite a quantidade de dias que o veículos ficou alugado:  '))

cal = (dias * 60) + (km * 0.15)

print('Km percorridos: {}km \nDias locado: {} \nValor a ser pago: R${:.2f} '.format(km, dias, cal))

