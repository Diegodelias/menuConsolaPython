# 2) Realizar una función que despliegue un menú en pantalla y pida al usuario que seleccione una
# opción del menú, la función debe devolver un código de la opción seleccionada (puede ser un
# carácter con la inicial de la opción seleccionada, o un entero de la opción seleccionada). Las
# opciones del menú son: Nuevo, Editar, Borrar y Salir.

def funcionMenu():
     
    opcion = input("""
Seleccione una de las siguientes opciones (ingresar número de la opción):
[1] Nuevo
[2] Editar
[3] Borrar
[4] Salir
""")
    if opcion == str(1):
        respuesta = 1
    elif opcion == str(2):
        respuesta = 2
    elif opcion == str(3):
        respuesta = 3
    elif opcion == str(4):
         respuesta = 4

    return respuesta




print(funcionMenu())