# cadena1 = "Esto es una cadena con comillas dobles" 
# cadena2 = 'Esto es otra cadena con comillas simples' 
# print(cadena1) 
# print(cadena2)


# parrafo = '''Esto es un ejemplo de una cadena multilínea. 
# Puede abarcar varias líneas sin necesidad de concatenar.''' 
# print(parrafo)




# parrafo = """Esto es otro ejemplo de una cadena multilínea. 
# Puedes comprobar como escribir varias líneas como una cadena.""" 
# print(parrafo)



# print("televisor \t"3000.0")
# print("lavadora \t2800.0")
# print("computador \t4300.0")



# cadena = "Esto es una comilla doble \" dentro de una cadena" 
# print( cadena )



# cadena = r"Esto es una cadena con \ncaracteres de escape." 
# print( cadena )



# ruta = r'c:\parent\tasks\new' 
# print(ruta)



# ruta = 'c:\\parent\\tasks\\new' 
# print(ruta)



# nombre = "Gustavo" 
# edad = 40 
# mensaje = "Hola, soy " + nombre + " y tengo " + str(edad) + " años." 
# print(mensaje)



# nombre = "Gustavo" 
# edad = 40 
# mensaje = f"Hola, me llamo {nombre} y tengo {edad} años." 
# print(mensaje)


# precio = 80.0
# cantidad = 5
# repo = f"Precio: {precio}"
# repo += f"\nCantidad: {cantidad}"
# repo += f"\nImporte: {precio*cantidad}"
# print(repo)




# cadena = "Hola, mundo" 
# longitud = len(cadena) 
# print(f"La longitud de la cadena es: {longitud}")


# cadena = "gUStaVo CorOnEl"
# print(cadena.upper())
# print(cadena.lower())
# print(cadena.capitalize())


# frase = "Python es genial, si es muy genial." 
# posicion = frase.find("Python") 
# if posicion != -1: 
# 	print(f"La subcadena 'genial' está en la posición {posicion}") 
# else: 
# 	print("La subcadena no se encontró")


# frase = "Python es genial, si es muy genial." 
# posicion = frase.find("genial",12) 
# if posicion == -1: 
# 	print("La subcadena no se encontró")
# else: 
#     print(f"La subcadena 'genial' está en la posición {posicion}") 



# mensaje1 = "Este mundo es un mundo de locos." 
# mensaje2 = mensaje1.replace("mundo", "amigo") 
# print(mensaje1) 
# print(mensaje2)




# direccion = "Calle Los Heroes 230, Lima" 
# partes = direccion.split(", ") 
# print(partes)




# datos = "Manzana,Naranja,Uva,Pera,Mango" 
# frutas = datos.split(",") 
# print(frutas)



nombre = "Gustavo" 
edad = 40 
mensaje = "Hola, me llamo {} y tengo {} años." 
mensaje = mensaje.format(nombre, edad) 
print(mensaje)



