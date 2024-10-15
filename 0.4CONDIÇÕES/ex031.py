'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

dis = float(input('Digite a distância de sua viagem. Km:'))
a = .50
b = .45

if dis <= 200:
    print('O preço de sua viagem ficou R$ {:.2f}'.format((dis * a)))
else:
    print('O \033[1;31mpreço\033[m de sua viagen ficou R$ {:.2f}'.format(dis * b))

