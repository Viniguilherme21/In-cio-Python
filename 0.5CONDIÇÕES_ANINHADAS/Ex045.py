'''
Elabore um programa que faça o computador jogar JOKENPÔ com você:
'''

import time
import random
from random import randint

from dateutil.utils import today
from openpyxl.worksheet.print_settings import PRINT_AREA_RE

print('VAMOS JOGAR JOKENPÔ!!'.center(40, '='))

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Suas escolhas
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua escolha? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
print('=-=' * 13)
print('O Jogador escolheu: \033[1:31m{}\033[m'.format(itens [jogador]))
print('O Computador escolheu \033[1:34m{}\033[m'.format(itens [computador]))
print('=-=' * 13)

if computador == 0:
    if jogador == 0:
        print('\033[1:32mO jogo EMPATOU!\033[m')
    elif jogador == 1:
        print('\033[1:31mO JOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1:34mO COMPUTADOR VENCEU\033[m')
    else:
        print('Jogada Inválida!')
elif computador == 1:
    if jogador == 0:
        print('\033[1:34mO COMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1:32mO JOGO EMPATOU\033[m')
    elif jogador == 2:
        print('\033[1:31mO JOGADOR VENCEU\033[m')
    else:
        print('Jogada Inválida"')
elif computador == 2:
    if jogador == 0:
        print('\033[1:31mO JOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1:34mO COMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1:32mO JOGO EMPATOU\033[m')
    else:
        print('Jogada Inválida!')

