dias = int(input('Quantidade de dias alugados: '))
valor = dias * 60
km = float(input('Quantidade de km rodados: '))
valor2 = km * 0.15
print('O valor a ser pago é de {:.2f}.'.format(valor+valor2))
