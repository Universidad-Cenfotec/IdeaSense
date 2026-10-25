# Sensores ambientales

Lectura de luz (LTR‑303) y temperatura (SHT30) y diferentes formas de visualizarlas en la matriz.

| Archivo | Ejemplo | Qué hace | Conceptos | Autoría |
| :--- | :--- | :--- | :--- | :--- |
| [`medidor_luz.py`](medidor_luz.py) | Medidor de luz | Tres niveles de luz en la matriz; por encima de 800 se enciende todo y el LED se pone amarillo. | `idea.light` | Fiorella Pérez |
| [`temp_bargraph.py`](temp_bargraph.py) | Gráfico de temperatura | Una barra nueva por segundo, entre 20 y 30 °C. A/C desplazan el gráfico. | `idea.temp`, búfer 5×5 | Tomás de Camino Beck |
| [`temp_scrolling.py`](temp_scrolling.py) | Temperatura desplazable | Texto como `24.5C` que se desplaza por la matriz con una fuente propia. | `idea.temp`, fuentes 5×5 | Tomás de Camino Beck |

## Cómo ejecutar

1. Conectar la IdeaBoard con la IdeaSense por USB.
2. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) en Chrome o Edge y presionar *Connect*.
3. Pegar el código del ejemplo y ejecutarlo con `Ctrl+R` (o guardarlo como `code.py`).

## Notas

- Los valores de luz dependen del aula: imprimir `idea.light` y ajustar los umbrales.
- Cambiar `TEMP_MIN` y `TEMP_MAX` en `temp_bargraph.py` para ver cambios más pequeños.
- Hacer un gráfico de humedad con `idea.humid`.
- Para mediciones con gráficos y CSV, usar [IdeaSense Ciencias](https://universidad-cenfotec.github.io/IdeaSense/ideaciencia/).

[← Volver a la lista de ejemplos](../README.md)
