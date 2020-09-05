lista = []
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? S/N')).upper().strip()
    if cont == 'N':
        break
for i, v in enumerate(lista):
    if v % 2==0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append(v)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

