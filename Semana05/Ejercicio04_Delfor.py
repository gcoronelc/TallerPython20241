# Delfor Dominguez Mendoza

import random

# Funciones

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [random.randint(10, 30) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def sumar_columnas(matriz):
    columnas = len(matriz[0])
    sumas = [0] * columnas
    for fila in matriz:
        for j in range(columnas):
            sumas[j] += fila[j]
    return sumas

# Datos
matriz = generar_matriz(4, 3)

# Proceso
sumas_columnas = sumar_columnas(matriz)

# Reporte
print("Matriz generada:")
for fila in matriz:
    print(fila)
print("\nSuma de cada columna:", sumas_columnas)