# ----------------------------------------
# Universidad Cenfotec
# Ph. Tomás de Camino Beck
# Fiorella Perez
# Aylin Salas
# Gabriela Urbina Hernández
# ----------------------------------------

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
