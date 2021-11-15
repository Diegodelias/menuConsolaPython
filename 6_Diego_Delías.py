# 6) Realizar una función para imprimir los datos de un producto. La función recibe una lista con los
# datos, y debe imprimirlos en pantalla. Los datos son Marca, Modelo, Precio y Stock disponible.
# Por ejemplo:
# Producto=[“Samsung”, “LA5890”,12345,128]






Producto=['Samsung', 'LA5890',12345,128]



def datosDeProducto(lista):
    print ("{:<15} {:<15} {:<10} {:<10} ".format('Marca','Modelo','Precio','Stock'))
    print ("{:<15} {:<15} {:<10} {:<10}".format(Producto[0], Producto[1], Producto[2], Producto[3]))
    

datosDeProducto(Producto)