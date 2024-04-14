# venta = {
#     "cliente": "Gustavo",
#     "producto": "Laptop",
#     "precio": 3872.00,
#     "cantidad": 3
# }
# print(venta)


# venta = dict([
#     ("cliente", "Gustavo"),
#     ("producto", "Laptop"),
#     ("precio", 3872.00),
#     ("cantidad", 3)
# ])
# print(venta)


# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# print(venta)


# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# print("Cliente:",venta["cliente"])
# print("Cliente:",venta.get("producto"))
# print(f"Precio: {venta["precio"]}")
# print(f"Cantidad: {venta.get("cantidad")}")


# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# venta["cliente"] = "Marlon"
# venta["importe"] = venta["precio"] * venta["cantidad"]
# print("Cliente:",venta["cliente"])
# print("Cliente:",venta.get("producto"))
# print(f"Precio: {venta["precio"]}")
# print(f"Cantidad: {venta.get("cantidad")}")
# print(f"Importe: {venta.get("importe")}")


# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )


# for valor in venta.values():
#     print(valor)


# for clave in venta:
#     print( clave, "=>" ,venta[clave] )





# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# for clave, valor in venta.items():
#     print(f"{clave} => {valor}")




# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# venta.clear();
# print(venta)


# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# print(venta)
# print("producto:", venta.get("valor",0))



# venta = dict(
#     cliente = "Gustavo",
#     producto = "Laptop",
#     precio = 3872.00,
#     cantidad = 3
# )
# ls = venta.items()
# print(ls)
# print(list(ls))

# ventas = [
#     {
#         "cliente": "Gustavo",
#         "producto": "Laptop",
#         "precio": 3872.00,
#         "cantidad": 3
#     },
#     {
#         "cliente": "Claudia",
#         "producto": "Laptop",
#         "precio": 3872.00,
#         "cantidad": 3
#     }, 
#     {
#         "cliente": "Hugo",
#         "producto": "Laptop",
#         "precio": 3872.00,
#         "cantidad": 3
#     }    
# ]
# print( ventas )



ventas = {
    1:{
        "cliente": "Gustavo",
        "producto": "Laptop",
        "precio": 3872.00,
        "cantidad": 3
    },
    2:{
        "cliente": "Claudia",
        "producto": "Laptop",
        "precio": 3872.00,
        "cantidad": 3
    }, 
    3:{
        "cliente": "Hugo",
        "producto": "Laptop",
        "precio": 3872.00,
        "cantidad": 3
    }    
}
for i in ventas:
    print( i, " == ", ventas[i] )