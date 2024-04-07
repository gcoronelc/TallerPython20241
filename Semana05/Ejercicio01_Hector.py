# Hector Denilson Flores Reyes

#Datos
import random

def generar_lista():
    return [random.randint(1, 100) for _ in range(10)]

#Proceso
def sumar_listas(lista1, lista2):
    lista_suma = []
    for i in range(10):
        suma = lista1[i] + lista2[i]
        lista_suma.append(suma)
    return lista_suma

lista_uno = generar_lista()
lista_dos = generar_lista()
lista_tres = sumar_listas(lista_uno, lista_dos)

#Reporte
print("Lista uno:", lista_uno)
print("Lista dos:", lista_dos)
print("Lista tres (suma de lista uno y lista dos):", lista_tres)