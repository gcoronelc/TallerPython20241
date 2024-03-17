# Datos
numero1= int(input("numero 1: "))
numero2 = int(input("numero 2: "))
operador = input("Operador (SRMD): ")
# Proceso
operacion = "Incorrecta"
resultado = ""
if operador in "sS":
    operacion = "Suma"
    resultado = numero1 + numero2

# Reporte
print("Operacion: ", operacion)
print("Resultado: ", resultado)
