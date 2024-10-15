'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou passou do prazo
'''

from datetime import date

atual = date.today().year
ano = int(input('Digite o ano do Nascimento: '))
idade = atual - ano

print('Quem nasceu em {} tem \033[1:31m{} anos\033[m em {}'.format(ano, idade, atual))

if idade < 18:
    saldo = 18 - idade
    print('\033[1:33mFalta {} anos\033[m para o alistamento militar'.format( saldo ))
    print('Seu alistamento será em {}'.format(atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('\033[1:31mUltrapassou {} anos\033[m do seu alistamento militar'.format(saldo))
    print('Você deveria ter se alistado em {}'.format(atual - saldo))
else: print('Está na \033[1:34midade correta\033[m para o alistamento militar')

