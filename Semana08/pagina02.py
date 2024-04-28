# Ejemplo 1: Clase vacia

# class Drink:
#     None

# drink = Drink()
# print("Todo bien")



# Ejemplo 2: Clase con constructor sin parametro

# class Drink:
#     def __init__(self): 
#         self.name = "Gustavo"
#         self.edad = 50

# drink = Drink() 
# print(drink.name)
# print(drink.edad)


# Ejemplo 3: Constructor con parametros

# class Drink: 
#     lugar = "Lima" # Variables estaticas
#     def __init__(self, name): 
#         self.name = name
#     def setLugar(self,lugar):
#         Drink.lugar = lugar

# print(Drink.lugar)
# drink = Drink("Gustavo Coronel") 
# print(drink.name)
# drink.setLugar("Chiclayo")
# print(Drink.lugar)




# Ejemplo 4: Encapsulamiento

# class Drink: 
#     def __init__(self, name): 
#         self.__name = name 
#     def getDetail(self): 
#         return "La bebida es: " + self.__name 

# drink = Drink("Agua") 
# print(drink.__name)
# print(drink.getDetail())



#Ejemplo 5: Herencia

# class Drink: 

#     def __init__(self, name): 
#         self.__name = name 

#     def getDetail(self): 
#         return "La bebida es: " + self.__name


# class Beer(Drink): 

#     def __init__(self, name, brand, alcohol): 
#         super().__init__(name) 
#         self.__brand = brand 
#         self.__alcohol = alcohol 

# beer1 = Beer("Cerveza Trigo","Cristal",10.0) 
# print(beer1.getDetail())


# Ejemplo 7: Sobre-escritura

class Drink: 

    def __init__(self, name): 
        self.__name = name 

    def getDetail(self): 
        return "La bebida es: " + self.__name


class Beer(Drink): 

    def __init__(self, name, brand, alcohol): 
        super().__init__(name) 
        self.__brand = brand 
        self.__alcohol = alcohol 

    def getDetail(self):
        repo = super().getDetail()
        repo += "\nBrand: " + self.__brand
        repo += "\nAlcohol: " + str(self.__alcohol)
        return repo

beer1 = Beer("Cerveza Trigo","Cristal",10.0) 
print(beer1.getDetail())