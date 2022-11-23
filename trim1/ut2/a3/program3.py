import sys

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

def maxcomun(a,b):
    if a == 0 or b == 0:
        return 0
        
    while b != 0:
        numero = b
        b = a%b
        a = numero
    return a


if numero1 < 0 or numero2 < 0:
    print('No son numeros positivos')

print(maxcomun(numero1,numero2))