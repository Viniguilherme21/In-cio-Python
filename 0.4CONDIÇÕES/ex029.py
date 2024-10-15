'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que foi multado.

A multa vai custar R$7,00 por cada km acima do limite.
'''

vel = float(input('Qual a velocidade que o veículo estava no momento do radar? Km/h: '))
val = (vel - 80) * 7

if vel >80:
    print('O limite da via é 80 km/h.')
    print('==' * 20)
    print('Você foi multado no valor de R$ {:.2f}'.format(val))
    print('==' * 20)
else:
    print('{} km/h, está dentro da velocidade permitida!'.format(vel))

