# IdeaSense Explorer AI & Gamepad BLE

Esta herramienta integra telemetría inalámbrica por **Web Bluetooth (BLE)** a 25 Hz, control mediante los botones físicos de la IdeaBoard (`idea.held`) para simulaciones de juegos 2D, matriz LED interactiva y entrenamiento de IA.

-# IdeaSense Explorer AI & Gamepad BLE

Esta herramienta integra telemetría inalámbrica por **Web Bluetooth (BLE)** a 25 Hz, control mediante los botones físicos de la IdeaBoard (`idea.held`) para simulaciones de juegos 2D, matriz LED interactiva y entrenamiento de IA.

---

## Estructura de Archivos

- `codigos/index.html`: Aplicación web interactiva (Dashboard, Juego Arcade de Carritos 2D y AI Lab).
- `codigos/code.py`: Firmware en CircuitPython para grabar en la tarjeta IdeaBoard (ESP32).

---

## Guía de Instalación y Uso

1. **Grabar el Firmware:**
   - Copia el archivo `codigos/code.py` en la unidad de la tarjeta IdeaBoard (o mediante [IdeaCode](https://ideacode.crcibernetica.com/)).
   - Asegúrate de tener instaladas las librerías `ideaboard`, `ideasense` y `adafruit_ble` en la tarjeta.

2. **Ejecutar la Aplicación Web:**
   - Abre `codigos/index.html` en Chrome o Edge.
   - Presiona el botón **"Conectar IdeaBoard"** y selecciona tu tarjeta BLE (`IdeaBoard-Explorer-AI`).

3. **Controles del Simulador de Carritos:**
   - **Botón A (`idea.held[0]`):** Mueve el carrito a la izquierda.
   - **Botones B / C (`idea.held[1]` / `idea.held[2]`):** Mueven el carrito a la derecha.

## Estructura de Archivos

- `codigos/index.html`: Aplicación web interactiva (Dashboard, Juego Arcade de Carritos 2D y AI Lab).
- `codigos/code.py`: Firmware en CircuitPython para grabar en la tarjeta IdeaBoard (ESP32).

---

## Guía de Instalación y Uso

1. **Grabar el Firmware:**
   - Copia el archivo `codigos/code.py` en la unidad de la tarjeta IdeaBoard (o mediante [IdeaCode](https://ideacode.crcibernetica.com/)).
   - Asegúrate de tener instaladas las librerías `ideaboard`, `ideasense` y `adafruit_ble` en la tarjeta.

2. **Ejecutar la Aplicación Web:**
   - Abre `codigos/index.html` en Chrome o Edge.
   - Presiona el botón **"Conectar IdeaBoard"** y selecciona tu tarjeta BLE (`IdeaBoard-Explorer-AI`).

3. **Controles del Simulador de Carritos:**
   - **Botón A (`idea.held[0]`):** Mueve el carrito a la izquierda.
   - **Botones B / C (`idea.held[1]` / `idea.held[2]`):** Mueven el carrito a la derecha.
