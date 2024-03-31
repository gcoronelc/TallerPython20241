"""
lista1 = [32,54,23,67]
lista2 = lista1
lista2[2] = 100
print(lista1)
print(lista2)

x = 2
y = x
y += 1
print(x, y)
"""
"""
a = "Gustavo"
b = 50
lista = [a, b]
print(lista)
"""


"""
import random
lista = [random.randint(1,30),random.randint(1,30)]
print(lista)
"""

"""
lista0 = []
print(lista0)
lista1 = [45,87,23,45]
print(lista1)
lista2 = ["Chiclayo","Cuzco","Arequipa","Huancayo"]
print(lista2)
lista3 = [65,"Gustavo Coronel",76.34]
print(lista3)
lista4 = [43,67,23,[54,67,23,100]]
print(lista4)
print(lista4[3][2])
"""

"""
lista = [1,2,3,4,5,6,7,8,9,"Gustavo"]
for i in range(2,7):
    print(lista[i])
print("--------------------")
for j in lista:
    print(j)
"""

"""
lista = [43,67,23,[54,67,23,54]]
print("Elemento [0]: ",lista[0])
print("Elemento [3]: ",lista[3])
print("Elemento [3,1]: ",lista[3][1])
"""

"""
matriz = [
    [65,23,78,90],
    [12,98,34],
    [76,49,27,54,23,"Gustavo"]
]
print(matriz)
print(len(matriz))
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(matriz[f][c],end="\t")
    print("")
"""

ganador = "Python in cool\n"
print(ganador*5)
lista1 = [34,65,12]
lista2 = lista1 * 3
lista3 = lista1 + lista2
print(lista2)
print(lista3)



