from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual-nascimento
print('O atleta tem {} anos.'.format(idade))
if idade<=9:
    print('A classificação Infantil')
elif idade <=14:
    print('Classificação Mirim')
elif idade <=19:
    print('Classificação Júnior:')
elif idade <= 25:
    print('Classificação Sênior:')
elif idade>25:
    print('Classificão Master')

