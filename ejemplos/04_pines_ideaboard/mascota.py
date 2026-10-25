"""
Mascota virtual táctil
======================

Una carita duerme en la matriz y despierta (sonríe) cuando se toca el pin IO4.

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Tocar el pin IO4.
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

# Inicialización de hardware
ib = IdeaBoard()
idea = IdeaSense()
toque = touchio.TouchIn(board.IO4) # Configura IO4 como pin capacitivo

def dibujar_durmiendo():
    idea.matrix.fill(0) # Apaga matriz
   
    # Ojos cerrados
    idea.matrix[0, 1] = 1; idea.matrix[1, 1] = 1  
    idea.matrix[3, 1] = 1; idea.matrix[4, 1] = 1  
    
    # Boca en reposo
    idea.matrix[1, 3] = 1
    idea.matrix[2, 3] = 1
    idea.matrix[3, 3] = 1
    
    idea.matrix.show() # Actualiza pantalla

def dibujar_despierto():
    idea.matrix.fill(0)
  
    # Ojos abiertos
    idea.matrix[1, 1] = 1
    idea.matrix[3, 1] = 1
    
    # Sonrisa
    idea.matrix[0, 3] = 1  
    idea.matrix[1, 4] = 1  
    idea.matrix[2, 4] = 1  
    idea.matrix[3, 4] = 1  
    idea.matrix[4, 3] = 1  
    
    idea.matrix.show()

print("Mascota ¡Toca el pin IO4 para despertarla!")

while True:
    if toque.value:
        # Tocado: Feliz
        ib.pixel = (0, 255, 0) # Verde
        dibujar_despierto()
    else:
        # Sin tocar: Durmiendo 
        ib.pixel = (10, 0, 10) # Morado
        dibujar_durmiendo()
        
    time.sleep(0.1) # Evita saturar el procesador
