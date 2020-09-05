n = cont = soma = 0
n = int(input('Digite um valor: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um valor: '))
print('{} foram digitados e a soma entre eles foi {}.'.format(cont, soma))

