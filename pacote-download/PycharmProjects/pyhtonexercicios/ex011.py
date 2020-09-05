lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
lap = lp * ap
print('Sua parede tem a dimensão de {} x {} e sua área é de {} metros quadrados.'.format(lp, ap, lap))
tinta = lap / 2
print('Para pintar essa parede, você precisará de {} l de tinta.'.format(tinta))

