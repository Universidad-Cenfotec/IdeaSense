# space_invaders.py
# Iconos 5x5 estilo Space Invaders para IdeaSense

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

"""
USAGE

from ideasense import IdeaSense
from space_invaders import ICONS, draw_icon
from time import sleep

idea = IdeaSense()

while True:
    for icon in ICONS:
        draw_icon(idea, icon)
        sleep(0.5)
"""
