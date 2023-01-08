import sys

#Primera funcion recorre buscando las vocales de la frase que le ponemos al programa.
#Primero recorre el texto recogiendo las vocales y la cadena de texto y las cuenta para sumar +1 al contador.

def num_vowels(text):

    vocales = 'aAeEiIoOuU'
    contador = 0
    for i in text:
        for j in vocales:
            if i == j:
                contador +=1
    return contador

#Segunda funcion recorre todo el texto plano buscando espacios en blanco.
#Lo que hace es recorrer palabra por palabra para encontrar los huecos en blanco y sumar +1 al contador.

def num_whitespaces(text):
    
    contador = 0
    for i in text:
        if i == ' ':
            contador+=1
    return contador

#Tercera funcion es recorrer el texto plano en busca de numeros.
#Recorre todo el texto buscando los numero o digitos y le suma un +1 al contador.

def num_digits(text):
    
    contador = 0
    digitos = '0123456789'
    for i in text:
        for num in digitos:
            if i == num:
                contador += 1
    return contador

#Cuarta funcion recorre el texto plano en busca de palabras.
#Lo que hace es con un split reccore todo el texto en busca de palabras completas y lo añade en una lista para mostrarlo alfinal.

def num_words(text):
    
    lista = text.split(' ')
    return len(lista)

#Quinta funcion pone el texto alrevez-.

def reverse(text):
    return text[::-1]

#Sexta funcion lo que hace es calcular la longitud de la cadena de texto.

def length(text):
    return len(text)

# Sexta funcion recorre el texto partiendolo por la mitad y calcula la longitud maxima del texto.

def halfs(text):
    
    half = int(len(text) /2 )
    return f'{text[:half]} | {text[half:]}'

#Octaba funcion lo que hace es que las vocales minusculas se conviertan en vocales mayuculas.
#Recorre el texto y recoge todas las vocales que hay y las cambiar por mayusculas.

def upper_vowels(text):

    vocales = 'aeiou'
    palabras = ''
    for i in text:
        if i == vocales[0] or i == vocales[1] or i == vocales[2] or i == vocales[3] or i == vocales[4]:
            palabras += i.upper()
        else:
            palabras +=i
    return palabras

#Novena funcion lo que hace es recorrer el texto plano para ordneadr las plabras.

def sorted_by_words(text):
    
    lista = text.split(' ')
    ordenarpalabras = sorted(lista)
    encadenar = ''
    for i in ordenarpalabras:
        encadenar += ' ' + i
    return encadenar

#Decima Funcion lo que hace es recorrer el texto para saber cuanto mide cada palabra.
#Primero la convierte en espacios separados y despues recorre la lista para contar las longitud de las palabras.

def length_of_words(text):
    
    lista = text.split(' ')
    numero = ''
    for i in lista:
        numero += ' ' +str(len(i))
    return numero


if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))