# Sistemas y evolución

Ejemplos de cibernética y computación evolutiva para discutir en clase: sistemas cuyo comportamiento surge de reglas simples.

| Archivo | Ejemplo | Qué hace | Conceptos | Autoría |
| :--- | :--- | :--- | :--- | :--- |
| [`ashby.py`](ashby.py) | Máquina de Ashby | Máquina de estados finitos con 52 estados: A y C cambian las entradas y la matriz muestra dos "lámparas" de salida. ¿Puede el estudiante descubrir la regla solo observando? (problema de la caja negra de W. Ross Ashby). | `idea.events`, operaciones de bits | Tomás de Camino Beck |
| [`algoritmo_genetico.py`](algoritmo_genetico.py) | Algoritmo genético | 20 patrones 5×5 evolucionan por selección, cruce y mutación; la aptitud depende de la luz del ambiente. | `random`, `idea.light` | Tomás de Camino Beck |

## Cómo ejecutar

1. Conectar la IdeaBoard con la IdeaSense por USB.
2. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) en Chrome o Edge y presionar *Connect*.
3. Pegar el código del ejemplo y ejecutarlo con `Ctrl+R` (o guardarlo como `code.py`).

## Notas

- En `algoritmo_genetico.py`, cambiar `MUTATION_RATE` y comparar qué tan rápido se adapta la población.
- Proponer otra función de aptitud (por ejemplo, patrones simétricos).

[← Volver a la lista de ejemplos](../README.md)
