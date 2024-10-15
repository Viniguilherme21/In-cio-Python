'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra “SANTO”.
'''

cidade = input('Digite o nome de sua cidade: ').strip().split()
ver = (cidade[0].upper() == 'SANTO') #JOGAMOS TUDO PARA MAIÚSCULA (com o upper) PARA DEPOIS VERIFICARMOS TUDO EM MAIÚSCULA

if ver:
    print('Sua cidade começa com a palavra SANTO')
else:
    print('Sua cidade não começa com a palavra SANTO')



