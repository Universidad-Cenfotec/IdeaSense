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
