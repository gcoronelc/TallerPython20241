# Delfor Dominguez Mendoza

productos = [
    {"nombre": "Laptop", "precio": 3674.89},
    {"nombre": "Teléfono", "precio": 1200},
    {"nombre": "Tablet", "precio": 600},
    {"nombre": "TV", "precio": 300},
    {"nombre": "Cámara", "precio": 700}
]

presupuesto = 2000

def comprar_canasta(productos, presupuesto):
    # Ordenar
    productos.sort(reverse=True,key=lambda x: x["precio"])
    costo_total = 0
    canasta = []
    #Buscar
    for producto in productos:
        if costo_total + producto["precio"] <= presupuesto:
            costo_total += producto["precio"]
            canasta.append(producto)
    #eliminamos
    while costo_total > presupuesto:
        producto_eliminado = canasta.pop()
        costo_total -= producto_eliminado["precio"]
    return canasta

canasta_optima = comprar_canasta(productos, presupuesto)

print("Productos en la canasta óptima:")
for producto in canasta_optima:
    print("Nombre:", producto["nombre"],"- Precio:", producto["precio"])

