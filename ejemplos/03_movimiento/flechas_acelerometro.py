"""
Flechas con el acelerómetro
===========================

Dibuja una flecha hacia el lado al que se inclina la tarjeta (ejes X e Y) y un
cuadro o una X cuando la tarjeta está boca arriba o boca abajo (eje Z).
Código generado originalmente con IdeaScratch.

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Inclinar la tarjeta. Umbral th = 1 m/s².
Usa      : idea.accel, idea.matrix
Autoría  : Tomás de Camino Beck, Ph.D. — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, pegar este código y ejecutarlo (Ctrl+R) o
guardarlo como code.py en la tarjeta.
"""

import board
from ideaboard import IdeaBoard
from time import sleep
import keypad

ib = IdeaBoard()
keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)

x = None
y = None
z = None

th = 1

from ideasense import IdeaSense
idea = IdeaSense()
while True:
  sleep(0.01)
  x = idea.accel[0]
  y = idea.accel[1]
  z = idea.accel[2]
  if x > th:
    _pat = [[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]
    for _r in range(5):
        for _c in range(5):
            idea.matrix[_c, _r] = _pat[_r][_c]
  elif x < -th:
    _pat = [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
    for _r in range(5):
        for _c in range(5):
            idea.matrix[_c, _r] = _pat[_r][_c]
  elif y > th:
    _pat = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
    for _r in range(5):
        for _c in range(5):
            idea.matrix[_c, _r] = _pat[_r][_c]
  elif y < -th:
    _pat = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
    for _r in range(5):
        for _c in range(5):
            idea.matrix[_c, _r] = _pat[_r][_c]
  elif z > th:
    _pat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    for _r in range(5):
        for _c in range(5):
            idea.matrix[_c, _r] = _pat[_r][_c]
  elif z < -th:
    _pat = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    for _r in range(5):
        for _c in range(5):
            idea.matrix[_c, _r] = _pat[_r][_c]
  sleep(0.1)
