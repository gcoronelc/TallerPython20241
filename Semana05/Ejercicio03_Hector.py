# Hector

import random

# Funciones

def generar_numeros_aleatorios(n):
    return [random.randint(1, 100) for _ in range(n)]

def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        return numeros_ordenados[n//2]
    
# Datos

n = int(input("Ingrese cantidad de números: "))
numeros = generar_numeros_aleatorios(n)

#Proceso

media = calcular_media(numeros)
mediana = calcular_mediana(numeros)

#Resultados

print("Números generados aleatoriamente:", sorted(numeros))
print("Media:", media)
print("Mediana:", mediana)