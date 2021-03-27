#mostra os 10 termos seguintes
termo  = int(input('digite um termo: '.capitalize()))
razao = int(input('digite a razão: '.capitalize()))
décimo = termo + (10 - 1) * razao
for c in range(termo, décimo + razao, razao):
    print(c, end=' 😀 ')