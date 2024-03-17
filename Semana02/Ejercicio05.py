# Delfor Dominguez Mendoza
##---------Ejercicio 5
#Datos
numero1= int(input("numero1 "))
numero2 = int(input("numero2 "))
operador = input("Operador ")

#Proceso
result ="Operado no valido "
texto =""

if (operador.upper() == "S"):
 result = numero1 + numero2
 texto="la suma"

if (operador.upper() == "R"):
 result = numero1 - numero2
 texto="la resta"

if (operador.upper() == "M"):
 result = numero1 * numero2
 texto="la multiplicacion"

if (operador.upper() == "D"):
 result = numero1 / numero2
 texto="la division"

#Resul
#Resultado
mensaje = result if texto == "" else  f"El resultado de {texto} es: {result}."
print(mensaje )