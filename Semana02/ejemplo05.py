# Datos
nota = 190
# Proceso
estado = "Nota incorrecta"
estado = "Desaprobado" if nota < 12.0 else estado
estado = "En proceso" if nota >= 12.0 and nota < 14.0 else estado
estado = "Bueno" if nota >= 14.0 and nota < 18.0 else estado
estado = "Excelente" if nota >= 18.0 and nota <= 20.0 else estado
# Reporte
print("Nota: ", nota)
print("Estado: ", estado)