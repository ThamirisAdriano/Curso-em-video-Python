print('{:=^40}'.format('Adriano Store'))
preço = float(input( 'Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
option = float(input('Qual é a opção?: '))
if option == 1:
    total = preço - (preço * (10/100))
    print('Sua compra de {}, vai sair por {} com desconto.'.format(preço, total))
elif option == 2:
    total = preço - (preço * (5/100))
    print('Sua compra de {} à vista no cartão sairá por {}.'.format(preço, total))
elif option == 3:
    total = preço / 2
    print('Sua compra de {} em duas vezes no cartão, sairá por {} mensais.'.format(preço, total))
elif option == 4:
    prest = int(input('Em quantas vezes será feita a sua compra?: '))
    total = preço + (preço * (20/100)) / prest
    print('Sua compra de {} em {} vezes ficará por {} mensais. '.format(preço, prest, total))


