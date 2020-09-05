distância = float(input('Qual a distância da sua viagem?'))
print('Você está prestes a iniciar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preco = distância * 0.50
else:
    preco = distância * 0.45
print('E o preço da sua passagem será: {}.'.format(preco))
