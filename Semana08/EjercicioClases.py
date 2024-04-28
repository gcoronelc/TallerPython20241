import math

class Raices:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def raiz1(self):
        d = self.__b**2 - 4*self.__a * self.__c
        x1 = (-self.__b + math.sqrt(d)) / (2 * self.__a)
        return x1

    def raiz2(self):
        d = self.__b**2 - 4*self.__a * self.__c
        x2 = (-self.__b - math.sqrt(d)) / (2 * self.__a)
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

