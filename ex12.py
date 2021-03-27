print('-'*60)
preco = float(input('Digite o preço do produto que você quer adquirir: R$'))

precoComDesconto = preco * 0.95

print('Com um desconto de 5% o valor do produto passa a ser R${:.2f}'.format(precoComDesconto))
print('-'*60)