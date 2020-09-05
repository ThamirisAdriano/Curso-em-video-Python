primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <=10:
    print('{}'.format(primeiro), end=' ')
    primeiro = primeiro + razao
    cont = cont + 1
print('FIM!!!')