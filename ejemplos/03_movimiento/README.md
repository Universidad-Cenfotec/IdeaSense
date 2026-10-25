# Movimiento

Uso del acelerómetro del LSM6DS3TR‑C para detectar la inclinación de la tarjeta. `idea.accel` devuelve `(ax, ay, az)` en m/s²; con la tarjeta plana y quieta, `az` ≈ 9.8.

| Archivo | Ejemplo | Qué hace | Conceptos | Autoría |
| :--- | :--- | :--- | :--- | :--- |
| [`flechas_acelerometro.py`](flechas_acelerometro.py) | Flechas | Dibuja una flecha hacia el lado de la inclinación, un cuadro boca arriba y una X boca abajo. Generado originalmente con IdeaScratch. | `idea.accel`, umbrales | Tomás de Camino Beck |
| [`gota.py`](gota.py) | Gota que rueda | Un punto se desplaza hacia donde se inclina la tarjeta. | `idea.accel`, `clamp()` | Tomás de Camino Beck |
| [`inclinacion.py`](inclinacion.py) | Nivel de burbuja | Calibra al inicio y dibuja una flecha que indica cómo nivelar la tarjeta. | calibración, vectores, `math.sqrt` | Tomás de Camino Beck |

## Cómo ejecutar

1. Conectar la IdeaBoard con la IdeaSense por USB.
2. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) en Chrome o Edge y presionar *Connect*.
3. Pegar el código del ejemplo y ejecutarlo con `Ctrl+R` (o guardarlo como `code.py`).

## Notas

- Imprimir `idea.accel` e inclinar la tarjeta para descubrir qué eje es cuál.
- Cambiar el umbral `th` y observar el efecto del ruido del sensor.
- Detectar una sacudida: `math.sqrt(ax*ax + ay*ay + az*az)` lejos de 9.8.

[← Volver a la lista de ejemplos](../README.md)
