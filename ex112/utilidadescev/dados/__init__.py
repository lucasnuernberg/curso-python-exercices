def leidinheiro():
    while True:
        din = input('Digite o preço: ').replace(',', '.')
        if ('').join(din.split()).isalpha() or din.strip() == '':
            print('\033[31mERRO!\033[m')
        else:
            din = float(din)
            return din
            break






