# MARLON MORI ALVAREZ

#Datos
import random
N=int(input("Ingrese la cantidad de números: "))

l1=[]
l2=[]
l3=[]

#Proceso
for i in range(N):
    numero=random.randint(0,99)
    l1.append(numero)
    numero=random.randint(0,99)
    l2.append(numero)

for ele in l1:
    i = l2.count(ele)
    if i >= 1:
        l3.append(ele)

# Salida
print("Lista 1: ",l1)
print("lista 2: ",l2)
print("números que repiten: ",l3)