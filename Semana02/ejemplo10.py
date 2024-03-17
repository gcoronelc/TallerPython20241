# Operador Morsa

import random

#variable = random.randint(1,10) 

#if variable > 5:
#    print(f"El número {variable} es mayor a 5")
#else:
#    print(f"El número {variable} es menor a 5")

if (variable := random.randint(1,10)) > 5:
    print(f"El resultado de la {variable} es mayor a 5")
else:
    print(f"El número {variable} es menor a 5")