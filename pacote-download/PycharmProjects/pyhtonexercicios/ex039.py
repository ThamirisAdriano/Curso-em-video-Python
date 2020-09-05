from datetime import date
nascimento = int(input('Digite o ano do nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você deverá se alistar em imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano.'.format(ano))
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento deveria ter sido em {}.'.format(ano))
