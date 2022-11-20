import sys

try:
    
    nota = float(sys.argv[1])


    if nota >= 0 and nota <= 10:
        if nota == 10:
            print('Matrícula de honor')
      
        elif nota >= 9:
            print('Sobresaliente')
      
        elif nota >= 7:
            print('Notable')
      
        elif nota >= 5:
            print('Aprobado')
      
        else:
            print('Suspenso')
    else:
        print('Error')
        
except:
    print("No has puesto ningun argumento")