'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/Pix: 10% DESCONTO
- À vista cartão: 5% DESCONTO
- Em até 2x no cartão: PREÇO NORMAL
- 3x ou mais no cartão: 20% DE JUROS
'''

print('LOJA DO POVO'.center(50, '='))
valor = float(input('Qual foi o valor das compras R$: '))
print('\033[1:31mFORMAS DE PAGAMENTO\033[m'.center(60))
print('''[1] À vista dinheiro ou PIX
[2] À vista cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão''')
escolha = int(input('Digite uma das opções acima: '))

print('\033[1:32mVALOR FINAL\033[m'.center(60, '='))

if escolha == 1:
    primeira = valor - (valor * 0.10)
    print('\033[1:34mVocê recebeu 10% de desconto!\033[m'.center(60))
    print('O valor total de sua compra ficou R$: \033[1:32m{}\033[m'.format(primeira))
elif escolha == 2:
    segunda = valor - (valor * 0.05)
    print('\033[1:34mVocê recebeu 5% de desconto!\033[m'.center(60))
    print('O valor total de sua compra ficou R$: \033[1:32m{}\033[m'.format(segunda))
elif escolha == 3:
    print('Sua compra será parcelada em 2x de {}'.format(valor / 2))
    print('O valor total de sua compra ficou R$: \033[1:32m{}\033[m'.format(valor))
elif escolha == 4:
    quarta = valor + (valor * 0.20)
    parcela = int(input('Quantas parcelas será: '))
    print('\033[1:33mPor escolher a opção 4, sua compra terá 20% de JUROS\033[m')
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcela, (quarta / parcela)))
    print('O valor total de sua compra ficou R$: \033[1:32m{}\033[m'.format(quarta))
else:
    print('\033[1:31mSua ecolha deve ser entre 1 e 4\033[m'.center(60))
    print('\033[1:31mDIGITE CORRETAMENTE\033[m'.center(60))

