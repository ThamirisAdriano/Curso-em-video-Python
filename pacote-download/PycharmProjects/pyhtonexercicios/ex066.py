s = cont = 0
while  True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s = s + n
    cont = cont + 1
print(f'A quantidade de números digitados foi {cont} e a soma entre eles resultou em {s}.')
print('Fim')
