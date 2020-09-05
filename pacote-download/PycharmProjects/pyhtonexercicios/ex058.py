from random import randint
pc = randint(0,10)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi esse número? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais')
        else:
            print('Menos')
print('Acertou com tantos {} palpites!!'.format(palpite))

