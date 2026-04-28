import time
from ideasense import IdeaSense
from ideaboard import IdeaBoard

# Inicializar hardware
idea = IdeaSense()
ib = IdeaBoard()

# Tabla de estados
tfs = [180, 45, 39, 156, 54, 198, 177, 147, 27, 135, 99, 201, 228, 30, 210, 108,
       225, 141, 78, 75, 120, 216, 57, 114, 135, 108, 78, 225, 210, 198, 156, 216,
       27, 39, 75, 141, 45, 30, 54, 177, 114, 57, 99, 120, 201, 147, 180, 228,
       78, 39, 120, 108]

# Estado
z = 0
inp = [0, 0]  # [A, C]

# -------------------------
# Output seguro (sin errores)
# -------------------------
def get_output():
    val = tfs[z]
    idx = inp[0]*2 + inp[1]

    if idx == 0:   # 00 → bits 7,6
        b1 = (val >> 7) & 1
        b2 = (val >> 6) & 1

    elif idx == 1: # 01 → bits 5,4
        b1 = (val >> 5) & 1
        b2 = (val >> 4) & 1

    elif idx == 2: # 10 → bits 3,2
        b1 = (val >> 3) & 1
        b2 = (val >> 2) & 1

    else:          # 11 → bits 1,0
        b1 = (val >> 1) & 1
        b2 = (val >> 0) & 1

    return b1, b2


# -------------------------
# Dibujar lámparas grandes
# -------------------------
def dibujar(l1, l2):
    idea.matrix.fill(0)

    # Lámpara izquierda (columnas 0-1)
    if l1:
        for x in [0, 1]:
            for y in [0,1]:
                idea.matrix[x, y] = 1

    # Lámpara derecha (columnas 3-4)
    if l2:
        for x in [3, 4]:
            for y in [0,1]:
                idea.matrix[x, y] = 1

    # Estado interno (columna central)
    idea.matrix[2, z % 5] = 1

    idea.matrix.show()


# -------------------------
# Avanzar estado
# -------------------------
def next_state():
    global z
    z = (z + 1) % len(tfs)


# -------------------------
# Loop principal (no bloqueante)
# -------------------------
last_update = time.monotonic()
interval = 0.02  # control visual (~20 ms)

while True:

    now = time.monotonic()

    # Leer botones
    event = idea.events.get()

    if event and event.pressed:

        # Botón A (0)
        if event.key_number == 0:
            inp[0] ^= 1
            next_state()

        # Botón C (2)
        elif event.key_number == 2:
            inp[1] ^= 1
            next_state()

        # Feedback visual
        ib.pixel = (0, 50, 0)

    else:
        ib.pixel = (0, 0, 0)

    # Actualización controlada
    if now - last_update >= interval:
        last_update = now

        l1, l2 = get_output()
        dibujar(l1, l2)

        # Debug
        print("z:", z, "inp:", inp, "out:", l1, l2)