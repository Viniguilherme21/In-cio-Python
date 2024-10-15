'''
Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''

#SEM IMPORTAÇÃO. ABAIXO, CRIAMOS UMA VARIÁVEL COM A FÓRMULA MATEMÁTICA
'''opos = float(input('Digite o comprimento do cateto oposto?: '))
adja = float(input('Digite o comprimento do cateto adjacente: '))
hi = (opos ** 2 + adja ** 2) ** (1/2)

print('A hipotenusa vai medir: {:.2f}'.format(hi))'''

#COM IMPORTAÇÃO. NESTA ETAPA NOS IMPORTAMOS A BIBLIOTECA MATH, JUNTO A HYPOT QUE TEM COMO FUNÇÃO CALCULAR A HIPOTENUSA.
import math
opos = float(input('Digite o comprimento do cateto oposto?: '))
adja = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(opos, adja)

print('A hipotenusa vai medir: {:.2f}'.format(hi))
