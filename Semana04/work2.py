# l = [76,20,67]
# l.clear()
# print(l)

# l = [12,54,67]
# t = len(l*3)
# print(t)


# l = [76,20,67,43,560,28]
# l.sort()
# print(l)
# print("Minimo:",l[0])
# print("Maximo:",l[len(l)-1])
# print("Maximo:",l[-1])


# l = [10,20,30]
# l.reverse()
# print(l)


# Reto Ordenar una lista de enteros en forma descendente


# l = [32,54,67,89,23]
# l.sort()
# l.reverse()
# print(l)

# l = [76,20,67]
# print(l)
# l.append(54)
# l.append(89)
# print(l)


# l = [76,20,67]
# m = max(l)
# print(m)


# l = [76,20,67]
# m = min(l)
# print(m)


# l = [10,20,30]
# l.insert(1,40)
# l.insert(1,70)
# print(l)


# l = [76,20]
# l.extend([90,74])
# print(l)


# l1 = [76,20]
# l2 = [90,74]
# l3 = l1 
# l3.extend(l2)
# l1[0] = 100
# print(l1)
# print(l3)


# l = [76,20,67,87,20,90,20]
# i = l.index(20,2)
# print(i)


# l = [76,20,67,20,20]
# n = l.count(200)
# print(n)

# Reto
# Generar 2 listas de enteros => l1, l2
# Luego obtener la lista diferencia, l3 = l1 - l2
# Contiene los elementos de l1 que no estan en l2


# l1 = [23,45,87,45,76,90,27,43,45,98]
# l2 = [15,45,55,45,76,77,44,43,88,98]
# l3 = []
# for ele in l1:
#     i = l2.count(ele)
#     if i == 0:
#         l3.append(ele)
# print(l1)
# print(l2)
# print(l3)


# l1 = [76, 20, 67, 43, 560, 28, 20]
# l2 = [20, 67]
# l3 = [x for x in l1 if x not in l2]
# print(l3)



# l1 = [4,8,20,10]
# l2 = [4,20]
# setA = set(l1)
# setB = set(l2)
# l3 = list(setA - setB)
# print(l3)


# l = [76,20,67,20,20]
# x = l.pop(2)
# print(l)
# print(x)


# l = [76,20,67,20,20]
# x = l.pop()
# print(l)
# print(x)

# l = [76,20,67,20]
# c = l.copy()
# print(l)
# print(c)
# c[0]=100
# print(l)
# print(c)


# l = [76,20,67,20,20]
# l.remove(20)
# print(l)


mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener los primeros tres elementos
primeros_tres = mi_lista[:3]
print(primeros_tres)  # Output: [1, 2, 3]

# Obtener los elementos desde el índice 3 hasta el final
desde_tres_hasta_el_final = mi_lista[3:]
print(desde_tres_hasta_el_final)  # Output: [4, 5, 6, 7, 8, 9, 10]

# Obtener los elementos desde el índice 2 hasta el índice 7
desde_dos_hasta_siete = mi_lista[2:7]
print(desde_dos_hasta_siete)  # Output: [3, 4, 5, 6, 7]


# Obtener los elementos desde el índice 1 hasta el índice 8, con un paso de 2
con_paso_de_dos = mi_lista[1:8:2]
print(con_paso_de_dos)  # Output: [2, 4, 6, 8]


# Obtener una copia invertida de la lista
invertida = mi_lista[::-1]
print(invertida)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]