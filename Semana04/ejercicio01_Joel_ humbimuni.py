# DATOS
notas = []
i = 0

while(i < 5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    i = i + 1
    notas.append(nota)

notas.sort(reverse=True)

# PROCESO
promedio = sum(notas[:3]) / 3

# SALIDA
print("El promedio es:", promedio)