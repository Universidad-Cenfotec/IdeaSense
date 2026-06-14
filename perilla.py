# Fiorella Pérez
#Universidad Cenfotec

import board
import time
from ideaboard import IdeaBoard
from ideasense import IdeaSense

# Inicializar placas
ib = IdeaBoard()
idea = IdeaSense()

# Pin IO33 como entrada analógica (ADC)
perilla = ib.AnalogIn(board.IO33)

print("Gira el potenciómetro para llenar la matriz.")

while True:
    # Leer potenciómetro
    valor_crudo = perilla.value
    
    # Mapear valor (ajustado a 60000 por caída física) a 25 LEDs
    leds_activos = int((valor_crudo / 60000.0) * 25)
    
    # Limitar estrictamente entre 0 y 25
    leds_activos = max(0, min(25, leds_activos))
    
    # Limpiar matriz
    idea.matrix.fill(0)
    
    # Encender LEDs secuencialmente
    for i in range(leds_activos):
        columna = i % 5  # Coordenada X
        fila = i // 5    # Coordenada Y
        idea.matrix[columna, fila] = 1
        
    idea.matrix.show()
    
    # Cambiar LED de Azul (0) a Rojo (Máximo)
    intensidad_rojo = int((valor_crudo / 60000.0) * 255)
    intensidad_rojo = max(0, min(255, intensidad_rojo))
    intensidad_azul = 255 - intensidad_rojo
    
    ib.pixel = (intensidad_rojo, 0, intensidad_azul)
    
    time.sleep(0.05) # Pausa
