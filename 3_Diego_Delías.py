# 3) Realizar una función que despliegue un menú en pantalla y pida al usuario que seleccione una
# opción del menú. A la función se le pasa (como parámetro de la función) un diccionario donde la
# clave es el valor que debe devolver si se selecciona esa opción y el dato es el texto que debe
# mostrar el menú. La función debe devolver la clave de la opción seleccionada por el usuario.
# Por ejempo:
# def menu(diccionario):
# ….. #Completar el código de la función
# return key
# # Programa principal
# menu_principal={‘N’:’Nuevo’, ‘E’:’Editar’, ‘B’:’Borrar’,
# ‘S’:’Salir’}
# opción=menu(menú_principal)
# print(“Opción seleccionada:”,menu_principal[opción])

dic = {'N':'Nuevo', 'E':'Editar','B': 'Borrar', 'S': 'Salir' }
def funcionMenu( diccionario ):
    print("""Seleccione una de las siguientes opciones: """)
    for k , v in diccionario.items():
        print(k,v)
    opcion= input("Ingrese letra a la opción deseada  ")

   


    res = opcion if opcion.capitalize() in diccionario.keys() else "la opción ingresada es inexistente"

    return res.capitalize()
    



print(funcionMenu(dic))