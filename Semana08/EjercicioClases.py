import math

class Raices:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = self.__b**2 - 4*self.__a * self.__c

    def raiz1(self):
        x1 = (-self.__b + math.sqrt(self.__d)) / (2 * self.__a)
        return x1

    def raiz2(self):
        x2 = (-self.__b - math.sqrt(self.__d)) / (2 * self.__a)
        return x2
    
# Datos
a = 1
b = 0
c = -4
# Proceso
raices = Raices(a,b,c)
x1 = raices.raiz1()
x2 = raices.raiz2()
# Reporte
print("Raiz 1:",x1)
print("Raiz 2:",x2)

