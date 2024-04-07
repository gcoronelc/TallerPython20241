# Delfor Dominguez Mendoza
from collections import Counter
import random

#Datos
N = int(input("Ingrese la cantidad de números a generar: "))

numeros = []
for i in range(N):
    numero = random.randint(20, 40)
    numeros.append(numero)

#Proceso
media = sum(numeros) / N

contador = Counter(numeros)
moda = contador.most_common(1)[0][0]

#Reporte
print("Números generados:", numeros)
print("Media:", media)
print("Moda:", moda)