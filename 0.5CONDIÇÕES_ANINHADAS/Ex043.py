'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL
- 25 até 30: SOBREPESO
- 30 até 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIA
'''

print('\33[1:31m-=' * 20)
print('\033[1:32mCALCULANDO SEU IMC\033[m'.center(50))
print('\033[1:31m-=\033[m' * 20)
peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC está em: {:.1f}'.format(imc))
print('\033[1:31m-=\033[m' * 20)
if imc < 18.5:
    print('Você está \033[1:34mABAIXO DO PESO!\33[1:34m')
elif imc < 25:
    print('Você está com o \33[1:33mPESO IDEAL\033[m')
elif imc <= 30:
    print('Você está com \033[1:31mSOBREPESO\033[m')
elif imc <= 40:
    print('Você está com \033[1:31mOBISIDADE\033[m')
else: print('Você está com \033[1:31mOBESIDADE MÓRBIDA\033[m')
