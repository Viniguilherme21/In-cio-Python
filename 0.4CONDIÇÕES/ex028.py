'''
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu o desafio.
'''

import random
import time
from time import sleep

num = (1, 2, 3, 4, 5)
escolha = random.choice(num)

usuario = int(input("Escolha um número entre 1 a 5: "))

if usuario == escolha:
    print('-=-' * 20)
    print('Número escolhido pela máquina....PROCESSANDO')
    sleep(2)
    print('NÚMERO: {}'.format(escolha))
    print('-=-' * 20)
    print('Você venceu o desafio!')
    print('-=-' * 20)
    print('PARABÉNS!')
else:
    print('-=-' * 20)
    print('Número escolhido pela máquina....PROCESSANDO')
    sleep(2)
    print('NÚMERO: {}'.format(escolha))
    print('-=-' * 20)
    print('Você perdeu o desafio!')
    print('-=-' * 20)
    print('TENTE NOVAMENTE!')

