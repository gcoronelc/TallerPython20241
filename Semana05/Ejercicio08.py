# Funciones

def pot(base,exponente):
    p = 1
    for i in range(0,exponente):
        p *= base
    return p

def fac( n ):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def calc_serie(x,n):
    serie = 0
    signo = -1
    for i in range(1,n+1):
        signo *= -1
        np = i*2 - 1
        numerador = pot(x,np)
        denominador = fac(np)
        termino = signo * numerador / denominador
        serie += termino
    return serie

# Datos
x = 5
n = 2

# Proceso
serie = calc_serie(x,n)

# Reporte
print(serie)