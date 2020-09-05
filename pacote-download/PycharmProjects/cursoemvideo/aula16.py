lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'batata frita')
#Tuplas são imutáveis
#lanche = [1] - comando errado.
for cont in range(0, len(lanche)):
   print(f' Eu vou comer {lanche[cont]} na posição {cont})'# quando precisa mostrar a posição

for comida in lanche:
   print(f'Eu vou comer {comida}')    #quando não é necessário mostrar a posição. Só funciona se colocar a de cima como comentário
print('Comi pa caramba!')

for pos, comida in enumerate(lanche): #outra forma de mostrar a posição
    print(f'Eu vou comer {comida} na posição {pos}')