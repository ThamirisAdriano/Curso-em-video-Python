num = [[], []]
c = 0
for c in range(0,7):
    valores = int(input(f'Digite o {c+1}º valor: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}')



