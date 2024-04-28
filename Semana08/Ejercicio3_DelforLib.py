def cantidad_estudiantes(notas):
    return len(notas)

def nota_mayor(notas):
    return max(notas)

def nota_menor(notas):
    return min(notas)

def nota_mas_repetida(notas):
    return max(set(notas), key=notas.count)

def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_mediana(notas):
    notas_sorted = sorted(notas)
    n = len(notas_sorted)
    if n % 2 == 0:
        return (notas_sorted[n//2 - 1] + notas_sorted[n//2]) / 2
    else:
        return notas_sorted[n//2]