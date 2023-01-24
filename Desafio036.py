valor = float(input('Qual o valor da casa ?'))
salário = float(input('O salário do comprador:'))
anos = int(input('Quantos anos de finaciamento ?'))
prestação = valor/(anos*12)
print('Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestação))
if prestação <= (salário*(30/100)):
    print ( 'Empréstimo pode ser concedido.')
else:
    print('Não foi concedido seu empréstimo.')




