"""
Interfaz táctil
===============

Usa el pin IO4 como sensor capacitivo: al tocarlo se dibuja una X y el LED
se pone azul; en reposo se muestra un punto central.

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Tocar el pin IO4 (o un cable/papel aluminio conectado a él).
Usa      : touchio.TouchIn, idea.matrix, ib.pixel
Autoría  : Fiorella Pérez — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, pegar este código y ejecutarlo (Ctrl+R) o
guardarlo como code.py en la tarjeta.
"""

import board
import touchio
import time
from ideaboard import IdeaBoard
from ideasense import IdeaSense

# Inicializamos ambas placas
ib = IdeaBoard()
idea = IdeaSense()

# Configuramos nuestro sensor capacitivo en el pin IO4
pin_tactil = touchio.TouchIn(board.IO4)

print("--- Interfaz Táctil Visual ---")
print("Toca el pin IO4 para alterar la matriz.")

while True:
    # La propiedad .value hace exactamente lo que explicaba tu código:
    # Compara en secreto el raw_value con el threshold y devuelve True o False
    if pin_tactil.value:
        # EL JUICIO DIGITAL ES 1 (Tocado)
        ib.pixel = (0, 0, 255) # LED Azul
        
        # Reacción en la matriz: Dibujamos una "X" expansiva
        idea.matrix.fill(0)
        for i in range(5):
            idea.matrix[i, i] = 1         # Diagonal principal
            idea.matrix[i, 4 - i] = 1     # Diagonal inversa
        idea.matrix.show()
        
    else:
        # EL JUICIO DIGITAL ES 0 (En reposo)
        ib.pixel = (0, 0, 0) # LED Apagado
        
        # Reacción en la matriz: Un punto central solitario
        idea.matrix.fill(0)
        idea.matrix[2, 2] = 1
        idea.matrix.show()
        
    # Pequeña pausa para no saturar el bus y poder ver los cambios
    time.sleep(0.1)
