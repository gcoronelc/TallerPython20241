# t1 = (45,67,34)
# print(t1)
# print(t1[0])


# t1 = 45,67,34
# print(t1)
# print(t1[1])


# t1 = 45,
# print(t1)
# print(t1[0])


# t1 = (45,)
# print(t1)
# print(t1[0])


# Recorrido tipo coleccion
# t1 = (45,67,34)
# for it in t1:
#     print(it)


# Recorrido indexado
# t1 = (45,67,34)
# for i in range(0,len(t1)):
#     print(t1[i])


# tupla = (10, 20, 30, 40, 50)
# print(tupla)
# primero = tupla[0]
# segundo = tupla[1]
# tercero = tupla[-3]
# cuarto = tupla[-2]
# ultimo = tupla[-1]
# print(primero,segundo,tercero,cuarto,ultimo)


# tupla = (10, 20, 30, 40, 50)
# print(tupla)
# primero,segundo,tercero,cuarto,ultimo = tupla[0],tupla[1],tupla[-3],tupla[-2],tupla[-1]
# print(primero,segundo,tercero,cuarto,ultimo)


# tupla = (10, 20, 30, 40, 50)
# print(tupla)
# primero,segundo,tercero,cuarto,ultimo = tupla
# print(primero,segundo,tercero,cuarto,ultimo)


# tupla = (10, 20, 30, 76, 34, 23, 98, 47, 40, 50)
# print(tupla)
# primero,segundo,*_,ultimo = tupla
# print(primero,segundo,ultimo)


# tupla= [10,20,40,20,30,20]
# print(tupla.count(20))



# tupla = [10,20,40,20,30,20]
# print(tupla.index(20))


# tupla = [10,20,40,20,30,20]
# print(tupla.index(20,2))


# #desempaquetado de tuplas
# print("---------")
# #       0  1  2  3  4  5  6
# tupla=(78,12,25,78,56,94,78)
# print(tupla.count(12))
# print(tupla.index(78))
# print(tupla.index(78,1))
# print("---------")
# # por que sale 3

# Tuplas homogeneas
t1 = (76,34,89,23,45)
# Tupla heterogenea
t2 = ("Gustavo",8000,True,[15,18,12,16])
# Imprimir tuplas
print(t1)
print(t2)
t2[3].append(43)
t2[3].append(47)
t2[3][0] = 20
print(t2)

