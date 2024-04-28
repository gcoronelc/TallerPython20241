# MARLON MORI ALVAREZ

def contar_palabras(linea):
    palabras=linea.split()
    num_palabras=len(palabras)
    print(palabras)
    return num_palabras

linea_1="Esta   es un ejemplo para calcular la cantidad de palabras en una oración"

resultado=contar_palabras(linea_1)
print(f"El número de palabras es: {resultado}")