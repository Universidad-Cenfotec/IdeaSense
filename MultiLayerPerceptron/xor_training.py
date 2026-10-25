"""
Entrenamiento XOR
=================

Entrena un FastMLP [2, 4, 1] para aprender la función XOR directamente en la
IdeaBoard y guarda los pesos en /xor.nn. Requiere mlp.py en la tarjeta.
Nota: para escribir /xor.nn el sistema de archivos debe ser escribible por el
programa (ver README de la carpeta).

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

for epoch in range(5000):

    for x,y in dataset:
        net.train(x,y)
    
    print(epoch)

for x,y in dataset:

    print(
        x,
        net.predict(x)
    )
net.save("/xor.nn")
print("grabado")
