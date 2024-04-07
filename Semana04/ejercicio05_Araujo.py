# Luiggi Andreu Ivan Araujo Su�rez
import random
#Datos
#Lista de numeros aleatorios de 1-100
n_entero = [random.randint(1, 100) for _ in range(5)]
#Valor maximo y minimo
maximo = max(n_entero)
minimo = min(n_entero)
#eliminamos esos valosres 
n_entero.remove(maximo)
n_entero.remove(minimo)
#Promedio de los numeros restantes 3
promedio = sum(n_entero) / len(n_entero)
#Reporte
print(f"Lista: {n_entero}")
print(f"Valor maximo eliminado: {maximo}")
print(f"valor minimo eliminado: {minimo}")
print(f"Promedio de la lista: {promedio:.2f}")