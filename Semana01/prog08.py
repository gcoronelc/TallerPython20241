import datetime
# Datos
nombre = input("Nombre: ")
anio_nac = int(input("Año de nacimiento: "))
# Proceso
anio_actual = datetime.datetime.now().year
edad = anio_actual - anio_nac
# Salida
print("La edad de ",nombre," es ", edad)
