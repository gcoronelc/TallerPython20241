import random
# Datos
n = 5
# Proceso
notas = ""
suma = 0
menor = 20 # Valor maximo de una nota
for i in range(1,n+1):
    nota = random.randint(0,20)
    suma += nota
    notas += f"{nota} "
    if menor > nota: menor = nota
suma -= menor
pr = suma / (n-1)
# Reporte
print(f"Notas: {notas}")
print(f"Suma: {suma}")
print(f"Promedio: {pr}")