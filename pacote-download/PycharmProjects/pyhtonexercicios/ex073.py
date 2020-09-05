times = ('Fla', 'Stos', 'Pal', 'Gre', 'Atl', 'SP', 'Inter', 'Cor', 'Fort', 'Goi', 'BA', 'Vco','Atle MG',
         'Flu', 'Bot', 'CE', 'Cru', 'CSA', 'Chape', 'Hava')
print(f'Lista de times: {times}')
print(f'Os cinco primeiros colocados do Brasileirão 2019 foram {times[0:5]}')
print('-='*30)
print(f'Os últimos quatro colocados : {times[-4:]}')
print('-='*30)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Chapecoense está na {times.index("Chape")+1}ª posição')


