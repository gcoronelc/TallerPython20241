#Delfor Dominguez Mendoza

#Datos
notas = [] 
for i in range(5):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    notas.append(nota)

#Proceso
notas.sort(reverse=True)
mejores_notas = notas[:3]
promedio = sum(mejores_notas) / len(mejores_notas)

#Reporte
print("El promedio de las 3 mejores notas es:", promedio)