# def sumar(n1,n2): 
#     # Proceso
#     suma = n1 + n2
#     # Reporte
#     return suma

# print(sumar(6,7))


# --------------------------------------------------------


# x = None

# # Definición de una función que no retorna ningún valor explícito
# def funcion_sin_retorno():
#     print("Esta función no retorna nada")

# # Llamada a la función que no retorna ningún valor explícito
# resultado = funcion_sin_retorno()
# print(resultado)

# # Comparación para verificar si una variable es igual a None
# if x is None:
#     print("La variable x no tiene ningún valor asignado")


# --------------------------------------------------------

# def cal_renta_4ta( ingreso ):
#     pass

# print(cal_renta_4ta(5000.00))
# print(cal_renta_4ta(1400.00))


# --------------------------------------------------------

# def cal_renta_4ta( ingreso ):
#     # Proceso
#     if ingreso > 1500.00: 
#         renta = ingreso * 0.08
#     else: 
#         renta = 0.00
#     # Reporte
#     return renta

# def cal_renta_4ta( ingreso ):
#     # Proceso
#     renta = 0.00
#     if ingreso > 1500.00: 
#         renta = ingreso * 0.08       
#     # Reporte
#     return renta

# print(cal_renta_4ta(5000.00))
# print(cal_renta_4ta(1400.00))


# --------------------------------------------------------

# def saludar():
#     print("Hola todos!!")

# saludar()
# print(saludar())


# --------------------------------------------------------

# def saludar():
#     print("Hola todos!!")

# llama_funcion = saludar()
# llama_funcion


# --------------------------------------------------------

# def promedio_t1(n1, n2, n3):
#     return (n1+n2+n3)/3

# def promedio_t2(n1, n2, n3):
#     return (n1*2+n2+n3)/4

# def promedio_t3(n1, n2, n3):
#     return (n1+n2*2+n3)/4

# def promedio_t4(n1, n2, n3):
#     return (n1+n2+n3*2)/4

# n1 = 10
# n2 = 15
# n3 = 18
# ejecutar_sol = None
# caso = 5
# if caso==1: ejecutar_sol = promedio_t1(n1,n2,n3)
# elif caso==2: ejecutar_sol = promedio_t2(n1,n2,n3)
# elif caso==3: ejecutar_sol = promedio_t3(n1,n2,n3)
# elif caso==4: ejecutar_sol = promedio_t4(n1,n2,n3)

# print(ejecutar_sol)


# --------------------------------------------------------

# def saludar(nombre):
#     print("Hola",nombre)

# saludar("Gustavo")
# saludar("Nestor")


# --------------------------------------------------------


# def restar(n1,n2):
#     resta = n1 - n2
#     return resta;

# print(restar(n1=7,n2=3))
# print(restar(n2=3,n1=7))


# --------------------------------------------------------

# def restar(n1=50,n2=30):
#     resta = n1 - n2
#     return resta;

# print(restar(n1=7,n2=3))
# print(restar(n2=3,n1=7))
# print(restar(n2=10))
# print(restar())


# --------------------------------------------------------

# resta = 50
# def restar(n1,n2):
#     resta = n1 - n2
#     return resta

# print(restar(7,3))
# print(resta)


# --------------------------------------------------------

# resta = 50
# def restar(n1,n2):
#     global resta
#     resta = n1 - n2
#     return resta

# print(restar(7,3))
# print(resta)


# --------------------------------------------------------


# def sumar(lista):
#     suma = 0
#     for dato in lista:
#         suma += dato
#     return suma

# print( sumar([5,2,8]) )
# print( sumar([50,20,30,80]) )


# --------------------------------------------------------


# def suma_multiple(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado

# total = suma_multiple(1, 2, 3, 4, 5, 8)
# print(total)


# --------------------------------------------------------

# def mate(n1, n2):
#     suma = n1 + n2
#     resta = n1 - n2
#     return suma, resta

# print( mate(8,5) )

# a,b = mate(8,5)
# print("suma:",a)
# print("resta:",b)


n = 10
def algo(x):
    x += n
    return n

algo(67)