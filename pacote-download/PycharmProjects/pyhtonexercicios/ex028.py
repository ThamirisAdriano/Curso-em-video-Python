from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar: ')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?: '))
print('PROCESSANDO... ')
sleep(3)
if jogador == pc:
    print('Parabéns, você acertou!')
else:
    print('Perdeu loser!!!Eu pensei no número {} e não no {}.'.format(pc, jogador))

