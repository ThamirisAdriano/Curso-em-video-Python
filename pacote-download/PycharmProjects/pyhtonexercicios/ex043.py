peso = float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está na faixa de peso ideal.')
elif imc > 25 and imc <30:
    print('Sobrepeso')
elif imc >30 and imc < 40:
    print('Obesidade')
elif imc >40:
    print('Obesidade mórbida')



