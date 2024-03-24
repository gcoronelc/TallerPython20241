# Datos
m = int(input("Valor de m: "))
n = int(input("Valor de n: "))
# Proceso
s = 0
cont= 0
for i in range(m,n+1):
    if i%5 != 0: continue
    s += i
# Reporte
print("Suma:",s)