import random

def generar_individuo():
    return random.sample(range(8), 8)

def evaluar_aptitud(individuo):
    colisiones = 0
    for i in range(8):
        colisiones += sum([1 for j in range(i + 1, 8) if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == j - i])
    return colisiones

def seleccionar_padres(poblacion, num_padres):
    return [min(random.sample(poblacion, 3), key=lambda x: evaluar_aptitud(x)) for _ in range(num_padres)]

def recombinar(padre1, padre2):
    punto_corte = random.randint(1, 6)
    return padre1[:punto_corte] + padre2[punto_corte:]

def mutar(individuo):
    indice = random.randint(0, 7)
    nuevo_valor = random.randint(0, 7)
    individuo[indice] = nuevo_valor
    return individuo

def algoritmo_genetico():
    poblacion = [generar_individuo() for _ in range(100)]

    generacion = 0
    while True:
        aptitudes = [evaluar_aptitud(individuo) for individuo in poblacion]
        indice_mejor = aptitudes.index(min(aptitudes))
        mejor_individuo = poblacion[indice_mejor]

        if aptitudes[indice_mejor] == 0:
            return generacion, mejor_individuo

        padres = seleccionar_padres(poblacion, 20)

        descendencia = [recombinar(random.choice(padres), random.choice(padres)) for _ in range(80)]
        descendencia = [mutar(individuo) for individuo in descendencia]

        poblacion = padres + descendencia

        generacion += 1

generacion_encontrada, solucion = algoritmo_genetico()
print("Solución encontrada en la generación:", generacion_encontrada)
print("Solución encontrada:", solucion)


