## Hector Denilson Flores Reyes

#Datos
cadena = input("Ingresa cadena de caracteres: ")

#Procedimiento
palabras = cadena.split()

primera_letra = "".join([palabra[0] for palabra in palabras])
mayusculas = " ".join([palabra.capitalize() for palabra in palabras])
palabras_con_A = [palabra for palabra in palabras if palabra.lower().startswith('a')]

#Resultado
print(f"La primera letra de cada palabra: {primera_letra}")
print(f"Cadena con la primera letra en mayúsculas: {mayusculas}")
print(f"Palabras que comienzan con la letra A: {', '.join(palabras_con_A)}")