# Hector Denilson Flores Reyes

# Diccionario
usuarios = {
    "Jorge": "clave123",
    "Ana": "abc456",
    "Thiago": "xyz789"
}

# Funciones

def validar_login(usuario, clave, usuarios):
    if usuario in usuarios and usuarios[usuario] == clave:
        return True
    else:
        return False
# Proceso

intentos_maximos = 3

for intento in range(intentos_maximos):
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    clave_ingresada = input("Ingrese su contraseña: ")

    if validar_login(usuario_ingresado, clave_ingresada, usuarios):
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        intentos_restantes = intentos_maximos - (intento + 1)
        if intentos_restantes > 0:
            print(f"Le quedan {intentos_restantes} intentos.\n")
        else:
            print("Usuaario bloqueado, supero el máximo de intentos permitidos.")