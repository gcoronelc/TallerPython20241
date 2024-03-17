# Datos
nota = 13
# Proceso
if nota > 20.0 or nota < 0.0: estado = "Nota incorrecta"
elif nota >= 18.0: estado = "Excelente"
elif nota >= 14.0: estado = "Bueno"
elif nota >= 12.0: estado = "En proceso"
else: estado = "Desaprobado"
# Reporte
print("Nota: ", nota)
print("Estado: ", estado)