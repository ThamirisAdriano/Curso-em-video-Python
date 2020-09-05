print('GERADOR DE PA')
print('=-'*10)
primeiro = int(input('Digite um termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print('{} ->'.format(termo), end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA..')
    mais = int(input('Quantos termos você quer mostrar?'))
print('Progressão finalizada com {} termos!'.format(total))