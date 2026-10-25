# Matriz y botones

Primeros pasos con la matriz LED 5×5 y los tres botones (A, B, C) de la IdeaSense.

| Archivo | Ejemplo | Qué hace | Conceptos | Autoría |
| :--- | :--- | :--- | :--- | :--- |
| [`botones_letras.py`](botones_letras.py) | Botones con letras | Mantener A, B o C muestra esa letra y cambia el color del LED RGB. | `idea.held`, `ib.pixel` | Fiorella Pérez |
| [`space_invaders.py`](space_invaders.py) | Íconos Space Invaders | Seis íconos 5×5 y la función `draw_icon()`. Ejecutado solo muestra una animación; guardado en `/lib` se puede importar desde otros programas. | listas 5×5, `__name__` | Tomás de Camino Beck |
| [`tetris.py`](tetris.py) | Mini Tetris | A/B mueven la pieza, C la rota. Las filas completas desaparecen. | `idea.pressed`, colisiones | Tomás de Camino Beck |

## Cómo ejecutar

1. Conectar la IdeaBoard con la IdeaSense por USB.
2. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) en Chrome o Edge y presionar *Connect*.
3. Pegar el código del ejemplo y ejecutarlo con `Ctrl+R` (o guardarlo como `code.py`).

## Notas

- Dibujar tu inicial o un emoji propio con una lista 5×5.
- En `tetris.py`, aumentar la velocidad cada vez que se borra una fila.

[← Volver a la lista de ejemplos](../README.md)
