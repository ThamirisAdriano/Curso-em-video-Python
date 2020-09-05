medida = float(input('Uma medida em metros: '))
dm = medida*10
cm = medida*100
mm = medida*1000
dam = medida/10
hm = medida/100
km = medida/1000
print('A medida de {} metros corresponde a {}dm, {}cm, {}mm, {}dam, {}hm e {}km.'.format(medida, dm, cm, mm, dam, hm, km))

