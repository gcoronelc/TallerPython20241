# Delfor Dominguez Mendoza

intentos = 3

usuarios = {
    "Juan": 1253,
    "Enrrique": 1937,
    "Edgar": 1586
}


while intentos > 0:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios.keys() and usuarios[usuario] == int(contraseña):
        print("¡Inicio de sesión exitoso!")
        break
    else:
        print("Usuario o contraseña incorrectos.")
        intentos -= 1
        print("Te quedan", intentos, "intentos.")

if intentos == 0:
    print("Has excedido el número máximo de intentos. Por favor, inténtalo de nuevo más tarde.")