"""
Íconos Space Invaders
=====================

Módulo con íconos 5x5 (invasores, ovni, nave, explosión) y la función
draw_icon(idea, icono). Se puede ejecutar directamente para ver una animación
o importarse desde otro programa (copiarlo a /lib o junto a code.py).

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Ninguno: la animación recorre los íconos.
Usa      : idea.matrix
Autoría  : Tomás de Camino Beck, Ph.D. — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, pegar este código y ejecutarlo (Ctrl+R) o
guardarlo como code.py en la tarjeta. Para importarlo desde otro
programa, guardarlo en la tarjeta como /lib/space_invaders.py.
"""

INVADER_1 = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
]

INVADER_2 = [
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
]

INVADER_3 = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
]

UFO = [
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
]

SHIP = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
]

EXPLOSION = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
]

ICONS = [
    INVADER_1,
    INVADER_2,
    INVADER_3,
    UFO,
    SHIP,
    EXPLOSION,
]


def draw_icon(idea, icon):
    """Dibuja un icono 5x5 en la matriz de IdeaSense."""
    idea.matrix.fill(0)

    for y in range(5):
        for x in range(5):
            idea.matrix[x, y] = icon[y][x]

    idea.matrix.show()

# -----------------------------------------------------------------
# Demostración: se ejecuta solo si este archivo es el programa
# principal (code.py). Si se importa desde otro programa, no corre.
# -----------------------------------------------------------------
if __name__ == "__main__":
    from ideasense import IdeaSense
    from time import sleep

    idea = IdeaSense()

    while True:
        for icon in ICONS:
            draw_icon(idea, icon)
            sleep(0.5)
