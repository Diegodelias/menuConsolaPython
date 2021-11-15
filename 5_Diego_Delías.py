# 5) Realizar una función que permita el ingreso de una fecha (día, mes, año). La función debe devolver
# la fecha con el tipo de dato string en formato ISO 8601
from datetime import date
def ingresarFecha(dia,mes,anio):
    d = date(anio,mes,dia)
    return d.isoformat()


print(ingresarFecha(25,12,2018))