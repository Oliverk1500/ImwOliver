import sys

numk = int(sys.argv[1])
cadena1=(sys.argv[2])

cadena1= cadena1.split(' ')

count=0

for i in cadena1:
   if numk == len(i):

       count+=1

print(f'Hay {count} palabras de tamaño {numk}')
