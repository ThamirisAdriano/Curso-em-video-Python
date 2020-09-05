numero = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numero[-1]:
        numero.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
                numero.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {numero}')
