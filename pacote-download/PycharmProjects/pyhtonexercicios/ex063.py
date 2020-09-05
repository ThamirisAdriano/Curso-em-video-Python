print('=-'*30)
print('Sequência de FIBONACCI')
print('=-'*30)
termo = int(input('Quantos termos você quer mostrar?: '))
print('˜' * 20)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print('->{}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM!!')
