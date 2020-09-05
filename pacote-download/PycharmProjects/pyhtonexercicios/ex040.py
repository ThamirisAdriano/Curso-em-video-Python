nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {}.'.format(nota1, nota2, media))
if media >=5 and media < 7:
    print('Recuperação!')
elif media <5:
    print('Reprovado!')
elif media >=7:
    print('Aprovado!')



