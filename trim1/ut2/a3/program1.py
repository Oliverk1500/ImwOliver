import sys

numeroprimo=int(sys.argv[1])

def es_primo(num):
  if num < 0:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
    return 'Error no es positivo'
  else:
    if num == 1 or num == 2:
      return 'Es primo'
    for i in range(2,num):  #un rango desde el dos hasta el numero que nosotros elijamos
      if num % i == 0:
        return 'No es primo'
      return 'Es primo'
        



print(es_primo(numeroprimo))
