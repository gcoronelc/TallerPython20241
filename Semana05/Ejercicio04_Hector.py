# Hector Denilson Flores Reyes

import random

#Funciones

def generar_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(10, 30) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def calcular_suma_columnas(matriz):
    sumas = [0] * len(matriz[0])
    for fila in matriz:
        for i, valor in enumerate(fila):
            sumas[i] += valor
    return sumas

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Datos
matriz = generar_matriz(4, 3)

# Proceso
suma_columnas = calcular_suma_columnas(matriz)

#Resultado
print("Matriz:")
mostrar_matriz(matriz)
print("Suma")
print(suma_columnas)