def soma (*valores): #desempacotamento
    s = 0
    for num in valores:
        s +=num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)