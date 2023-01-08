import sys

#Creamos una funcion donde se recoge una sentencia dicha sentencia la sopara por palabras
#U recorre la lista para ver que palabras o letras se repiten para sumarlas a un contador.
def count_words(sentence):
    summary = {}
    lista = sentence.split()
    formatear = ''
    
    for i in lista:
        summary[i] = lista.count(i)
 
    for i in summary.keys():
        formatear += f'{i}: {summary[i]}\n'
    
    return formatear
        



sentence = sys.argv[1]
print(count_words(sentence))