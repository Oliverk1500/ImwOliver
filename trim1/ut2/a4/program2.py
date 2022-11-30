import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

a=0
g=0
c=0
t=0

for i in sequence:
   if i == 'A':
    a = a+1 
   elif i == 'C':
    c = c+1
   elif i == 'G':
    g = g+1
   elif i == 'T':
    t = t+1
print(f'''Adenine:{a}
Guanine:{g}
Cytosine:{c}
Thymine:{t}''')