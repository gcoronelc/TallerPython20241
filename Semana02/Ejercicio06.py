# Hector Denilson Flores Reyes
# Hay que revisar est solución

# Datos
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
numero3 = int(input("Número 3: "))
numero4 = int(input("Número 4: "))
numero5 = int(input("Número 5: "))

# Proceso
resultado = "Todos los numeros son iguales"

if numero1 > numero2 and numero3 and numero4 and numero5 :
    resultado = numero1

if numero2 > numero1 and numero3 and numero4 and numero5 :
    resultado = numero2

if numero3 > numero1 and numero2 and numero4 and numero5 :
    resultado = numero3

if numero4 > numero1 and numero2 and numero3 and numero5 :
    resultado = numero4

if numero5 > numero1 and numero2 and numero3 and numero4 :
    resultado = numero5

# Reporte
print("El numero mayor es: ",resultado)