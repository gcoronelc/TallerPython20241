# Variables
productos = []
precios = []

# Datos
for i in range(5):
    print(f"PRODUCTO: {i+1}")
    nom = input("Nombre: ")
    pre = float(input("Precio: "))
    productos.append(nom)
    precios.append(pre)

# Proceso
mayor_precio = max(precios)
mayor_precio_indice = precios.index(mayor_precio)
mayor_precio_nombre = productos[mayor_precio_indice]
menor_precio = min(precios)
menor_precio_indice = precios.index(menor_precio)
menor_precio_nombre = productos[menor_precio_indice]

# Reporte
print("DATOS")
print("Productos:",productos)
print("Precios:",precios)
print("PRODUCTO DE MAYOR PRECIO")
print(f"Nombre: {mayor_precio_nombre}")
print(f"Precio: {mayor_precio}")
print("PRODUCTO DE MENOR PRECIO")
print(f"Nombre: {menor_precio_nombre}")
print(f"Precio: {menor_precio}")




