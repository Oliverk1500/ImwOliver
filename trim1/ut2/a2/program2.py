import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])

x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

x3 = float(sys.argv[5])
y3 = float(sys.argv[6])



d1=math.sqrt((x1-x3)**2+(y1*y2)**2)   
d2=math.sqrt((x1-x3)**2+(y1*y2)**2)

if d1 < d2:
    print()

if d1 < d2:
    print(f'El punto mas cercano es ({int(x2)},{int(y2)}) y esta a una distacia de {d1}')

else:
    print(f'El punto mas cercano es({int(x2)},{int(y3)} y esta a una distacia de {d2}')