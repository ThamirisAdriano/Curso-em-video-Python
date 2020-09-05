numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = str(input('Quer continuar? S/N ')).upper().strip()
    if r == 'N':
        break
print('-='* 30)
numeros.sort()
print(f' Você adicionou os valores {numeros}')
