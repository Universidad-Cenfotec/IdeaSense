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
