import sys

factor = int(sys.argv[1])



if factor < 0:
    print('No son numeros positivos')
else:
    unidad = 1
    for i in range(1,factor+1):
        unidad  *= i
        print(f'{i}! = {unidad}')

