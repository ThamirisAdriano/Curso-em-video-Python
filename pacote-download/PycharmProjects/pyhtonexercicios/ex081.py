lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    cont = str(input('Quer continuar? S/N ')).upper()
    if cont == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescentesão {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi adicionado na lista')
print(sorted(lista))