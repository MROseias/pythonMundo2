r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))
if r1< r2+r3 and r2<r1+r3 and r3<r1 +r2:
    print('Os segmentos acime podem formar um triângulo', end='')
    if r1 ==r2== r3:
        print('Equilátero')
    elif r1!= r2 != r3 !=r1:
            print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo:')
