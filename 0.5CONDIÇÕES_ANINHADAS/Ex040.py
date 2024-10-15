'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7.0:
    print('A média foi igual a {:.2f}'.format(media))
    print('Aluno\033[1:32m APROVADO!\033[m')
elif media < 5.0:
    print('A média foi igual a {:.2f}'.format(media))
    print('O alino ficou foi\033[1:31m REPROVADO!\033[m')
else:
    print('A média foi igual a {:.2f}'.format(media))
    print('O aluno ficou de\033[1:33m RECUPERAÇÃO\033[m')