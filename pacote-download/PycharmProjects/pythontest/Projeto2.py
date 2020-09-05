sim = nao = mulsim = homp = 0
for p in range (1,11):
    sexo = str(input('Qual o seu gênero? [F/M]: ')).upper().strip()[0]
    resp = str(input('Você gostou do novo produto lançado recentemente?[S/N]: ')).upper().strip()[0]
    if sexo == 'F' and resp == 'S':
        mulsim = mulsim + 1
    if resp == 'N':
         nao = nao + 1
    if resp == 'S':
        sim = sim +1
    if sexo == 'M'and resp == 'N':
        homp = homp + 1 * (1/10) *100
print(f'Número de pessoas que respondeu sim: {sim}')
print(f'Número de pessoas que respondeu não: {nao}')
print(f'Número de mulheres que responderam sim: {mulsim}')
print(f'Porcentagem de homens que responderam não: {homp:.1f}%')


