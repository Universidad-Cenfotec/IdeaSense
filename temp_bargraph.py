from ideasense import IdeaSense
from ideaboard import IdeaBoard
import time

idea = IdeaSense()
ib = IdeaBoard()

TEMP_MIN = 20
TEMP_MAX = 30

col = 0

# Buffer de la matriz (estado persistente)
grid = [[0 for _ in range(5)] for _ in range(5)]

def temp_to_height(temp):
    t = (temp - TEMP_MIN) / (TEMP_MAX - TEMP_MIN)
    t = max(0, min(1, t))
    return int(t * 5)

def draw():
    for x in range(5):
        for y in range(5):
            idea.matrix[x, y] = grid[y][x]  # ojo: grid es [fila][col]
    idea.matrix.show()

def shift_down():
    global grid
    # desplaza todo hacia abajo
    for y in range(4, 0, -1):
        grid[y] = grid[y-1][:]
    grid[0] = [0]*5  # fila superior se limpia

def shift_up():
    global grid
    # desplaza todo hacia arriba
    for y in range(0, 4):
        grid[y] = grid[y+1][:]
    grid[4] = [0]*5  # fila inferior se limpia

last_time = time.monotonic()

while True:
    now = time.monotonic()

    # ---- lectura de botones ----
    if idea.pressed[0]:  # Botón A
        shift_down()

    if idea.pressed[2]:  # Botón C
        shift_up()

    # ---- cada segundo: nueva barra ----
    if now - last_time >= 1:
        last_time = now

        temp = idea.temp
        h = temp_to_height(temp)

        print("Temp:", temp, "Altura:", h)

        # borrar columna actual
        for y in range(5):
            grid[y][col] = 0

        # dibujar nueva barra (desde abajo)
        for y in range(h):
            grid[4 - y][col] = 1

        col = (col + 1) % 5

    # ---- dibujar siempre ----
    draw()

    time.sleep(0.05)