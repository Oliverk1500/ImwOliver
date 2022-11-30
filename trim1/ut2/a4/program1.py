import sys

dni = int(sys.argv[1])

resto = dni % 23

text = 'TRWAGMYFPDXBNJZSQVHLCKE'

print(f'{dni}{text[resto]}')
