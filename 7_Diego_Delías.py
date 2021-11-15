# Realizar una función para imprimir un listado de productos. La función recibe una lista de tuplas
# conteniendo los datos de los productos a mostrar. Los datos son Marca, Modelo, Precio y Stock
# disponible.
# Por ejemplo:
Lista=[('Samsung', 'LA5890',12345,28),
('Samsung', 'LB001',2550,205),
('LG', 'GL-2552',25400,18)]

def imprimirListadoDeProductos(lista):
    print ("{:<15} {:<15} {:<10} {:<10} ".format('Marca','Modelo','Precio','Stock'))
    for producto in lista:
        print ("{:<15} {:<15} {:<10} {:<10} ".format(producto[0],producto[1],producto[2],producto[3]))
    
imprimirListadoDeProductos(Lista)

