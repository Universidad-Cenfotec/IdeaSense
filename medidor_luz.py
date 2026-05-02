import board
from ideaboard import IdeaBoard
from ideasense import IdeaSense
from time import sleep

# Inicialización
ib = IdeaBoard()
idea = IdeaSense()

idea.matrix.fill(0)
idea.matrix.show()

print("Iniciando Medidor de Luz (Alerta Amarilla > 800)...")

while True:
    # 1. Leer la luz de forma segura
    lectura_luz = idea.light
    
    if isinstance(lectura_luz, tuple):
        valor_luz = lectura_luz[0]
    else:
        valor_luz = lectura_luz

    print('Luz actual: ' + str(valor_luz))

    # Limpiamos la matriz antes de dibujar el nuevo estado
    idea.matrix.fill(0) 

    # 2. Lógica de estados según el nivel de luz
    if valor_luz > 800:
        # --- ESTADO DE LUZ ALTA ---
        idea.matrix.fill(1)       # Enciende todos los LEDs de la matriz de golpe
        ib.pixel = (100, 100, 0)  # Led Amarillo
        
    else:
        # --- ESTADO NORMAL / BAJO ---
        if valor_luz > 300:
            ib.pixel = (0, 50, 0) # Verde
        else:
            ib.pixel = (50, 0, 0) # Rojo
            
        # Gráfico de barras proporcional (escalado a 800 como tope)
        filas_a_encender = int((valor_luz / 800.0) * 5)
        filas_a_encender = max(0, min(5, filas_a_encender))
        
        for y in range(filas_a_encender):
            for x in range(5):
                idea.matrix[x, 4 - y] = 1 
                
    # 3. Mostrar los cambios en la matriz
    idea.matrix.show() 
    
    sleep(0.1)
