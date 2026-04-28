from ideasense import IdeaSense
from time import sleep

idea = IdeaSense()

# Posición inicial (centro)
x = 2
y = 2

# Sensibilidad (más pequeño = más sensible)
th = 0.20

# Ganancia de movimiento (qué tanto se mueve por lectura)
gain = 0.8

def clamp(val, min_v, max_v):
    return max(min_v, min(max_v, val))

while True:
    ax, ay, az = idea.accel  # aceleración en X, Y, Z

    # Movimiento en X
    if ax < th:
        x += gain
    elif ax > -th:
        x -= gain

    # Movimiento en Y (invertido para que sea intuitivo)
    if ay < th:
        y -= gain
    elif ay > -th:
        y += gain

    # Convertir a entero
    x = int(round(x))
    y = int(round(y))

    # Limitar a la matriz (bordes)
    x = clamp(x, 0, 4)
    y = clamp(y, 0, 4)

    # Limpiar matriz
    idea.matrix.fill(0)

    # Dibujar gota
    idea.matrix[x, y] = 1
    idea.matrix.show()

    sleep(0.05)