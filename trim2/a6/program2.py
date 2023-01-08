
#Creamos funciones para pasarle un parametro por el diccionare y que registre todo lo que ponemos .

def show_contacts(phone_book):
    formatear = ''
    for i in phone_book.keys():
        formatear += f'{i}: {str(phone_book[i])}\n'
        
    return formatear

#La funcion añade el numero y el nombre al diccionaro y los pasa por el mismo.

def add_contact(phone_book,name,phone):
    phone_book[name] = phone
    
 
#Funcion que elimina del diccionario lo que le pongamos para eliminar.
def remove_contact(phone_book,name):
    if not phone_book.get(name):
        return 'Error - Nombre no exite'
    else:
        del phone_book[name]


#Funcion que crea y el menu del diccionario y crea todo el diccionario

def menu():
    phone_book = {
        "Alicia" : 645617432,
        "Manuel" : 691854321,
        "Pepe" : 676298911,
        "Zeben" : 699812345
        }
    while True:
        print('1.Mostrar lista de contactos.')
        print('2.Añadir contacto (nombre y teléfono).')
        print('3.Borrar contacto (nombre).')
        print('4.Salir.')
        option = int(input('Elige un número: '))
        if option == 1:
            print(show_contacts(phone_book))
        elif option == 2:
            name = input('Dame un nombre: ')

            if name in phone_book:
                print('Error - Nombre ya exite')
            else:
                phone = int(input('Dame un número de telefono: '))
                print(add_contact(phone_book,name,phone))
        elif option == 3:
            name = input('Dame un nombre: ')
            print(remove_contact(phone_book,name))
        elif option == 4:
            break
        else:
            print("Unknown option")




try:
    menu()
except:
    print('Error has realizado algo que no debias')