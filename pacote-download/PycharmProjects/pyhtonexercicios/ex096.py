def area (larg, comp):
    a = larg * comp
    print(f' A área de um terreno com a largura {larg} e comprimento {comp} é igual a {a}m2')


print('CONTROLE DE TERRENOS')
print('-'* 20)
l = float(input('Largura (m):'))
c = float(input('Comprimento (m): '))
area(l, c)