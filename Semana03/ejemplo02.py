# Datos
m = int(input("m: "))
n = int(input("n: "))
# Proceso
# Parte 1
if (m>n):
    auxi = m
    m = n
    n = auxi
# Parte 2
i = m
reporte = ""
while(i <= n):
    if (i%2 == 1):
        reporte += str(i) + " "
    i = i + 1
# Reporte
print("Reporte:", reporte)