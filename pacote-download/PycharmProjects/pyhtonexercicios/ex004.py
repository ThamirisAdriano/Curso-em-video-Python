a = input('\033[7;5;45m Digite algo: ')
print('Só tem espaços?',(a.isspace()))
print('É somente números?',(a.isnumeric()))
print('É alfabético?',(a.isalpha()))
print('É alfanumérico?'.format,(a.isalnum()))
print('Está em maiúsculas?',(a.isupper()))
print('Está em minúsculas?',(a.islower()))
print('Está capitalizado?',(a.istitle()))