print('='*15 + 'LOJAS LUCAS' + '='*15)
compras = float(input('Digite o preço das compras: R$'))
precoFinal = compras
print('FORMAS DE PAGAMENTO:')
print('[1] á vista')
print('[2] á vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
metodoPagamento = int(input('Qual o metodo de pagamento? '))

if metodoPagamento == 1:
    precoFinal = compras * 0.9
elif metodoPagamento == 2:
    precoFinal = compras * 0.95
elif metodoPagamento == 3:
    precoFinal = compras
else:
    precoFinal = compras * 1.20
print(f'\nO preço a ser pago é de R${precoFinal:.2f}')