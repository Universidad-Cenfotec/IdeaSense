"""
Carga de red XOR entrenada
==========================

Carga los pesos guardados en /xor.nn por xor_training.py y muestra las
predicciones para las cuatro entradas de XOR.

Hardware : IdeaBoard
Controles: Ninguno; ver la consola.
Usa      : mlp.FastMLP (ulab)
Autoría  : Tomás de Camino Beck, Ph.D. — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, pegar este código y ejecutarlo (Ctrl+R) o
guardarlo como code.py en la tarjeta.
"""

from mlp import FastMLP

net = FastMLP(
    [2,4,1],
    learning_rate=0.3
)

dataset = [

    ([0,0],[0]),
    ([0,1],[1]),
    ([1,0],[1]),
    ([1,1],[0])

]

net.load("/xor.nn")

for x,y in dataset:

    print(
        x,
        net.predict(x)
    )
