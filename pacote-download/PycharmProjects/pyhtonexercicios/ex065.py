resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma = soma + n
    quant = quant + 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n


    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print('Você digitou {} números e a média foi {}!'.format(n, media))
print('O menor número digitado foi {} e o maior foi {}'.format(menor, maior))
