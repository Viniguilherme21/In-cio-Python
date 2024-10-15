'''
A confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÉNIOR
- Acima: Master
'''

from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print('Considerando o ano de nascimento, o atleta \033[1:36mtem ou fará {} ANOS\033[m neste ano.'.format(idade))

if idade < 10:
    print('''De acordo com a idade '{} anos'
A \033[1:35mcategoria é MIRIM\033[m'''.format(idade))
elif idade < 15:
    print('''De acordo com a idade '{} anos'
A \033[1:31mcategoria é INFANTIL\033[m'''.format(idade))
elif idade < 20:
    print('''De acordo com a idade '{} anos'
A \033[1:32mcategoria é JUNIOR\033[m'''.format(idade))
elif idade < 25:
    print('''De acordo com a idade '{} anos'
A \033[1:33mcategoria é SÉNIOR\033[m'''.format(idade))
else:
    print('''De acordo com a idade '{} anos'
A \033[1:34mcategoria é MASTER\033[m'''.format(idade))

