from time import sleep #feito sozinha :)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('Multiplicando {} por {} da {}.'.format(n1, n2, produto))
    elif opcao ==3:
        if n1 > n2:
            print('{} é maior do que {}.'.format(n1, n2))
        elif n1 < n2:
            print('{} é menor do que {}.'.format(n1, n2))
    elif opcao == 4:
        print('Digite novamente os valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando..')
    else:
        print('Opção inválida, tente novamente!')
    print('=-='*10)
    sleep(2)
print('Fim do programa, volte sempre!!')




