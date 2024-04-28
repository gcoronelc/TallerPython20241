
class Mate:

    def __init__(self, num1=0, num2=0):
        self.__num2 = num2
        self.__num1 = num1

    def setNum1(self,num1):
        self.__num1 = num1

    def setNum2(self,num2):
        self.__num2 = num2

    def sumar(self):
        return self.__num1 + self.__num2  

# mate1 = Mate()
# print(mate1.sumar())

# mate1 = Mate(15)
# print(mate1.sumar())

# mate1 = Mate(15,13)
# print(mate1.sumar())

mate1 = Mate()
mate1.setNum1(50)
mate1.setNum2(60)
print(mate1.sumar())  
