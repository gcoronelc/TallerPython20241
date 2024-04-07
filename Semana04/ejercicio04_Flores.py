# Hector Denilson Flores Reyes
import random

#Datos
tamaño = int(input("Ingrese el tamaño de las listas: "))


#Proceso
lista1 = lista = [random.randint(1, 50) for _ in range(tamaño)]
lista2 = lista = [random.randint(1, 50) for _ in range(tamaño)]

conjunto_lista1 = set(lista1)
conjunto_lista2 = set(lista2)
numeros_comunes = conjunto_lista1.intersection(conjunto_lista2)
resultado = list(numeros_comunes)

#Resultado
print("lista 1:", lista1)
print("Lista 2:", lista2)
print("Números comunes:", resultado)