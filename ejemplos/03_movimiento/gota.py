"""
Gota que rueda
==============

Un punto ("gota") se mueve por la matriz según la inclinación de la tarjeta,
como una gota de agua sobre una superficie.

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Inclinar la tarjeta.
Usa      : idea.accel, idea.matrix
Autoría  : Tomás de Camino Beck, Ph.D. — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, pegar este código y ejecutarlo (Ctrl+R) o
guardarlo como code.py en la tarjeta.
"""

from ideasense import IdeaSense
from time import sleep

idea = IdeaSense()

# Posición inicial (centro)
x = 2
y = 2

# Sensibilidad (más pequeño = más sensible)
th = 1.5   # m/s²; con 0.2 el ruido del sensor movía la gota

# Ganancia de movimiento (qué tanto se mueve por lectura)
gain = 0.8

def clamp(val, min_v, max_v):
    return max(min_v, min(max_v, val))

while True:
    ax, ay, az = idea.accel  # aceleración en X, Y, Z

    # Movimiento en X
    # (corregido: antes la gota nunca se quedaba quieta porque las dos
    #  condiciones cubrían todos los valores posibles de ax)
    if ax < -th:
        x += gain
    elif ax > th:
        x -= gain

    # Movimiento en Y (invertido para que sea intuitivo)
    if ay < -th:
        y -= gain
    elif ay > th:
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
