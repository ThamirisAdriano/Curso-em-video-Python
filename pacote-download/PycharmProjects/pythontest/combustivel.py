gasolina = float(input('Valor da gasolina: R$ '))
etanol = float(input('Valor do etanol: R$ '))
combustivel = gasolina * 0.7
if combustivel >= etanol:
    print('Abasteça com gasolina.')
elif combustivel < etanol:
    print('Abasteça com etanol.')