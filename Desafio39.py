from datetime import date

nascimento = int(input('Qual o ano de seu nascimento?'))
atual = date.today().year
idade = atual - nascimento
print('Quem nascu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!!!')
elif idade < 18:
    print('Faltam {} anos para você se alistar'.format(18-(idade<18)))
elif idade>18:
    print('Se passaram {} anos do seu alistamento! Se já se alistou ignore, se não se alistou procure a unidade mais '
          'próxima para mais informações.'.format(idade-18))


