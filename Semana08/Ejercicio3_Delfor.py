import Ejercicio3_DelforLib as func

notas = input("Ingrese las notas de los estudiantes separadas por coma: ")
notas_list = [int(nota) for nota in notas.split(",")]

print("Cantidad de estudiantes:", func.cantidad_estudiantes(notas_list))
print("Nota mayor:", func.nota_mayor(notas_list))
print("Nota menor:", func.nota_menor(notas_list))
print("Nota que más se repite:", func.nota_mas_repetida(notas_list))
print("Media:", func.calcular_media(notas_list))
print("Mediana:", func.calcular_mediana(notas_list))