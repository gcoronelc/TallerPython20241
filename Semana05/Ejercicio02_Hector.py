# Hector Denilson Flores Reyes

#Datos
import random
def generar_lista():
    return [random.randint(20, 50) for _ in range(10)]

#Proceso
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

lista_numeros = generar_lista()

num_pares, num_impares = contar_pares_impares(lista_numeros)


#Resultado
print("Lista de números generada:", lista_numeros)
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)