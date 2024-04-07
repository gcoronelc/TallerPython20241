#Delfor Dominguez Mendoza

import random

def generar_lista_enteros(longitud):
    return [random.randint(1, 100) for _ in range(longitud)]

def sumar_listas(lista1, lista2):
    return [lista1[i] + lista2[i] for i in range(len(lista1))]

lista1 = generar_lista_enteros(10)
lista2 = generar_lista_enteros(10)
lista_suma = sumar_listas(lista1, lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista suma:", lista_suma)