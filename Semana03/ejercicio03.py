# Datos
while (True):
    n = int(input("n mayor que 3: "));
    if n>3: break
# Proceso
s = 0
for k in range(3,n+1):
    numerador = k - 1
    denominador = k * (k + 1)
    s += numerador / denominador
# Reporte
print("Suma:",s)


