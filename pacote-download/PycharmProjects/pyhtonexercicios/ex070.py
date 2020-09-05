total = totimil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont = cont + 1
    total += preco
    if preco > 1000:
        totimil = totimil + 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
         break
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totimil} produtos com valor maior de R$ 1000,00.')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}.')
print('{:-^40}'.format(' Fim do programa '))
