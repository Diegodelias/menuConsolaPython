# 1) Realizar el programa que despliegue un menú en pantalla y pida al usuario que seleccione una
# opción del menú. Si la opción es válida, informa la opción seleccionada, Si la opción es invalida, pide
# que la ingrese nuevamente. Las opciones del menú son: Nuevo, Editar, Borrar y Salir.
seguir = True
opcion = input("""
Seleccione una de las siguientes opciones (ingresar número de la opción):
[1] Nuevo
[2] Editar
[3] Borrar
[4] Salir
""")

while seguir == True:
    if opcion == str(1):
        print("La opción elegida es la opción 1 Nuevo")
        seguir = False
    elif opcion == str(2):
        print("La opción elegida es la opción 2 Editar")
        seguir = False
    elif opcion == str(3):
        print("La opción elegida es la opción 3 Borrar")
        seguir = False
    elif opcion == str(4):
        print("La opción elegida es la opción 4 Salir")
        seguir = False

    else:
        opcion = input("""
La opción ingresada no es válida
Seleccione una de las siguientes opciones  (ingresar número de la opción):
[1] Nuevo
[2] Editar
[3] Borrar
[4] Salir
""")

