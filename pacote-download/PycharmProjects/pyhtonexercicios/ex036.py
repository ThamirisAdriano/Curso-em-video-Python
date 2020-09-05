casa = float(input('Qual é o valor do imóvel? R$ '))
sal = float(input('Qual é o salário do comprador? R$ '))
ano = int(input('Em quantos anos será pago o imóvel? '))
valor = casa / (ano * 12)
minimo = sal * 30/100
print('O valor mensal da prestação será de R$ {:.2f}.'.format(valor))
if valor <= minimo:
    print('Seu empréstimo foi APROVADO!')
else:
    print('Seu empréstimo foi NEGADO!!')





