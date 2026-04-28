import board
from ideaboard import IdeaBoard
from time import sleep
from ideasense import IdeaSense
import math

ib = IdeaBoard()
idea = IdeaSense()

# --- parámetros ---
th = 0.12        # zona muerta (evita ruido)
scale = 3.0      # cuánto se amplifica la flecha
center = (2, 2)  # centro de la matriz 5x5

# --- función para limpiar matriz ---
def clear():
    for r in range(5):
        for c in range(5):
            idea.matrix[c, r] = 0

# --- dibujar punto seguro ---
def set_pixel(x, y):
    if 0 <= x < 5 and 0 <= y < 5:
        idea.matrix[x, y] = 1

# --- dibujar línea simple (Bresenham simplificado) ---
def draw_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = max(abs(dx), abs(dy))
    if steps == 0:
        set_pixel(x0, y0)
        return

    for i in range(steps + 1):
        x = int(round(x0 + dx * i / steps))
        y = int(round(y0 + dy * i / steps))
        set_pixel(x, y)

# --- calibración inicial ---
print("Calibrando...")
sleep(1)
offset_x, offset_y, offset_z = idea.accel
print("Offset:", offset_x, offset_y, offset_z)

while True:
    sleep(0.05)

    ax, ay, az = idea.accel

    # quitar offset
    x = ax - offset_x
    y = ay - offset_y

    # vector de corrección (invertido)
    vx = -x
    vy = -y

    mag = math.sqrt(vx*vx + vy*vy)

    clear()

    # si está casi estable, solo punto central
    if mag < th:
        set_pixel(center[0], center[1])
        continue

    # normalizar
    vx /= mag
    vy /= mag

    # escalar a la matriz
    end_x = int(round(center[0] + vx * scale))
    end_y = int(round(center[1] + vy * scale))

    # dibujar flecha (línea desde el centro)
    draw_line(center[0], center[1], end_x, end_y)

    # opcional: cabeza de flecha simple
    set_pixel(end_x, end_y)
