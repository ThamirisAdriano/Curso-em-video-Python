termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10-1) * razao
for c in range(termo1, decimo + razao, razao):
    print('{}'.format(c), end='->')
print('ACABOU!')
