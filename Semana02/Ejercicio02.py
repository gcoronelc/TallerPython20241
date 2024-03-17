#Datos
numero1 = int(input("Ingrese nota 1: "))
numero2 = int(input("Ingrese nota 2: "))
numero3 = int(input("Ingrese nota 3: "))
#Proceso
suma = numero1 + numero2 + numero3
promedio = suma / 3
estado = "Aprobado" if promedio>=14 else "Desaprobado"
#Resultado
print("Promedio: ", promedio)
print("Estado: ", estado)