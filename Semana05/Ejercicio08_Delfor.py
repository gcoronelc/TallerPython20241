# Delfor Dominguez Mendoza

def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
def calcular_sumatoria(x, n):
    resultado = 0
    for i in range(n):
        numerador = x**(2*i + 1)
        denominador = factorial(2*i + 1)
        termino = numerador / denominador
        if i % 2 == 1:
            resultado -= termino
        else:
            resultado += termino
    return resultado
x = 5
n = 2
resultado = calcular_sumatoria(x, n)
print("El resultado de la sumatoria es:", resultado)