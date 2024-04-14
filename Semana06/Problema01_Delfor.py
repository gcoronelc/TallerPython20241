# Delfor Dominguez Mendoza

# Datos

productos = [
    {"nombre": "Laptop", "costo": 2500, "precio": 3674.89},
    {"nombre": "Teléfono", "costo": 800, "precio": 1200},
    {"nombre": "Tablet", "costo": 400, "precio": 700},
    {"nombre": "TV", "costo": 1000, "precio": 5000},
    {"nombre": "TV-plasma", "costo": 1000, "precio": 5000},
    {"nombre": "Cámara", "costo": 300, "precio": 600}
]

# Proceso

margen_maximo = -float('inf')
productos_con_margen_maximo = []

for producto in productos:

    costo = producto["costo"]
    precio = producto["precio"]
    margen = precio - costo
    
    if margen > margen_maximo:
        margen_maximo = margen
        productos_con_margen_maximo = [producto] # Primer elemento
    elif margen == margen_maximo:
        productos_con_margen_maximo.append(producto)


# Reporte
        
print("Productos con el mayor margen de ganancia:")
for producto in productos_con_margen_maximo:
    print("- Nombre:", producto["nombre"])
    print("- Margen de ganancia:", margen_maximo)