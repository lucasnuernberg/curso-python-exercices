
valorc = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar a casa: '))
cond = valorc / (anos*12)
print('{}O valor a ser pago mensalmente é de R${:.2f}'.format('\033[32m', cond), end='')
if cond > 0.3*salario:
    print('\nInfelizmente seu emprestimo foi negado')
elif cond < 0.3*salario:
    print('\nEmprestimo aceito você deverá pagar R${:.2f} por mês'.format(cond))

