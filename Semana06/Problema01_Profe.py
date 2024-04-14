# Datos

productos = [
    {"nombre": "Laptop", "costo": 2500, "precio": 3674.89},
    {"nombre": "Teléfono", "costo": 800, "precio": 1200},
    {"nombre": "Tablet", "costo": 400, "precio": 700},
    {"nombre": "TV", "costo": 1000, "precio": 5000},
    {"nombre": "TV-plasma", "costo": 1000, "precio": 5000},
    {"nombre": "Cámara", "costo": 300, "precio": 600}
]

# Calcular el margen

for o in productos:
    o["margen"] = o["precio"] - o["costo"]

print(productos)

# margen maximo

margen_maximo = productos[0]["margen"]
for i in range(1,len(productos)):
    if productos[i]["margen"] > margen_maximo:
        margen_maximo = productos[i]["margen"]

print(margen_maximo)

# Encontrar los productos

lista_final = []
for o in productos:
    if o["margen"] == margen_maximo:
        lista_final.append(o)

# Reporte

print(lista_final)
