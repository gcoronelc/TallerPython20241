# Delfor Dominguez Mendoza

import random
def generar_lista_enteros(longitud):
    return [random.randint(20, 50) for _ in range(longitud)]

def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = len(lista) - pares
    return pares, impares

lista_numeros = generar_lista_enteros(10)
num_pares, num_impares = contar_pares_impares(lista_numeros)

print("Lista de números enteros generada:", lista_numeros)
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)