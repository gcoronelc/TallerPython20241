# Delfor Dominguez Mendoza

# Funciones
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    longitud = len(numeros_ordenados)
    if longitud % 2 == 0:
        return (numeros_ordenados[longitud // 2 - 1] + numeros_ordenados[longitud // 2]) / 2
    else:
        return numeros_ordenados[longitud // 2]
    
# Datos

numeros = []
n = int(input("Ingrese la cantidad de números enteros positivos: "))

for i in range(n):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Proceso

media = calcular_media(numeros)
mediana = calcular_mediana(numeros)

# Reporte

print("Los números ingresados son:", numeros)
print("La media de los números es:", media)
print("La mediana de los números es:", mediana)