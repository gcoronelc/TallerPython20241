#Datos
palabra = input("Ingrese una palabra: ")

# Proceso
contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palabra:
    if letra.lower() in contador_vocales:
        contador_vocales[letra.lower()] += 1

reporte = ""
for vocal, frecuencia in contador_vocales.items():
    reporte += f"{vocal}: {frecuencia}\n"


# Reporte
print("Frecuencia de las vocales:")
print(reporte)