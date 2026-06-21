# 📟 Edge-Morse-Classifier: Traductor Morse con Inteligencia Artificial (CircuitPython)

Este proyecto es un sistema interactivo de **Edge AI** desarrollado bajo el ecosistema de **CircuitPython**. El núcleo del proyecto se basa en la combinación de la placa de desarrollo **IdeaBoard** y, de manera fundamental, el escudo de sensores **IdeaSense**. 

Utilizando el sensor de movimiento integrado en el **IdeaSense**, el sistema captura gestos físicos del usuario en tiempo real, los clasifica como "puntos" o "rayas" de código Morse mediante una red neuronal embebida (MLP) y los traduce a caracteres alfabéticos, utilizando su matriz de LED incorporada como la interfaz de usuario principal.

---

## 🛠️ El Rol Crítico de IdeaSense en el Hardware

El hardware **IdeaSense** es el pilar sensorial y visual del proyecto. A diferencia de un desarrollo emulado o basado en botones estándar, este sistema exprime las capacidades nativas del módulo:

* **Módulo IMU (Acelerómetro y Giroscopio):** Captura las aceleraciones físicas y velocidades angulares en los ejes $X, Y, Z$. Estos datos puros de telemetría son el alimento directo del modelo de IA.
* **Matriz LED Integrada ($5 \times 5$):** Funciona como la pantalla principal del sistema. Renderiza animaciones fluidas en tiempo real para dar *feedback* inmediato del tipo de movimiento detectado, confirmaciones de éxito (`✓`), errores (`X`) y la reproducción final de los caracteres traducidos.

---

## 🧠 Flujo de Trabajo y Entrenamiento (CRCibernetica IdeaAI)

El corazón de la clasificación no se programó a mano con reglas fijas (`if/else`), sino que se obtuvo mediante un pipeline de Inteligencia Artificial utilizando **CRCibernetica IdeaAI** (una plataforma web intuitiva optimizada para capturar señales analógicas de sensores inerciales):

1. **Captura de Datos con IdeaSense:** Conectando el módulo, se recolectaron las muestras reales de los sensores de movimiento en dos estados gestuales específicos: **"Golpe-Punto"** (movimientos rápidos y secos detectados por el acelerómetro) y **"Nada-Raya"** (movimientos prolongados o estáticos).
2. **Extracción de Características:** Cada ráfaga de movimiento del **IdeaSense** se dividió en ventanas de tiempo de **25 lecturas (WINDOW = 25)**. Para cada ventana, la plataforma calculó de forma automática métricas estadísticas complejas (medias, desviaciones estándar, valores mínimos/máximos y cruces por cero de los 6 ejes del sensor).
3. **Entrenamiento y Exportación:** **IdeaAI** entrenó una red neuronal densa (Multilayer Perceptron). Al finalizar, la plataforma exportó directamente los parámetros de normalización, los pesos de las capas (`W1`, `W2`) y los sesgos (`B1`, `B2`) estructurados en listas nativas de Python para ser procesados directamente en el microcontrolador.

> 💡 **Nota de implementación (Zero-Dependency):** A diferencia de las soluciones que dependen de runtimes complejos de TinyML, este modelo se ejecuta mediante operaciones aritméticas puras a través de las funciones `extract_features()`, `dense()` y `predict()` escritas directamente en el script a partir de los datos recolectados por el **IdeaSense**. Esto optimiza drásticamente el uso de memoria RAM y elimina por completo las librerías pesadas de Machine Learning.

---

## 🚀 Características Principales del Sistema

* **Edge AI Nativo:** Clasificación local instantánea ejecutada mediante operaciones algebraicas directas en CircuitPython, procesando la telemetría del **IdeaSense** sin requerir frameworks externos.
* **Diccionario Alfabético Corregido:** Menú por consola ordenado de forma estrictamente alfabética (**A-Z**) invirtiendo la indexación de símbolos Morse para una lectura limpia del mapeo.
* **Interfaz de Usuario en Matriz LED:** El **IdeaSense** dibuja de forma interactiva patrones específicos para guiar al usuario sin necesidad de pantallas externas.
* **Persistencia en Almacenamiento Flash:** Al mantener presionado el combo de botones A+B, se realiza un registro automático de las palabras en un archivo local llamado `registro_morse.csv` acompañado de una estampa de tiempo (`time.localtime()`).
* **Freno Antirrebote por Software:** Implementación de lógica por banderas (`ya_guardado_combo`) y delays estratégicos para mitigar la alta velocidad del bucle principal y evitar registros duplicados o lecturas corruptas.

---

## 📁 Estructura del Repositorio y Descripción de Archivos

```text
Morse_Classifier/
├── README.md               <-- Documentación principal del proyecto
└── code.py                 <-- Script unificado de ejecución (Firmware, interfaz IdeaSense y modelo embebido)
