from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint (0,10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR ')
    if tipo == 'P':
        if total % 2 ==0:
            print('Você venceu!!!')
            v = v + 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if total %2 ==1:
            print('Você venceu!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER, você venceu {v} vezes.')
