# Datos
m = int(input("m: "))
n = int(input("n: "))
# Proceso
m1 = m
n1 = n
# Parte 1
if (m1>n1):
    auxi = m1
    m1 = n1
    n1 = auxi
# Parte 2
i = m1
reporte = ""
while(i <= n1):
    if (i%2 == 1):
        reporte += str(i) + " "
    i = i + 1
# Reporte
print("=========================")
print("m:",m)
print("n:",n)
print("Reporte:", reporte)