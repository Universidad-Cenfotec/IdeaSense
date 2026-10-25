# Pines de la IdeaBoard

Combinan la IdeaSense con entradas conectadas a los pines de la IdeaBoard.

| Archivo | Ejemplo | Qué hace | Conceptos | Autoría |
| :--- | :--- | :--- | :--- | :--- |
| [`perilla.py`](perilla.py) | Perilla | Un potenciómetro en IO33 enciende de 0 a 25 LEDs y pasa el LED RGB de azul a rojo. | `ib.AnalogIn` | Fiorella Pérez |
| [`tactil.py`](tactil.py) | Interfaz táctil | Al tocar IO4 se dibuja una X; en reposo, un punto. | `touchio.TouchIn` | Fiorella Pérez |
| [`mascota.py`](mascota.py) | Mascota virtual | Una carita dormida despierta al tocar IO4. | `touchio.TouchIn`, animación | Fiorella Pérez |

## Cómo ejecutar

1. Conectar la IdeaBoard con la IdeaSense por USB.
2. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) en Chrome o Edge y presionar *Connect*.
3. Pegar el código del ejemplo y ejecutarlo con `Ctrl+R` (o guardarlo como `code.py`).

## Hardware adicional

**Conexiones**

| Ejemplo | Conexión |
| :--- | :--- |
| `perilla.py` | Potenciómetro de 10 kΩ: extremos a 3.3 V y GND, pin central a **IO33**. |
| `tactil.py`, `mascota.py` | Un cable, clip o papel aluminio en **IO4** (pin táctil). |

Otros pines táctiles: IO27, IO32, IO33. Otros pines analógicos: IO32, IO34, IO35, IO36, IO39.

[← Volver a la lista de ejemplos](../README.md)
