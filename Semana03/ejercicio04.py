# Datos
nb10 = int(input("n: "))
# Proceso
nb16 = ""
while True:
    resto = nb10 % 16    
    nb10 = nb10 // 16
    if resto<10:
        nb16 = str(resto) + nb16
    elif resto==10:
        nb16 = "A" + nb16
    elif resto==11:
        nb16 = "B" + nb16
    elif resto==12:
        nb16 = "C" + nb16
    elif resto==13:
        nb16 = "D" + nb16
    elif resto==14:
        nb16 = "E" + nb16
    else:
        nb16 = "F" + nb16
    if(nb10==0): break
# Reporte
print(nb16)