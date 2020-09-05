velocidade = float(input('Qual a velocidade atual do carro?: '))
if velocidade >= 80:
    print('MULTADO, você excedeu o limite que é 80Km/H')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de: {:.2f}.'.format(multa))
print('Tenha um bom dia, dirija com segurança')
