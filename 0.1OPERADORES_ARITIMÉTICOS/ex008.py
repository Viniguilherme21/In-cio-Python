'''
Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
'''

val = float(input('Digite o valor do metro: '))
cm = val * 100
mm = val * 1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(val, cm, mm))



