'''
Escreva um programa que converta uma temperatura digitada em °C e converta para °F
'''

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32 #Equação de °C para °F (fórmula física)
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))


