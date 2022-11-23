import sys

num_entero = int(sys.argv[1])

def entero(num):
  if num < 0:
    return 'Error no es positivo'
  else:
    resultado = 0
    for i in range(1,num+1):
        resultado += i**2
    return resultado




print(entero(num_entero))