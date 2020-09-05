nome = str(input('Qual é o seu nome?: '))
if nome == 'Thamiris':
    print('Você tem um lindo nome!')
elif nome =='Pedro'or nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
