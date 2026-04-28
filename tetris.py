from time import sleep
from ideasense import IdeaSense

idea = IdeaSense()

# Dimensiones
W = 5
H = 5

# Botones
BTN_A = 0  # izquierda
BTN_B = 1  # derecha
BTN_C = 2  # rotar

# Piezas simples
PIEZAS = [
    [[1, 1]],
    [[1], [1]],
    [[1, 1], [1, 0]],
    [[1, 1], [1, 1]],
    [[1, 1, 1]]
]

pieza_actual = 0
pieza = PIEZAS[pieza_actual]

x = 2
y = 0

tablero = [[0 for _ in range(W)] for _ in range(H)]


# =========================
# MATRIZ
# =========================
def limpiar_matriz():
    idea.matrix.fill(0)


def dibujar():
    limpiar_matriz()

    # tablero fijo
    for fila in range(H):
        for col in range(W):
            if tablero[fila][col] == 1:
                idea.matrix[col, fila] = 1

    # pieza actual
    for py in range(len(pieza)):
        for px in range(len(pieza[py])):
            if pieza[py][px] == 1:
                dx = x + px
                dy = y + py
                if 0 <= dx < W and 0 <= dy < H:
                    idea.matrix[dx, dy] = 1

    idea.matrix.show()


# =========================
# LOGICA
# =========================
def colision(nx, ny, p):
    for py in range(len(p)):
        for px in range(len(p[py])):
            if p[py][px] == 1:
                dx = nx + px
                dy = ny + py

                if dx < 0 or dx >= W:
                    return True

                if dy >= H:
                    return True

                if dy >= 0 and tablero[dy][dx] == 1:
                    return True
    return False


def fijar_pieza():
    global pieza, x, y, pieza_actual

    for py in range(len(pieza)):
        for px in range(len(pieza[py])):
            if pieza[py][px] == 1:
                dx = x + px
                dy = y + py
                if 0 <= dx < W and 0 <= dy < H:
                    tablero[dy][dx] = 1

    limpiar_lineas()

    pieza_actual = (pieza_actual + 1) % len(PIEZAS)
    pieza = PIEZAS[pieza_actual]
    x = 2
    y = 0

    if colision(x, y, pieza):
        reiniciar()


def limpiar_lineas():
    global tablero

    nuevo = []

    for fila in tablero:
        if sum(fila) < W:
            nuevo.append(fila)

    eliminadas = H - len(nuevo)

    for _ in range(eliminadas):
        nuevo.insert(0, [0]*W)

    tablero = nuevo


def rotar(p):
    nueva = []
    filas = len(p)
    cols = len(p[0])

    for c in range(cols):
        fila = []
        for f in range(filas-1, -1, -1):
            fila.append(p[f][c])
        nueva.append(fila)

    return nueva


def reiniciar():
    global tablero, pieza, pieza_actual, x, y

    for i in range(H):
        for j in range(W):
            tablero[i][j] = 0

    pieza_actual = 0
    pieza = PIEZAS[pieza_actual]
    x = 2
    y = 0

    # animación simple
    for _ in range(3):
        idea.matrix.fill(1)
        idea.matrix.show()
        sleep(0.2)

        idea.matrix.fill(0)
        idea.matrix.show()
        sleep(0.2)


# =========================
# LOOP
# =========================
contador = 0
velocidad = 8

while True:
    dibujar()

    botones = idea.pressed

    # izquierda
    if botones[BTN_A]:
        if not colision(x - 1, y, pieza):
            x -= 1

    # derecha
    if botones[BTN_B]:
        if not colision(x + 1, y, pieza):
            x += 1

    # rotar
    if botones[BTN_C]:
        pr = rotar(pieza)
        if not colision(x, y, pr):
            pieza = pr

    contador += 1

    if contador >= velocidad:
        contador = 0

        if not colision(x, y + 1, pieza):
            y += 1
        else:
            fijar_pieza()

    time.sleep(0.5)