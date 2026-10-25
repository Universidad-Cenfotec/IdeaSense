"""
statemachine — máquina de estados mínima para CircuitPython
===========================================================

Cada estado es una función sin argumentos que ejecuta su comportamiento y
devuelve el nombre del próximo estado. step() ejecuta el estado actual.

Uso:
    from statemachine import StateMachine

    def rojo():
        ...
        return "VERDE"

    sm = StateMachine("ROJO")
    sm.add_state("ROJO", rojo)
    sm.add_state("VERDE", verde)
    while True:
        sm.step()
        time.sleep(0.05)

Instalación: copiar este archivo a /lib/statemachine.py en la IdeaBoard
(en minúscula: los programas lo importan como `from statemachine import ...`).

Autoría: Tomás de Camino Beck, Ph.D., Fiorella Pérez, Aylin Salas y
Gabriela Urbina Hernández — Universidad CENFOTEC
"""

class StateMachine:
    def __init__(self, initial_state):
        # 1. Estado interno actual
        self.current_state = initial_state
        
        # 2. Diccionario estado -> función
        self.state_actions = {}

    # 3. Método para agregar asociaciones estado-función
    def add_state(self, state, action):
        """
        state: cualquier objeto hashable (str, int, enum)
        action: función que implementa el comportamiento del estado
                y retorna el próximo estado
        """
        self.state_actions[state] = action

    def step(self):
        """
        Ejecuta la función asociada al estado actual
        y avanza al siguiente estado.
        """
        if self.current_state not in self.state_actions:
            return  # estado sin comportamiento definido

        next_state = self.state_actions[self.current_state]()
        self.current_state = next_state
