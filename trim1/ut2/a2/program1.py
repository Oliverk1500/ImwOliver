import sys
import math

a = float(sys.argv[1])

b = float(sys.argv[2])

c = float(sys.argv[3])

if a == 0:
    print(-c / b, )

elif b**2-4*a*c<0:
    print('No tiene solucion real.')

else:
    x1 = (-b+(math.sqrt(b**2-4*a*c))) // 2*a
    x2 = (-b-(math.sqrt(b**2-4*a*c))) // 2*a
    print(f'x1={int(x1)}; x2={int(x2)}')

