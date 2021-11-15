# 4) Realizar una función que permita el ingreso de los datos de un cliente (Nombre de la empresa,
# Nombre del contacto y email). La función devuelve una Tupla con dichos datos en el orden
# indicado.

def ingresarDatosCliente(nombreEmpresa,nombreContacto,email):
    respuesta= (nombreEmpresa,nombreContacto,email)
    return respuesta


print(ingresarDatosCliente('Acme','Coyote','coyote@gmail.com'))
