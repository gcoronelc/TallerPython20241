# # Datos
# num1 = 89
# num2 = 0
# # Proceso
# cociente = num1 / num2
# # Reporte
# print(f"Cociente: {cociente}")
# print("Fin del programa")

# -------------------------------------------

# # Datos
# num1 = 89
# num2 = 8
# # Proceso
# try:
#     cociente = num1 / num2
#     reporte = f"Cociente: {cociente}"
# except:
#     cociente = 0
#     reporte = "Error en ejecucion"
# # Reporte
# print(reporte)
# print("Fin del programa")



# -------------------------------------------

# Datos
num1 = 89
num2 = 0
# Proceso
try:
    cociente = num1 / num2
    reporte = f"Cociente: {cociente}"
except ZeroDivisionError:
    cociente = 0
    reporte = "No es posible dividir por cero."
# Reporte
print(reporte)
print("Fin del programa")