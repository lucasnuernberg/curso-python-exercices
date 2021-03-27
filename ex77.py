#pegando as vogais

palavras = ('FORTALECER', 'COMPETIR', 'FOCAR', 'COMPARECER', 'SUPERAR', 'SURPREENDER')

for n in palavras:
    print(f'\n{n}', end=' ')
    for letra in n:
        if letra in 'AEIOU':
            print(letra, end=' ')






