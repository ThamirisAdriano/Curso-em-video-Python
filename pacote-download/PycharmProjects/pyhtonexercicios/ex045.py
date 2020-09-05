from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
pc = randint (0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 11)
if pc == 0 :
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador ganha!')
    elif jogador == 2:
        print('Computador ganha!')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:
    if jogador == 0:
        print('Computador ganha')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador ganha')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if jogador == 0:
        print('Jogador ganha')
    elif jogador == 1:
        print('Computador ganha')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVÁLIDA')



