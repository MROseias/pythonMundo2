n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2)/2
print('Sua média é {}'.format(media))
if 7 > media >= 5:
    print('O aluno está de recuperação.')
elif media < 5:
    print('O aluno está reprovado')
elif media >= 7:
    print('O aluno está aprovado')


