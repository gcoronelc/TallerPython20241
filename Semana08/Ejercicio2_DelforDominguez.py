# Delfor Dominguez Mendoza

from datetime import datetime

# Proceso
def es_fecha_valida(fecha_str):
    try:
        datetime.strptime(fecha_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    

# Datos
fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/yyyy: ")
 
if es_fecha_valida(fecha_nacimiento):
    dia, mes, anio = fecha_nacimiento.split('/')

    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)
    
else:
    print("La fecha ingresada no es válida.")