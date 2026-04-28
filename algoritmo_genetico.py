import time
import random
from ideasense import IdeaSense
from ideaboard import IdeaBoard

# Inicialización
idea = IdeaSense()
ib = IdeaBoard()

# -----------------------------
# Parámetros del algoritmo
# -----------------------------
POP_SIZE = 20
MUTATION_RATE = 0.3

# -----------------------------
# Representación
# -----------------------------
def crear_individuo():
    # Cromosoma: 25 genes (5x5)
    return [random.randint(0, 1) for _ in range(25)]

def mostrar(individuo):
    idea.matrix.fill(0)
    for i, gen in enumerate(individuo):
        x = i % 5
        y = i // 5
        idea.matrix[x, y] = gen
    idea.matrix.show()

# -----------------------------
# Fitness
# -----------------------------
def fitness(individuo, luz):
    leds_encendidos = sum(individuo)

    # Normalizamos luz (ajustar según entorno)
    # idea.light viene del sensor :contentReference[oaicite:2]{index=2}
    luz_norm = min(luz / 1000, 1.0)

    # Queremos:
    # poca luz -> muchos LEDs
    # mucha luz -> pocos LEDs
    objetivo = int((1 - luz_norm) * 25)

    return -abs(leds_encendidos - objetivo)

# -----------------------------
# Selección
# -----------------------------
def seleccionar(poblacion, luz):
    poblacion.sort(key=lambda ind: fitness(ind, luz), reverse=True)
    return poblacion[:POP_SIZE // 2]

# -----------------------------
# Cruce
# -----------------------------
def cruzar(p1, p2):
    punto = random.randint(0, 24)
    return p1[:punto] + p2[punto:]

# -----------------------------
# Mutación
# -----------------------------
def mutar(ind):
    for i in range(len(ind)):
        if random.random() < MUTATION_RATE:
            ind[i] = 1 - ind[i]
    return ind

# -----------------------------
# Inicialización
# -----------------------------
poblacion = [crear_individuo() for _ in range(POP_SIZE)]

# -----------------------------
# Loop evolutivo
# -----------------------------
while True:

    luz = idea.light
    print("Luz:", luz)

    # Evaluar y seleccionar
    padres = seleccionar(poblacion, luz)

    # Nueva generación
    nueva_poblacion = padres.copy()

    while len(nueva_poblacion) < POP_SIZE:
        p1 = random.choice(padres)
        p2 = random.choice(padres)

        hijo = cruzar(p1, p2)
        hijo = mutar(hijo)

        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

    # Mostrar el mejor individuo
    mejor = max(poblacion, key=lambda ind: fitness(ind, luz))
    mostrar(mejor)

    print("Fitness:", fitness(mejor, luz))

    time.sleep(0.2)