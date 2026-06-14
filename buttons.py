# Fiorella Pérez
# Universidad Cenfotec

import time
from ideaboard import IdeaBoard
from ideasense import IdeaSense

# Inicializar placas
ib = IdeaBoard()
idea = IdeaSense()

print("Presiona el botón izquierdo (A), central (B) o derecho (C)")

while True:
    idea.matrix.fill(0) # Limpiar matriz
    
    # Botón 1 (Índice 0): Letra 'A'
    if idea.held[0]:
        ib.pixel = (0, 255, 0) # Verde
        # Coordenadas que forman la letra A en 5x5
        letra_a = [(1,0),(2,0),(3,0), (0,1),(4,1), (0,2),(1,2),(2,2),(3,2),(4,2), (0,3),(4,3), (0,4),(4,4)]
        for x, y in letra_a:
            idea.matrix[x, y] = 1
            
    # Botón 2 (Índice 1): Letra 'B'
    elif idea.held[1]:
        ib.pixel = (0, 0, 255) # Azul
        # Coordenadas que forman la letra B en 5x5
        letra_b = [(0,0),(1,0),(2,0),(3,0), (0,1),(4,1), (0,2),(1,2),(2,2),(3,2), (0,3),(4,3), (0,4),(1,4),(2,4),(3,4)]
        for x, y in letra_b:
            idea.matrix[x, y] = 1
            
    # Botón 3 (Índice 2): Letra 'C'
    elif idea.held[2]:
        ib.pixel = (255, 0, 0) # Rojo
        # Coordenadas que forman la letra C en 5x5
        letra_c = [(1,0),(2,0),(3,0), (0,1),(4,1), (0,2), (0,3),(4,3), (1,4),(2,4),(3,4)]
        for x, y in letra_c:
            idea.matrix[x, y] = 1
            
    # Ningún botón presionado: Apagado
    else:
        ib.pixel = (0, 0, 0)

    idea.matrix.show()
    time.sleep(0.1) # Pausa
