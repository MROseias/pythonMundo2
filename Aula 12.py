nome = str(input('Qual é seu nome?'))
if nome == 'Oséias':
    print('Que nome bonito!')
    print('Tenha um bom dia, {}!'. format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')


